import streamlit as st
import pandas as pd
import requests
import openai

import holoviews as hv
import hvplot.pandas  # Para utilizar hvplot con Pandas
# Si panel no es requerido, asegúrate de no inicializarlo para reducir conflictos
import panel as pn
pn.config.sizing_mode = None  # Ajusta o deshabilita configuraciones de panel
from holoviews import opts

# Inicializar holoviews con bokeh y desactivar logo para reducir errores visuales
hv.extension('matplotlib')

# Inicializar panel explícitamente
pn.extension()


st.set_page_config(
    page_title="VizBot - Análisis con IA",
    page_icon="https://raw.githubusercontent.com/disenodc/vizbot/main/bot_2.ico",
)

# Configuración del logo y el título
logo_url = "https://raw.githubusercontent.com/disenodc/vizbot/main/bot_1.png"
logo_width = 100

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
            {"role": "system", "content": "Eres un asistente experto en análisis de datos de biodiversidad marina, especializado en elefantes marinos."},
            {"role": "user",
             "content": f"Tengo un conjunto de datos. {description} ¿Qué tipo de visualizaciones recomendarías para analizar estos datos? Por favor, explica por qué."}
        ],
        max_tokens=500  # Aumentamos los tokens si se desea más contexto
    )

    return response['choices'][0]['message']['content']

# Función para generar visualizaciones utilizando Holoviews
def recommend_and_plot(df):
    st.subheader("Visualizaciones Recomendadas")
    
    # Análisis de tipos de datos
    analysis = analyze_data(df)

    # Parámetros configurables
    hist_bins = st.slider("Número de bins para histogramas", min_value=10, max_value=100, value=30)
    scatter_size = st.slider("Tamaño de los puntos en el gráfico de dispersión", min_value=5, max_value=50, value=10)
    
    # Selectbox para seleccionar las columnas de los ejes X y Y
    x_axis = st.selectbox("Selecciona la columna para el eje X", df.columns)
    y_axis = st.selectbox("Selecciona la columna para el eje Y", df.columns)
    
    # Obtener los tipos de las columnas seleccionadas
    x_type = analysis.get(x_axis, 'unknown')
    y_type = analysis.get(y_axis, 'unknown')

    # Generar gráficos dependiendo de los tipos de datos seleccionados
    if x_type == 'numeric' and y_type == 'numeric':
        # Gráfico de dispersión
        fig_scatter = df.hvplot.scatter(x=x_axis, y=y_axis, size=scatter_size, title=f'Dispersión: {x_axis} vs {y_axis}')
        st.bokeh_chart(hv.render(fig_scatter))

        # Gráfico de correlación de densidad
        fig_density = df.hvplot.kde(x=x_axis, y=y_axis, title=f'Densidad: {x_axis} vs {y_axis}')
        st.bokeh_chart(hv.render(fig_density))

        # Gráfico de dispersión 3D si se tiene una tercera variable numérica
        if len(df.select_dtypes(include='number').columns) > 2:
            z_axis = st.selectbox("Selecciona la columna para el eje Z (Opcional)", df.columns)
            if z_axis:
                fig_3d = df.hvplot.scatter3d(x=x_axis, y=y_axis, z=z_axis, title=f'Dispersión 3D: {x_axis}, {y_axis}, {z_axis}')
                st.bokeh_chart(hv.render(fig_3d))

    elif x_type == 'numeric' and y_type == 'categorical':
        # Gráfico de caja (boxplot)
        fig_box = df.hvplot.box(y=x_axis, by=y_axis, title=f'Cajas: {x_axis} por {y_axis}')
        st.bokeh_chart(hv.render(fig_box))

        # Gráfico de barras con medias
        fig_bar_mean = df.groupby(y_axis)[x_axis].mean().hvplot.bar(title=f'Media de {x_axis} por {y_axis}')
        st.bokeh_chart(hv.render(fig_bar_mean))

    elif x_type == 'categorical' and y_type == 'numeric':
        # Gráfico de caja (boxplot)
        fig_box = df.hvplot.box(y=y_axis, by=x_axis, title=f'Cajas: {y_axis} por {x_axis}')
        st.bokeh_chart(hv.render(fig_box))

        # Gráfico de barras con medias
        fig_bar_mean = df.groupby(x_axis)[y_axis].mean().hvplot.bar(title=f'Media de {y_axis} por {x_axis}')
        st.bokeh_chart(hv.render(fig_bar_mean))

    elif x_type == 'categorical' and y_type == 'categorical':
        # Gráfico de barras apiladas
        fig_bar = df.groupby([x_axis, y_axis]).size().unstack().hvplot.bar(stacked=True, title=f'Barras Apiladas: {x_axis} por {y_axis}')
        st.bokeh_chart(hv.render(fig_bar))

    elif x_type == 'numeric' and y_type == 'datetime':
        # Gráfico de líneas
        fig_line = df.hvplot.line(x=y_axis, y=x_axis, title=f'Tendencia: {x_axis} sobre {y_axis}')
        st.bokeh_chart(hv.render(fig_line))

    elif x_type == 'datetime' and y_type == 'numeric':
        # Gráfico de líneas
        fig_line = df.hvplot.line(x=x_axis, y=y_axis, title=f'Tendencia: {y_axis} sobre {x_axis}')
        st.bokeh_chart(hv.render(fig_line))

    # Visualizaciones adicionales para columnas individuales
    for column, col_type in analysis.items():
        if col_type == 'numeric':
            # Histograma
            fig_hist = df[column].hvplot.hist(bins=hist_bins, title=f'Histograma: {column}')
            st.bokeh_chart(hv.render(fig_hist))

        elif col_type == 'categorical':
            # Gráfico de barras para conteo de categorías
            fig_count = df[column].value_counts().hvplot.bar(title=f'Conteo: {column}')
            st.bokeh_chart(hv.render(fig_count))

        elif col_type == 'datetime':
            # Gráfico de líneas para tendencias
            fig_trend = df.hvplot.line(x=column, y=df[column].value_counts().sort_index(), title=f'Tendencia: {column}')
            st.bokeh_chart(hv.render(fig_trend))

# Función para analizar datos
def analyze_data(df):
    analysis = {}
    for column in df.columns:
        dtype = df[column].dtype
        if pd.api.types.is_numeric_dtype(df[column]):
            analysis[column] = 'numeric'
        elif pd.api.types.is_categorical_dtype(df[column]) or df[column].nunique() < 10:
            analysis[column] = 'categorical'
        elif pd.api.types.is_datetime64_any_dtype(df[column]):
            analysis[column] = 'datetime'
        else:
            analysis[column] = 'other'
    return analysis

# Inserta Logotipo
st.markdown(
    f"""
    <div style="display: flex; align-items: center;">
        <img src="{logo_url}" width="{logo_width}" style="margin-right: 10px;">
    </div>
    """,
    unsafe_allow_html=True
)

# Interfaz de usuario con Streamlit
st.title("VizBot - Generador Automático de Visualizaciones con IA")

# Input para la clave API de OpenAI
api_key = st.text_input("Ingrese su API Key de OpenAI", type="password")

# Input para URL
url_input = st.text_input("Ingrese la URL del archivo de datos")

# Input para cargar un archivo local
uploaded_file = st.file_uploader("O cargue un archivo CSV, XLSX o JSON", type=["csv", "xlsx", "json"])

df = None

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
        st.write(df.head())  # Mostrar las primeras filas del dataframe

        # Obtener recomendaciones de OpenAI
        st.subheader("Recomendaciones basadas en IA")
        ai_recommendation = get_openai_recommendation(df, api_key)
        st.write(ai_recommendation)

        # Generar y mostrar las visualizaciones recomendadas
        recommend_and_plot(df)
else:
    st.warning("Por favor, ingrese su API Key de OpenAI para continuar.")

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #111 ;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .footer a {
        color: #34ede3;
    }
    </style>
    <div class="footer">
        Developed by: <a href="https://linktr.ee/oiradsollabec" target="_blank">Dario Ceballos</a> | Repo: <a href="https://github.com/disenodc/vizbot" target="_blank"> Github </a>
    </div>
    """,
    unsafe_allow_html=True
)
