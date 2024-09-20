import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import openai

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


# Función para generar visualizaciones utilizando Plotly
def recommend_and_plot(df):
    st.subheader("Visualizaciones Recomendadas")
    analysis = analyze_data(df)

    # Parámetros configurables
   # hist_bins = st.slider("Número de bins para histogramas", min_value=10, max_value=100, value=30)
   # scatter_size = st.slider("Tamaño de los puntos en el gráfico de dispersión", min_value=5, max_value=50, value=10)
    x_axis = st.selectbox("Selecciona la columna para el eje X", df.columns)
    y_axis = st.selectbox("Selecciona la columna para el eje Y", df.columns)

    for column, col_type in analysis.items():
        if col_type == 'numeric':
            # Aplicar el parámetro configurable 'hist_bins' para el histograma
            fig_hist = px.histogram(df, x=column, nbins=hist_bins, title=f'Histograma de {column}')
            st.plotly_chart(fig_hist)

            fig_box = px.box(df, y=column, title=f'Diagrama de caja de {column}')
            st.plotly_chart(fig_box)

            # Verificar si el usuario seleccionó las columnas para el gráfico de dispersión
            if x_axis and y_axis:
                # Aplicar el parámetro configurable 'scatter_size' para el gráfico de dispersión
                fig_scatter = px.scatter(df, x=x_axis, y=y_axis, size_max=scatter_size, title=f'Gráfico de dispersión de {x_axis} vs {y_axis}')
                st.plotly_chart(fig_scatter)

        elif col_type == 'categorical':
            fig_count = px.bar(df[column].value_counts().reset_index(), x='index', y=column, title=f'Conteo de {column}')
            st.plotly_chart(fig_count)

            fig_prop = px.bar(df[column].value_counts(normalize=True).reset_index(), x='index', y=column,
                              title=f'Proporciones de {column}', labels={column: 'Porcentaje'})
            st.plotly_chart(fig_prop)

        elif col_type == 'datetime':
            fig_trend = px.line(df, x=column, y=df[column].value_counts().sort_index(), title=f'Tendencia temporal de {column}')
            st.plotly_chart(fig_trend)

            fig_cumsum = px.line(df, x=column, y=df[column].value_counts().sort_index().cumsum(),
                                 title=f'Cambio acumulativo de {column} a lo largo del tiempo')
            st.plotly_chart(fig_cumsum)


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
