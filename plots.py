import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Función principal de la app
def main():
    st.title("Generador de Visualizaciones")

    # Input para cargar un archivo local
    uploaded_file = st.file_uploader("Cargue un archivo CSV, XLSX o JSON", type=["csv", "xlsx", "json"])

    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.json'):
            df = pd.read_json(uploaded_file)

        st.write(df.head())  # Mostrar las primeras filas del dataframe

        # Análisis de los tipos de columnas en el DataFrame
        analysis = analyze_data(df)

        # Selección de tipo de gráfico
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

        # Parámetros adicionales
        st.sidebar.subheader("Selección de Variables")
        x_axis = st.sidebar.selectbox("Seleccione la columna para el eje X", df.columns)
        y_axis = st.sidebar.selectbox("Seleccione la columna para el eje Y", df.columns)
        z_axis = None
        if chart_type in ["Gráfico de dispersión 3D", "Gráfico de barras apiladas"]:
            z_axis = st.sidebar.selectbox("Seleccione la columna para el eje Z (opcional)", df.columns)

        hist_bins = st.sidebar.slider("Número de bins para el histograma", min_value=10, max_value=100, value=30)
        scatter_size = st.sidebar.slider("Tamaño de los puntos para gráficos de dispersión", min_value=5, max_value=50, value=10)

        # Generar el gráfico seleccionado
        fig = generate_plot(df, chart_type, x_axis, y_axis, z_axis, hist_bins, scatter_size)

        # Mostrar el gráfico en la interfaz
        if fig:
            st.plotly_chart(fig)
        else:
            st.warning("Por favor, seleccione un tipo de gráfico y columnas válidas.")
    else:
        st.info("Cargue un archivo para comenzar a generar visualizaciones.")


# Función para analizar datos y categorizar las columnas del dataframe
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



# Ejecutar la aplicación
if __name__ == "__main__":
    main()
