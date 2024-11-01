import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import openai

st.set_page_config(
    page_title="VisBot - Visualization Recommender with IA",
    page_icon="https://raw.githubusercontent.com/disenodc/visbot/main/bot_2.ico",
)

# Función para leer datos
def read_data(file_path_or_url):
    if isinstance(file_path_or_url, str) and file_path_or_url.startswith('http'):
        response = requests.get(file_path_or_url)
        content_type = response.headers.get('Content-Type')

        if 'application/json' in content_type:
            df = pd.read_json(response.content)
        elif 'text/csv' in content_type:
            # Determine the delimiter by checking for ';' in the file content
            first_line = response.text.splitlines()[0]
            delimiter = ';' if ';' in first_line else ','
            df = pd.read_csv(file_path_or_url, delimiter=delimiter)
        elif 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' in content_type:
            df = pd.read_excel(file_path_or_url)
        else:
            raise ValueError("File format not supported or content could not be identified.")
    else:
        # For local files, check extension and handle accordingly
        if file_path_or_url.name.endswith('.csv'):
            # Determine delimiter by reading the first line of the file
            first_line = file_path_or_url.readline().decode('utf-8')
            file_path_or_url.seek(0)  # Reset pointer after reading first line
            delimiter = ';' if ';' in first_line else ','
            df = pd.read_csv(file_path_or_url, delimiter=delimiter)
        elif file_path_or_url.name.endswith('.xlsx'):
            df = pd.read_excel(file_path_or_url)
        elif file_path_or_url.name.endswith('.json'):
            df = pd.read_json(file_path_or_url)
        else:
            raise ValueError("Unsupported file format.")

    return df.head()

# Función para obtener recomendaciones de visualización de OpenAI utilizando GPT-4
def get_openai_recommendation(df, api_key, model="gpt-4-turbo"):
    description = f"The data set has {df.shape[0]} rows and {df.shape[1]} columns. "
    for column in df.columns:
        description += f"The '{column}' column is {df[column].dtype} type, "
        if pd.api.types.is_numeric_dtype(df[column]):
            description += f"and contains numerical values ​​ranging from {df[column].min()} to {df[column].max()}. "
        elif pd.api.types.is_categorical_dtype(df[column]) or df[column].nunique() < 10:
            description += f"and contains {df[column].nunique()} unique categories. "
        elif pd.api.types.is_datetime64_any_dtype(df[column]):
            description += f"and contains time data ranging from {df[column].min()} to {df[column].max()}. "

    openai.api_key = api_key

    # Usamos GPT-4 o GPT-4-turbo
    response = openai.ChatCompletion.create(
        model= "gpt-4-turbo",  # Cambiamos a gpt-4 o gpt-4-turbo
        messages=[
            {"role": "system", "content": "You are an expert assistant in data analysis, specialist in visualization."},
            {"role": "user",
             "content": f"I have a data set. {description} What type of visualizations would you recommend to and Exploratory Data Analysis from this data? Please describe from and statistical view"}
        ],
        max_tokens=500  # Aumentamos los tokens si se desea más contexto
    )

    return response['choices'][0]['message']['content']

# Función para generar visualizaciones
def recommend_and_plot(df):
    #st.subheader("Visualizaciones Recomendadas")
    # Parámetros configurables en la barra lateral
    st.sidebar.header("Configuration")

    try:
        # Selectbox para seleccionar las columnas de los ejes X, Y y Z
        x_axis = st.sidebar.selectbox("Select the column for the X axis", df.columns)
        y_axis = st.sidebar.selectbox("Select the column for the Y axis", df.columns)
        z_axis = st.sidebar.selectbox("Select the column for the Z axis", df.columns)
        z_axis = None


        if chart_type in ["3D Scatter Chart", "Stacked Bar Chart"]:
            z_axis = st.sidebar.selectbox("Select the column for the Z axis", df.columns)

        # Parámetros adicionales
        st.sidebar.subheader("Parámetros configurables")
        hist_bins = st.sidebar.slider("Número de bins para histogramas", min_value=10, max_value=100, value=30)
        scatter_size = st.sidebar.slider("Tamaño de los puntos en el gráfico de dispersión", min_value=5, max_value=50, value=10)

        # Verificar si las columnas seleccionadas existen en el DataFrame
        if x_axis not in df.columns or y_axis not in df.columns or z_axis not in df.columns:
            raise ValueError(f"Una de las columnas seleccionadas no es válida. Columnas esperadas: {list(df.columns)}.")

        # Generar gráfico de dispersión (ejemplo simple)
        fig_scatter = px.bar(df, x=x_axis, y=y_axis, title=f'Bar chart from {x_axis} vs {y_axis}')
        #fig_scatter = px.scatter(df, x=x_axis, y=y_axis, size_max=scatter_size, title=f'Scatter Plot from {x_axis} vs {y_axis}')
        st.plotly_chart(fig_scatter)

    except ValueError as e:
        # Mostrar advertencia si ocurre un error relacionado con las columnas
        st.warning(f"Warning: {str(e)}")
    except Exception as e:
        # Cualquier otro error no previsto
        st.error(f"Ha ocurrido un error inesperado: {str(e)}")

# Función principal
def main():
    # Interfaz de usuario con Streamlit
    st.title("VisBot - TEST - Visualization Recommender with iA")

    # Input para la clave API de OpenAI
    api_key = st.text_input("Enter your OpenAI API Key to continue", type="password")

    # Input para URL
    url_input = st.text_input("Enter the URL of the data file")

    # Input para cargar un archivo local
    uploaded_file = st.file_uploader("Load your CSV, XLSX or JSON file", type=["csv", "xlsx", "json"])

    df = None

    # Leer el archivo o URL
    if api_key:
        if url_input:
            try:
                df = read_data(url_input)
            except ValueError as e:
                st.error(f"Error when processing data from URL: {e}")
        elif uploaded_file is not None:
            try:
                df = read_data(uploaded_file)
            except ValueError as e:
                st.error(f"Error processing file: {e}")

        if df is not None:
            st.write(df.head())  # Mostrar las primeras filas del DataFrame

            # Generar y mostrar las recomendaciones de visualización de OpenAI
            st.subheader("iA Recommended Visualizations")
            try:
                recommendation = get_openai_recommendation(df, api_key)
                st.markdown(recommendation)  # Muestra las recomendaciones de GPT-4
            except Exception as e:
                st.error(f"Error getting OpenAI recommendations: {str(e)}")

            # Selección de tipo de gráfico (chart_type) y variables para los ejes
            chart_type = st.sidebar.selectbox(
                "Select chart type",
                [
                    "Scatter Chart", "Bar Chart", "Stacked Bar Chart", 
                    "Histogram","Line Chart", "Area Chart",  "Boxplot", "Pie chart",
                    "3D Scatter Chart",  "Violin plot", "Heat map",
                    "Geospatial scatter map", "Choropleth map", "Sun diagram"
                ]
            )

            x_axis = st.sidebar.selectbox("Select the column for the X axis", df.columns)
            y_axis = st.sidebar.selectbox("Select the column for the Y axis", df.columns)
            z_axis = None
            if chart_type in ["3D Scatter Chart", "Stacked Bar Chart"]:
                z_axis = st.sidebar.selectbox("Select column for Z axis (optional)", df.columns)

            hist_bins = st.sidebar.slider("Number of bins for histograms", min_value=10, max_value=100, value=30)
            scatter_size = st.sidebar.slider("Size of points on scatter plot", min_value=5, max_value=50, value=10)

            # Generar el gráfico seleccionado
            fig = generate_plot(df, chart_type, x_axis, y_axis, z_axis, hist_bins, scatter_size)

            # Mostrar el gráfico en la interfaz
            if fig:
                st.plotly_chart(fig)
            else:
                st.warning("Please select a chart type and valid columns.")
    else:
        st.warning("Please enter your OpenAI API Key to continue.")




# Función para generar gráficos dependiendo de los tipos de datos y gráfico seleccionado
def generate_plot(df, chart_type, x_axis=None, y_axis=None, z_axis=None, hist_bins=30, scatter_size=10):
    fig = None

    if chart_type == "Scatter Plot":
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f'Dispersión de {x_axis} vs {y_axis}', size_max=scatter_size)
    
    elif chart_type == "Bar chart":
        fig = px.bar(df, x=x_axis, y=y_axis, title=f'Bar chart from {x_axis} vs {y_axis}')
    
    elif chart_type == "Stacked Bar Chart":
        fig = px.bar(df, x=x_axis, y=y_axis, color=z_axis, title=f'Stacked Bar Chart from {x_axis} vs {y_axis} for {z_axis}', barmode='stack')
    
    elif chart_type == "Histogram":
        fig = px.histogram(df, x=x_axis, nbins=hist_bins, title=f'Histogram from {x_axis}')
    
    elif chart_type == "Line chart":
        fig = px.line(df, x=x_axis, y=y_axis, title=f'Líneas de {x_axis} vs {y_axis}')
    
    elif chart_type == "Area Chart":
        fig = px.area(df, x=x_axis, y=y_axis, title=f'Área de {x_axis} vs {y_axis}')
    
    elif chart_type == "Pie chart":
        fig = px.pie(df, names=x_axis, title=f'Pie Chart from {x_axis}')
    
    elif chart_type == "3D Scatter Plot":
        fig = px.scatter_3d(df, x=x_axis, y=y_axis, z=z_axis, title=f'Scatter plot 3D from {x_axis}, {y_axis} y {z_axis}')
    
    elif chart_type == "Boxplot":
        fig = px.box(df, x=x_axis, y=y_axis, title=f'Boxplot from {x_axis} vs {y_axis}')
    
    elif chart_type == "Violin chart":
        fig = px.violin(df, x=x_axis, y=y_axis, title=f'Violin from {x_axis} vs {y_axis}')
    
    elif chart_type == "Heat map":
        fig = px.density_heatmap(df, x=x_axis, y=y_axis, title=f'heat map from {x_axis} vs {y_axis}')
    
    elif chart_type == "Geospatial dispersion map":
        fig = px.scatter_geo(df, lat=y_axis, lon=x_axis, title=f'Geospatial dispersion map from {x_axis} y {y_axis}')
    
    elif chart_type == "Choropleth map":
        fig = px.choropleth(df, locations=x_axis, color=y_axis, title=f'Choropleth map from {x_axis} y {y_axis}')
    
    elif chart_type == "Sun diagram":
        fig = px.sunburst(df, path=[x_axis, y_axis], title=f'Sun diagram from {x_axis} y {y_axis}')
    
    return fig

# Ejecutar la función principal
if __name__ == "__main__":
    main()
