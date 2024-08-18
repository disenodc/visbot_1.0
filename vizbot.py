import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import openai


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


# Función para obtener recomendaciones de visualización de OpenAI
def get_openai_recommendation(df, api_key):
    # Generar una breve descripción de los datos
    description = f"El conjunto de datos tiene {df.shape[0]} filas y {df.shape[1]} columnas. "
    for column in df.columns:
        description += f"La columna '{column}' es de tipo {df[column].dtype}, "
        if pd.api.types.is_numeric_dtype(df[column]):
            description += f"y contiene valores numéricos que van desde {df[column].min()} hasta {df[column].max()}. "
        elif pd.api.types.is_categorical_dtype(df[column]) or df[column].nunique() < 10:
            description += f"y contiene {df[column].nunique()} categorías únicas. "
        elif pd.api.types.is_datetime64_any_dtype(df[column]):
            description += f"y contiene datos de tiempo que van desde {df[column].min()} hasta {df[column].max()}. "

    # Configura la clave API para la solicitud
    openai.api_key = api_key

    # Usar el modelo de chat con el endpoint correcto
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # También puedes usar "gpt-4" si tienes acceso
        messages=[
            {"role": "system", "content": "Eres un asistente experto en análisis de datos."},
            {"role": "user", "content": f"Tengo un conjunto de datos. {description} ¿Qué tipo de visualizaciones recomendarías para analizar estos datos? Por favor, explica por qué."}
        ],
        max_tokens=150
    )

    return response['choices'][0]['message']['content'].strip()


# Función para generar visualizaciones básicas
def recommend_and_plot(df):
    st.subheader("Visualizaciones Básicas")
    analysis = analyze_data(df)

    for column, col_type in analysis.items():
        plt.figure(figsize=(10, 6))

        if col_type == 'numeric':
            sns.histplot(df[column], kde=True)
            plt.title(f'Histograma de {column}')
            st.pyplot(plt)
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=df[column])
            plt.title(f'Diagrama de caja de {column}')
            st.pyplot(plt)

        elif col_type == 'categorical':
            sns.countplot(x=column, data=df)
            plt.title(f'Conteo de {column}')
            st.pyplot(plt)
            plt.figure(figsize=(10, 6))
            (df[column].value_counts(normalize=True) * 100).plot(kind='bar')
            plt.title(f'Proporciones de {column}')
            plt.ylabel('Porcentaje')
            st.pyplot(plt)

        elif col_type == 'datetime':
            df[column].value_counts().sort_index().plot()
            plt.title(f'Tendencia temporal de {column}')
            st.pyplot(plt)
            plt.figure(figsize=(10, 6))
            df[column].value_counts().sort_index().cumsum().plot()
            plt.title(f'Cambio acumulativo de {column} a lo largo del tiempo')
            st.pyplot(plt)


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


# Interfaz de usuario con Streamlit
st.title("VizBot - Generador Automático de Visualizaciones con IA")

# Cambiar color de fondo a azul
st.markdown(
    """
    <style>
    .stApp {
        background-color:;
        
    }
    </style>
    """,
    unsafe_allow_html=True
)

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


#Footer
# Footer con enlace a tu sitio web
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
        Developed by:  <a href="https://linktr.ee/oiradsollabec" target="_blank"> Dario Ceballos </a>
    </div>
    """,
    unsafe_allow_html=True
)