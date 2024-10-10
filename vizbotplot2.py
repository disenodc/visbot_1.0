import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import openai

st.set_page_config(
    page_title="VizBot - Análisis con IA",
    page_icon="https://raw.githubusercontent.com/disenodc/vizbot/main/bot_2.ico",
)

# Función para leer datos
def read_data(file_path_or_url):
    if isinstance(file_path_or_url, str) and file_path_or_url.startswith('http'):
        response = requests.get(file_path_or_url)
        content_type = response.headers.get('Content-Type')

        if 'application/json' in content_type:
            df = pd.read_json(response.content)
        elif 'text/csv' in content_type:
            df = pd.read_csv(file_path_or_url)
        elif 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' in content_type:
            df = pd.read_excel(file_path_or_url)
        else:
            raise ValueError("Formato de archivo no soportado o no se pudo identificar el contenido.")
    else:
        if file_path_or_url.name.endswith('.csv'):
            df = pd.read_csv(file_path_or_url)
        elif file_path_or_url.name.endswith('.xlsx'):
            df = pd.read_excel(file_path_or_url)
        elif file_path_or_url.name.endswith('.json'):
            df = pd.read_json(file_path_or_url)
        else:
            raise ValueError("Formato de archivo no soportado.")

    return df

# Función para obtener recomendaciones de visualización de OpenAI utilizando GPT-4
def get_openai_recommendation(df, api_key, model="gpt-4-turbo"):
    description = f"El conjunto de datos tiene {df.shape[0]} filas y {df.shape[1]} columnas. "
    for column in df.columns:
        description += f"La columna '{column}' es de tipo {df[column].dtype}, "
        if pd.api.types.is_numeric_dtype(df[column]):
            description += f"y contiene valores numéricos que van desde {df[column].min()} hasta {df[column].max()}. "
        elif pd.api.types.is_categorical_dtype(df[column]) or df[column].nunique() < 10:
            description += f"y contiene {df[column].nunique()} categorías únicas. "
        elif pd.api.types.is_datetime64_any_dtype(df[column]):
            description += f"y contiene datos de tiempo que van desde {df[column].min()} hasta {df[column].max()}. "

    openai.api_key = api_key

    # Usamos GPT-4 o GPT-4-turbo
    response = openai.ChatCompletion.create(
        model= "gpt-4-turbo",  # Cambiamos a gpt-4 o gpt-4-turbo
        messages=[
            {"role": "system", "content": "Eres un asistente experto en análisis de datos de biodiversidad marina."},
            {"role": "user",
             "content": f"Tengo un conjunto de datos. {description} ¿Qué tipo de visualizaciones recomendarías para analizar estos datos? Por favor, explica por qué."}
        ],
        max_tokens=500  # Aumentamos los tokens si se desea más contexto
    )

    return response['choices'][0]['message']['content']

# Función para generar visualizaciones
def recommend_and_plot(df):
    #st.subheader("Visualizaciones Recomendadas")
    # Parámetros configurables en la barra lateral
    st.sidebar.header("Configuración")

    try:
        # Selectbox para seleccionar las columnas de los ejes X, Y y Z
        x_axis = st.sidebar.selectbox("Selecciona la columna para el eje X", df.columns)
        y_axis = st.sidebar.selectbox("Selecciona la columna para el eje Y", df.columns)
        z_axis = st.sidebar.selectbox("Selecciona la columna para el eje Z", df.columns)
        z_axis = None
        if chart_type in ["Gráfico de dispersión 3D", "Gráfico de barras apiladas"]:
            z_axis = st.sidebar.selectbox("Seleccione la columna para el eje Z (opcional)", df.columns)

        # Parámetros adicionales
        st.sidebar.subheader("Parámetros configurables")
        hist_bins = st.sidebar.slider("Número de bins para histogramas", min_value=10, max_value=100, value=30)
        scatter_size = st.sidebar.slider("Tamaño de los puntos en el gráfico de dispersión", min_value=5, max_value=50, value=10)

        # Verificar si las columnas seleccionadas existen en el DataFrame
        if x_axis not in df.columns or y_axis not in df.columns or z_axis not in df.columns:
            raise ValueError(f"Una de las columnas seleccionadas no es válida. Columnas esperadas: {list(df.columns)}.")

        # Generar gráfico de dispersión (ejemplo simple)
        fig_scatter = px.scatter(df, x=x_axis, y=y_axis, size_max=scatter_size, title=f'Gráfico de dispersión de {x_axis} vs {y_axis}')
        st.plotly_chart(fig_scatter)

    except ValueError as e:
        # Mostrar advertencia si ocurre un error relacionado con las columnas
        st.warning(f"Advertencia: {str(e)}")
    except Exception as e:
        # Cualquier otro error no previsto
        st.error(f"Ha ocurrido un error inesperado: {str(e)}")

# Función principal
def main():
    # Interfaz de usuario con Streamlit
    st.title("VizBot - TEST - Generador Automático de Visualizaciones con IA")

    # Input para la clave API de OpenAI
    api_key = st.text_input("Ingrese su API Key de OpenAI", type="password")

    # Input para URL
    url_input = st.text_input("Ingrese la URL del archivo de datos")

    # Input para cargar un archivo local
    uploaded_file = st.file_uploader("O cargue un archivo CSV, XLSX o JSON", type=["csv", "xlsx", "json"])

    df = None

    # Leer el archivo o URL
    if api_key:
        if url_input:
            try:
                df = read_data(url_input)
            except ValueError as e:
                st.error(f"Error al procesar los datos desde la URL: {e}")
        elif uploaded_file is not None:
            try:
                df = read_data(uploaded_file)
            except ValueError as e:
                st.error(f"Error al procesar el archivo: {e}")

        if df is not None:
            st.write(df.head())  # Mostrar las primeras filas del DataFrame

            # Generar y mostrar las recomendaciones de visualización de OpenAI
            st.subheader("Visualizaciones recomendadas por iA")
            try:
                recommendation = get_openai_recommendation(df, api_key)
                st.markdown(recommendation)  # Muestra las recomendaciones de GPT-4
            except Exception as e:
                st.error(f"Error al obtener las recomendaciones de OpenAI: {str(e)}")

            # Selección de tipo de gráfico (chart_type) y variables para los ejes
            chart_type = st.sidebar.selectbox(
                "Seleccione el tipo de gráfico",
                [
                    "Gráfico de dispersión", "Gráfico de dispersión 3D", "Gráfico de líneas", 
                    "Gráfico de áreas", "Gráfico de barras", "Gráfico de barras apiladas", 
                    "Histograma", "Gráfico de caja (boxplot)", "Gráfico de violín", 
                    "Gráfico de pastel (pie chart)", "Mapa de calor", "Mapa de dispersión geoespacial", 
                    "Mapa de coropletas", "Diagrama de sol"
                ]
            )

            x_axis = st.sidebar.selectbox("Selecciona la columna para el eje X", df.columns)
            y_axis = st.sidebar.selectbox("Selecciona la columna para el eje Y", df.columns)
            z_axis = None
            if chart_type in ["Gráfico de dispersión 3D", "Gráfico de barras apiladas"]:
                z_axis = st.sidebar.selectbox("Seleccione la columna para el eje Z (opcional)", df.columns)

            hist_bins = st.sidebar.slider("Número de bins para histogramas", min_value=10, max_value=100, value=30)
            scatter_size = st.sidebar.slider("Tamaño de los puntos en el gráfico de dispersión", min_value=5, max_value=50, value=10)

            # Generar el gráfico seleccionado
            fig = generate_plot(df, chart_type, x_axis, y_axis, z_axis, hist_bins, scatter_size)

            # Mostrar el gráfico en la interfaz
            if fig:
                st.plotly_chart(fig)
            else:
                st.warning("Por favor, seleccione un tipo de gráfico y columnas válidas.")
    else:
        st.warning("Por favor, ingrese su API Key de OpenAI para continuar.")




# Función para generar gráficos dependiendo de los tipos de datos y gráfico seleccionado
def generate_plot(df, chart_type, x_axis=None, y_axis=None, z_axis=None, hist_bins=30, scatter_size=10):
    fig = None

    if chart_type == "Gráfico de dispersión":
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f'Dispersión de {x_axis} vs {y_axis}', size_max=scatter_size)
    
    elif chart_type == "Gráfico de dispersión 3D":
        fig = px.scatter_3d(df, x=x_axis, y=y_axis, z=z_axis, title=f'Dispersión 3D de {x_axis}, {y_axis} y {z_axis}')
    
    elif chart_type == "Gráfico de líneas":
        fig = px.line(df, x=x_axis, y=y_axis, title=f'Líneas de {x_axis} vs {y_axis}')
    
    elif chart_type == "Gráfico de áreas":
        fig = px.area(df, x=x_axis, y=y_axis, title=f'Área de {x_axis} vs {y_axis}')
    
    elif chart_type == "Gráfico de barras":
        fig = px.bar(df, x=x_axis, y=y_axis, title=f'Barras de {x_axis} vs {y_axis}')
    
    elif chart_type == "Gráfico de barras apiladas":
        fig = px.bar(df, x=x_axis, y=y_axis, color=z_axis, title=f'Barras apiladas de {x_axis} vs {y_axis} por {z_axis}', barmode='stack')
    
    elif chart_type == "Histograma":
        fig = px.histogram(df, x=x_axis, nbins=hist_bins, title=f'Histograma de {x_axis}')
    
    elif chart_type == "Gráfico de caja (boxplot)":
        fig = px.box(df, x=x_axis, y=y_axis, title=f'Boxplot de {x_axis} vs {y_axis}')
    
    elif chart_type == "Gráfico de violín":
        fig = px.violin(df, x=x_axis, y=y_axis, title=f'Violín de {x_axis} vs {y_axis}')
    
    elif chart_type == "Gráfico de pastel (pie chart)":
        fig = px.pie(df, names=x_axis, title=f'Gráfico de pastel de {x_axis}')
    
    elif chart_type == "Mapa de calor":
        fig = px.density_heatmap(df, x=x_axis, y=y_axis, title=f'Mapa de calor de {x_axis} vs {y_axis}')
    
    elif chart_type == "Mapa de dispersión geoespacial":
        fig = px.scatter_geo(df, lat=y_axis, lon=x_axis, title=f'Mapa de dispersión geoespacial de {x_axis} y {y_axis}')
    
    elif chart_type == "Mapa de coropletas":
        fig = px.choropleth(df, locations=x_axis, color=y_axis, title=f'Mapa de coropletas basado en {x_axis} y {y_axis}')
    
    elif chart_type == "Diagrama de sol":
        fig = px.sunburst(df, path=[x_axis, y_axis], title=f'Diagrama de sol para {x_axis} y {y_axis}')
    
    return fig

# Ejecutar la función principal
if __name__ == "__main__":
    main()
