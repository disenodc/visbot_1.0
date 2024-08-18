import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests


# Función para leer datos de diferentes fuentes
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


# Función para recomendar y generar visualizaciones
def recommend_and_plot(df, analysis):
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

        elif col_type == 'numeric' and 'numeric' in analysis.values():
            for other_column, other_type in analysis.items():
                if other_type == 'numeric' and other_column != column:
                    sns.scatterplot(x=df[column], y=df[other_column])
                    plt.title(f'Dispersión entre {column} y {other_column}')
                    st.pyplot(plt)

        elif col_type == 'categorical' and 'numeric' in analysis.values():
            for other_column, other_type in analysis.items():
                if other_type == 'numeric':
                    sns.boxplot(x=df[column], y=df[other_column])
                    plt.title(f'{other_column} por categorías de {column}')
                    st.pyplot(plt)


# Interfaz de usuario con Streamlit
st.title("VizBot - Generador Automático de Visualizaciones")

# Input para URL
url_input = st.text_input("Ingrese la URL del archivo de datos")

# Input para cargar un archivo local
uploaded_file = st.file_uploader("O cargue un archivo CSV, XLSX o JSON", type=["csv", "xlsx", "json"])

df = None

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

# Si hay datos cargados, proceder con el análisis y las visualizaciones
if df is not None:
    st.write(df.head())  # Mostrar las primeras filas del dataframe
    data_analysis = analyze_data(df)
    recommend_and_plot(df, data_analysis)  # Generar y mostrar las visualizaciones recomendadas
