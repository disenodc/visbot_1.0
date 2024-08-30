![Logo vizbot](https://raw.githubusercontent.com/disenodc/vizbot/main/bot_1.png)
# VizBot - Generador Automático de Visualizaciones interactivas con IA

- Visitar: [Sitio Web](https://vizbot-main.streamlit.app/)
- Autor: Lic. Luis Dario Ceballos. (2024). *VizBot - Generador Automático de Visualizaciones interactivas con IA*. 
- Doctorado en Informática. UAI (Universidad Abierta Interamericana), Buenos Aires-Argentina.
   CESIMAR - CENPAT - CONICET. Puerto Madryn, Chubut, Argentina, (U9120).



1. Introducción

En la era del big data, la capacidad para transformar grandes volúmenes de datos en información comprensible y accionable es crucial. Las visualizaciones de datos juegan un papel esencial en este proceso, ya que permiten identificar patrones, tendencias y anomalías de manera intuitiva. Sin embargo, la creación de visualizaciones efectivas puede ser un desafío, especialmente para usuarios que no cuentan con experiencia en análisis de datos o diseño gráfico. Con la aparición de los Modelos de Lenguaje de Gran Escala (LLMs, por sus siglas en inglés), como los desarrollados por OpenAI, se abre una nueva posibilidad para la automatización de este proceso. Este proyecto propone la construcción de una interfaz interactiva utilizando el framework Streamlit, que se apoya en LLMs y técnicas de machine learning para analizar la estructura de los datos proporcionados por los usuarios y generar visualizaciones recomendadas. Esta herramienta tiene el potencial de democratizar el acceso a análisis de datos avanzados, facilitando la interpretación de datos para una amplia gama de usuarios.

 2. Objetivos

Objetivo General:

Desarrollar una interfaz interactiva basada en Streamlit, utilizando LLMs y técnicas de machine learning, para analizar y generar automáticamente visualizaciones de datos recomendadas, adaptadas a los datos proporcionados por los usuarios.

Objetivos Específicos:

1. Integrar un modelo LLM que pueda interpretar descripciones de datos y contextualizar la estructura de los mismos.
2. Desarrollar algoritmos de machine learning que permitan seleccionar el tipo de visualización más adecuada para los datos en cuestión.
3. Implementar una interfaz en Streamlit que facilite la interacción del usuario con el sistema, permitiendo la carga de datos y la visualización de las recomendaciones generadas.
4. Evaluar la efectividad de las visualizaciones generadas automáticamente en comparación con las creadas manualmente por expertos.
5. Validar la herramienta a través de pruebas con usuarios de distintos niveles de experiencia en análisis de datos.

 3. Desarrollo

El desarrollo del proyecto se llevará a cabo en varias etapas clave:

3.1. Selección y Configuración del LLM:
   - Se seleccionará un LLM adecuado de OpenAI, con la capacidad de comprender y procesar instrucciones en lenguaje natural relacionadas con la estructura y el análisis de datos.
   - Se configurará el modelo para que interactúe eficientemente con los datos ingresados por los usuarios y pueda sugerir visualizaciones basadas en patrones reconocibles en los datos.

3.2. Diseño de Algoritmos de Recomendación:
   - Se desarrollarán algoritmos de machine learning que analicen la estructura de los datos (tipos de variables, relaciones entre ellas, etc.) para recomendar la visualización más adecuada.
   - Estos algoritmos serán entrenados utilizando conjuntos de datos estándar para asegurar la precisión de las recomendaciones.

3.3. Construcción de la Interfaz en Streamlit:
   - Se diseñará una interfaz interactiva en Streamlit, donde los usuarios podrán cargar sus datos, recibir recomendaciones y generar visualizaciones de manera automatizada.
   - La interfaz será intuitiva y accesible, pensada para usuarios con diversos niveles de experiencia técnica.

3.4. Integración y Pruebas:
   - Se integrarán todos los componentes del sistema, asegurando que la comunicación entre el LLM, los algoritmos de machine learning y la interfaz sea fluida.
   - Se realizarán pruebas con usuarios para identificar posibles mejoras en la usabilidad y precisión del sistema.

 4. Metodología

La metodología del proyecto se basará en un enfoque ágil, iterativo, que permite ajustes rápidos en respuesta al feedback de los usuarios y a los resultados obtenidos durante las pruebas. 

PIPELINE:

- Investigación Inicial: Revisión de la literatura sobre LLMs, machine learning y técnicas de visualización de datos.
- Desarrollo Tecnológico: Programación e integración de los componentes utilizando Python, Streamlit, y APIs de OpenAI.
- Entrenamiento de Algoritmos: Uso de datasets de prueba para entrenar y ajustar los modelos de recomendación.
- Validación y Evaluación: Aplicación de métricas de usabilidad y precisión para evaluar la herramienta desarrollada.
- Documentación y Presentación: Preparación de documentación técnica y académica para presentar los hallazgos y el funcionamiento del sistema en el congreso.

 5. Resultados Esperados

Al finalizar el proyecto, se espera haber desarrollado una herramienta que:

- Proporcione visualizaciones precisas y útiles basadas en un análisis automatizado de los datos.
- Facilite la comprensión y presentación de datos para usuarios con distintos niveles de experiencia técnica.
- Democratice el acceso a herramientas de análisis avanzado, permitiendo a más personas tomar decisiones informadas basadas en sus datos.
- Genere un impacto positivo en la comunidad académica y profesional al presentar un enfoque innovador para la automatización del análisis de datos.


 6. Conclusión

Este proyecto propone una solución innovadora para uno de los desafíos contemporáneos en la gestión y visualización de datos. Al combinar la capacidad de los LLMs con técnicas avanzadas de machine learning y una interfaz accesible, se puede ofrecer una herramienta poderosa para mejorar la comprensión de datos complejos. La automatización de la generación de visualizaciones no solo ahorra tiempo, sino que también aumenta la precisión y relevancia de las presentaciones visuales, beneficiando a una amplia gama de usuarios. La implementación de este sistema tiene el potencial de marcar un avance significativo en la accesibilidad y efectividad del análisis de datos.

 7. Referencias

 - Brown, T., Mann, B., Ryder, N., et al. (2020). Language Models are Few-Shot Learners. *Advances in Neural Information Processing Systems, 33*, 1877-1901.
- McKinney, W. (2010). Data Structures for Statistical Computing in Python. *Proceedings of the 9th Python in Science Conference*, 51-56.
- OpenAI. (2024). *OpenAI API documentation*. Recuperado de https://platform.openai.com/docs
- Plotly. (2024). *Plotly Python Graphing Library*. Recuperado de https://plotly.com/python/
- Reitz, K., & Team. (2024). *Requests: HTTP for Humans*. Recuperado de https://requests.readthedocs.io/
- Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why Should I Trust You?": Explaining the Predictions of Any Classifier. *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 1135-1144.
- Seaborn: Statistical Data Visualization — Seaborn 0.11.1 Documentation. (2020). Recuperado de https://seaborn.pydata.org/
- Streamlit. (2024). *The fastest way to build and share data apps*. Recuperado de https://streamlit.io/
- The Pandas Development Team. (2024). *Pandas documentation*. Recuperado de https://pandas.pydata.org/

