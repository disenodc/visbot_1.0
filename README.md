![Logo visbot](https://raw.githubusercontent.com/disenodc/VisBot/refs/heads/main/bot_1.png)
# VisBot - Visualization Recommender with iA - Automated Interactive Visualization Recommendations Using Large Language Models: Enhancing Data Insights and Accessibility


- Visitar: [Sitio Web](https://visbot.streamlit.app/) / [LICENCIA](https://github.com/disenodc/VisBot/blob/main/LICENSE)
- Authors: BCCs. Luis Dario Ceballos. Dr. Marcos Zarate, BCCs Gustavo Nuñez and Dr. Claudio Delrieux


## PIPELINE locally executed

- Clone the repository

```bash
git clone https://github.com/disenodc/visbot.git
```
- Navigate to directory

```bash
cd ruta/al/directorio/del/repositorio/
```

- then install required libraries

```bash
 pip install -r requirements.txt
```
- Finally run the application

```bash
 streamlit run visbot.py
```

/////////////////////////////////
## PROJECT


1. Summary

In today's data-driven world, the ability to visualize complex datasets is crucial for effective data analysis and decision-making. However, creating accurate and meaningful visualizations remains a challenge, particularly for non-experts. This paper presents VisBot, an automated system that leverages large language models to generate and recommend interactive visualizations. By integrating language models with effective data visualization principles and an interactive user interface, VisBot facilitates the automated generation of dataset visual analyses. Here, we show that VisBot can generate contextually relevant visualizations, as evidenced by user feedback and comparative analysis with existing systems. The results underscore the potential of language models for automating data exploration tasks, thereby enhancing data comprehension and communication for users across multiple domains.

 2. Objectives

General Objective:

Develop an interactive interface based on Streamlit, using LLMs and machine learning techniques, to automatically analyze and generate recommended data visualizations, adapted to the data provided by users.

Specific Objectives:

   1. Integrate an LLM model that can interpret data descriptions and contextualize their structure.
   2. Develop machine learning algorithms that allow selecting the most appropriate type of visualization for the data in question.
   3. Implement an interface in Streamlit that facilitates user interaction with the system, allowing the loading of data and the visualization of the generated recommendations.
   4. Evaluate the effectiveness of automatically generated visualizations compared to those created manually by experts.
   5. Validate the tool through tests with users of different levels of experience in data analysis.


3. Development

The development of the project will take place in several key stages:

3.1. Selection and Configuration of the LLM:
   - A suitable OpenAI LLM will be selected, with the ability to understand and process natural language instructions related to data structure and analysis.
   - The model will be configured so that it interacts efficiently with the data entered by users and can suggest visualizations based on recognizable patterns in the data.

3.2. Design of Recommendation Algorithms:
   - Machine learning algorithms will be developed that analyze the structure of the data (types of variables, relationships between them, etc.) to recommend the most appropriate visualization.
   - These algorithms will be trained using standard data sets to ensure the accuracy of the recommendations.

3.3. Construction of the Interface in Streamlit:
   - An interactive interface will be designed in Streamlit, where users will be able to upload their data, receive recommendations and generate visualizations in an automated manner.
   - The interface will be intuitive and accessible, designed for users with various levels of technical experience.

3.4. Integration and Testing:
   - All system components will be integrated, ensuring that communication between the LLM, the machine learning algorithms and the interface is fluid.
   - Tests will be carried out with users to identify possible improvements in the usability and accuracy of the system.

 4. Methodology

The project methodology will be based on an agile, iterative approach, which allows rapid adjustments in response to user feedback and results obtained during testing. Stages of the methodology:

- Initial Research: Review of the literature on LLMs, machine learning and data visualization techniques.
- Technological Development: Programming and integration of components using Python, Streamlit, and OpenAI APIs.
- Algorithm Training: Use of test datasets to train and adjust recommendation models.
- Validation and Evaluation: Application of usability and precision metrics to evaluate the developed tool.
- Documentation and Presentation: Preparation of technical and academic documentation to present the findings and operation of the system at the congress.

 5. Expected Results

At the end of the project, it is expected to have developed a tool that:

- Provide accurate and useful visualizations based on automated data analysis.
- Facilitate the understanding and presentation of data for users with different levels of technical experience.
- Democratize access to advanced analytics tools, allowing more people to make informed decisions based on their data.
- Create a positive impact on the academic and professional community by presenting an innovative approach to data analysis automation.


 6. Conclusion

The project represents a significant advancement in the field of data analysis automation and the generation of interactive visualizations by leveraging the capabilities of LLMs. The integration of these technologies with an accessible interface based on Streamlit aims to provide a robust, intuitive, and effective tool, allowing users with varying levels of experience to generate accurate and relevant visualizations, thus facilitating data analysis and presentation. By employing an LLM to interpret data structures and to select the most appropriate visualization type from the data characteristics, the platform reduces the cognitive load on users. This automation minimizes common errors associated with manual graph creation, thereby enhancing the efficiency and accuracy of visual analysis. The platform provides an inclusive and accessible solution that democratizes access to advanced data analysis tools. Non-technical users, who previously had to rely on experts or complex tools, now can interact with their data and autonomously generate high-quality visualizations. This aligns with current trends in simplifying technical processes through artificial intelligence, as seen in platforms such as Microsoft’s LIDA.

The most notable aspects are the correct implementation of georeferenced data and the customization of the recommended visualizations on the basis of the selection of the variables of interest. This represents an important advancement, as the quality of visualizations directly impacts users’ ability to identify patterns and make informed decisions. The impact of this solution is substantial for both the academic community and professionals, who require advanced data analysis capabilities in their daily work. The scalability of such solutions in real-world applications and potential improvements in accessibility, interpretability, and user engagement highlight the tangible impacts that LLM-driven visualizations could have. The usability study demonstrated that VisBot is a promising tool for the automated generation of interactive visualizations. While users appreciated the ease of use and relevance of the recommendations, they also identified areas for improvement in customization and clarity of instructions. These findings support the viability of the platform as an accessible solution for nontechnical users while highlighting directions for future refinement.


7. Author’s biographical summary

Dario Ceballos holds a degree in Arts and Technologies and is currently a Doctoral Researcher in Strategic Topics. His work falls within the fields of Computer Science and Communications and Earth, Water, and Atmospheric Sciences, with a specialization in Data Science. His research focuses on the development of Visual Analytics for Linked Data in Ocean Sciences, with applications in water resources, oceanic basins, and socioeconomic development and services. His interdisciplinary approach integrates artificial intelligence, robotics, and data visualization techniques to enhance the analysis and understanding of scientific data in the marine environment He is currently conducting his research at the Center for the Study of Marine Systems (CESIMAR - CENPAT), within the Scientific and Technological Center CONICET - National Patagonian Center (CCT CENPAT), under the supervision of Dr. Claudio Augusto Delrieux and co-supervision of Dr. Mirtha Noemí Lewis. His main research interests include Visual Analytics, Linked Data, and Ocean Sciences, contributing to the development of innovative tools for the exploration and analysis of large-scale oceanographic datasets. ORCID: 0009-0002-9207-7023


Marcos Zárate holds a Ph.D. in Computer Science and is currently an Assistant Researcher. His work spans the disciplines of Computer Science and Communications and Earth, Water, and Atmospheric Sciences, with a specialization in Semantic Web, Linked Open Data, and Knowledge Graphs. His research focuses on Knowledge Extraction and Exploitation for Online Data Management in Marine Sciences, contributing to the management and analysis of oceanographic data, knowledge graphs, and semantic web technologies. His work has applications in water resources, oceanic basins, and meteorology, aiming to enhance data-driven decision-making in marine and atmospheric sciences. He conducts his research at the Center for the Study of Marine Systems (CESIMAR - CENPAT), within the Scientific and Technological Center CONICET - National Patagonian Center (CCT CENPAT), under the supervision of Dr. Claudio Augusto Delrieux and co-supervision of Dr. Mirtha Noemí Lewis. His research interests include Knowledge Graphs, Oceanographic Campaigns, and the Semantic Web, focusing on the integration and exploitation of linked data to improve the accessibility and usability of marine science information. ORCID: 0000000188518602.


Claudio Delrieux, holds a Ph.D. in Computer Science and a degree in Electronic Engineering. He is currently a Principal Researcher, specializing in Computing, within the disciplines of Technological and Social Development in Complex Projects and Computer Science and Communications. His research focuses on the analysis and processing of optical, SAR satellite, and airborne imagery for environmental monitoring, leveraging remote sensing, artificial intelligence, and radar imaging techniques to enhance environmental assessment and decision-making processes. His work contributes to the sustainable management of renewable natural resources and territorial planning through advanced computational methods. He conducts his research at the Institute of Computer Science and Engineering (ICIC), within the Scientific and Technological Center CONICET - Bahía Blanca (CCT Bahía Blanca), affiliated with the National Scientific and Technical Research Council (CONICET). His main research interests include RADAR imagery, remote sensing and environmental monitoring, and artificial intelligence, with a focus on developing cutting-edge computational techniques for analyzing complex geospatial data. ORCID: 0000-0002-2727-8374.

Gustavo Nuñez holds a Bachelor’s degree in Computer Science and is currently a Doctoral Fellow. His research is within the field of Computer Science and Communications, with a specialization in Artificial Intelligence. His work focuses on Artificial Intelligence as a Tool for the Exploitation of Oceanographic Data, leveraging knowledge graphs and AI techniques to enhance the analysis and management of marine science data. His research aims to develop innovative methods for extracting, integrating, and interpreting oceanographic information to support scientific discovery and decision-making. He conducts his research at the Center for the Study of Marine Systems (CESIMAR - CENPAT), within the Scientific and Technological Center CONICET - National Patagonian Center (CCT CENPAT), under the supervision of Dr. Claudio Augusto Delrieux and co-supervision of Dr. Mirtha Noemí Lewis. His main research interests include Artificial Intelligence, Knowledge Graphs, and Marine Science, focusing on the development of AI-driven solutions to enhance data exploration and knowledge extraction in oceanographic studies. ORCID: 0009-0007-0215-2699.


 8. References

[1] Tufte, E.: The Visual Display of Quantitative Information. Graphics Press, Cheshire, CT (1983)
[2] Wong, P., Thomas, J., Wiley, S.: Visual analytics. IEEE Computer Graphics and Applications 20(5), 20–21 (2000). https://doi.org/10.1109/MCG.2004.39 
[3] Keim, D., Andrienko, G., Fekete, J., Görg, C., Kohlhammer, J., Melançon, G.: Visual analytics: Definition, process, and challenges. In: Information Visualization: Human-Centered Issues and Perspectives, vol. 4950 of Lecture Notes in Computer Science, pp. 154–175. Springer, Heidelberg (2008). https://doi.org/10.1007/978-3-540-70956-5_7   
[4] Tukey, J.: Exploratory Data Analysis. Addison-Wesley, Reading, MA (1977)
[5] Smith-Miles, K.: Exploratory Data Analysis. In: Springer Berlin Heidelberg (ed.), pp. 486–488. Springer, Berlin, Heidelberg (2011)
[6] Cleveland, W.: Visualizing Data. Hobart Press, Summit, NJ (1993)  
[7] Midway, S.: Principles of effective data visualization. Patterns 1 (2020)  
[8] Turing, A.: Computing machinery and intelligence. Mind 59(236), 433–460 (1950)  
[9] Good, I.: Speculations concerning the first ultraintelligent machine. In: Alt, F., Rubinoff, M. (eds.) Advances in Computers, vol. 6, pp. 31–88. Academic Press, New York (1965)  
[10] Mackinlay, J.: Automating the design of graphical presentations of relational information. ACM Transactions on Graphics (TOG) 5(2), 110–141 (1986)
[11] Wu, Y., Wan, Y., Zhang, H., Sui, Y., Wei, W., Zhao, W., Xu, G., Jin, H.: Automated data visualization from natural language via large language models: An exploratory study. Proc. ACM Manag. Data 2(3), May 2024 
[12] OpenAI: GPT-4 is OpenAI’s most advanced system, producing safer and more useful responses. https://openai.com/index/gpt-4/  (Accessed 2024)
[13] Wang, L., Zhang, S., Wang, Y., Lim, E., Wang, Y.: Llm4vis: Explainable visualization recommendation using chatgpt. In: Conference on Empirical Methods in Natural Language Processing (2023) 
[14] Cheonsu, J.: A study on the implementation of generative AI services using an enterprise data-based LLM application architecture. arXiv preprint arXiv:2309.01105 (2023) 
[15] Lin, C., Huang, A., Yang, S.: A review of AI-driven conversational chatbots implementation methodologies and challenges (1999–2022). Sustainability 15(5), 4012 (2023)
[16] Alazzam, B., Alkhatib, M., Shaalan, K.: Artificial intelligence chatbots: A survey of classical versus deep machine learning techniques. Inf. Sci. Lett 12(4), 1217–1233 (2023)  
[17] Russell, S., Norvig, P.: Artificial Intelligence: A Modern Approach. Pearson, Upper Saddle River, NJ, 4th edition (2021)  
[18] Gentsch, P.: AI in Marketing, Sales and Service: How Marketers without a Data Science Degree can use AI, Big Data and Bots. Springer, Cham (2018)  
[19] Wang, P.: On defining artificial intelligence. Journal of Artificial General Intelligence 10(2), 1–37 (2019)
[20] Joulin, A., Grave, E., Bojanowski, P., Mikolov, T.: Bag of tricks for efficient text classification. In: Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics (2017). https://doi.org/10.18653/v1/E17-2068 
[21] Kim, J.K., Chua, M., Rickard, M., Lorenzo, A.: ChatGPT and large language model (LLM) chatbots: The current state of acceptability and a proposal for guidelines on utilization in academic medicine. Journal of Pediatric Urology 19(5), 598–604 (2023)  
[22] Heer, J., Bostock, M.: Declarative language design for interactive visualization. IEEE Transactions on Visualization and Computer Graphics 16(6), 1149–1156 (2010)
[23] Nielsen, J.: Usability Engineering. Morgan Kaufmann (1994)  
[24] Nielsen, J., Molich, R.: Heuristic evaluation of user interfaces. In: Proceedings of the SIGCHI conference on Human factors in computing systems, pp. 249–256 (1990)  
[25] Goertzel, B., Pennachin, C. (eds.): Artificial General Intelligence. Springer, Berlin, Heidelberg (2007)
[26] Marcus, G.: The next decade in AI: Four steps toward robust artificial intelligence. arXiv preprint arXiv:2002.06177 (2020)  
[27] Schmidhuber, J.: Deep learning in neural networks: An overview. Neural Networks 61, 85–117 (2015)
[28] Mittal, M., Raheja, N.: Data Visualization and Storytelling with Tableau. CRC Press (2024)
[29] Gonçalves, C.T., Gonçalves, M.J.A., Campante, M.I.: Developing integrated performance dashboards visualisations using Power BI as a platform. Information 14(11), 614 (2023)  
[30] Gulliksen, J., Göransson, B., Boivie, I., Blomkvist, S., Persson, J., Cajander, Å.: Key principles for user-centred systems design. Behavior & Information Technology 22(6), 397–409 (2003)  
[31] McKinney, W.: Data structures for statistical computing in Python. In: SciPy, vol. 445, pp. 51–56 (2010) 
[32] Card, S., Mackinlay, J., Shneiderman, B.: Readings in Information Visualization: Using Vision to Think. Morgan Kaufmann, San Francisco, CA (1999)  
[33] Ware, C.: Information Visualization: Perception for Design. Morgan Kaufmann, San Francisco, CA, 2nd edition (2004)
[34] Sunitha, G., Sriharsha, A.V., Yalgashev, O., Mamatov, I.: Interactive visualization with Plotly Express. In: Advanced Applications of Python Data Structures and Algorithms, pp. 182–206. IGI Global (2023)  
[35] Prasad, G., Gujjar, P., Kotiyal, A., HR, P., Devadas, R., Jahan, A.: Exploratory data analysis using AutoViz for machine learning classification problem. In: 2024 International Conference on Emerging Innovations and Advanced Computing (INNOCOMP), pp. 496–500. IEEE (2024)  
[36] Lima, R.d.A., Barbosa, S.D.J.: VisMaker: A question-oriented visualization recommender system for data exploration. arXiv e-prints, arXiv–2002 (2020) 
[37] Li, H., Wang, Y., Zhang, S., Song, Y., Qu, H.: Kg4Vis: A knowledge graph-based approach for visualization recommendation. IEEE Transactions on Visualization and Computer Graphics 28(1), 195–205 (2021)
[38] Dibia, V.: LIDA: A tool for automatic generation of grammar-agnostic visualizations and infographics using large language models. arXiv preprint arXiv:2303.02927 (2023) 
[39] Tian, Y., Cui, W., Deng, D., Yi, X., Yang, Y., Zhang, H., Wu, Y.: ChartGPT: Leveraging LLMs to generate charts from abstract natural language. IEEE Transactions on Visualization and Computer Graphics (2024) 
[40] Maddigan, P., Susnjak, T.: Chat2Vis: Fine-tuning data visualisations using multilingual natural language text and pre-trained large language models. ArXiv abs/2303.14292 (2023)  
[41] Podo, L., Angelini, M., Velardi, P.: V-Recs, a low-cost LLM4Vis recommender with explanations, captioning and suggestions. ArXiv abs/2406.15259 (2024) 
[42] Streamlit: Streamlit: A faster way to build and share data apps. https://streamlit.io/ (Accessed 2024)
[43] Shneiderman, B.: Designing the user interface: Strategies for effective human-computer interaction. ACM SIGBIO Newsletter 9(1), 6 (1987)
[44] OpenAI: OpenAI Developer Platform. https://platform.openai.com/docs/overview (Accessed 2024)
[45] Pace, R., Barry, R.: Sparse spatial autoregressions. Statistics & Probability Letters 33(3), 291–297 (1997)
[46] Available in SciKitLearn datasets, https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html (accessed March 26, 2025). Also available in Kaggle,  https://www.kaggle.com/datasets/camnugent/california-housing-prices (accessed March 26, 2025). Published under CCO: Public Domain License.
[47] Xie, J., Zhu, F., Huang, M., Xiong, N., Huang, S., Xiong, W.: Unsupervised learning of paragraph embeddings for context-aware recommendation. IEEE Access 7, 43100–43109 (2019)  
[48] Brown, T.: Language models are few-shot learners. arXiv preprint arXiv:2005.14165 (2020). https://doi.org/10.48550/arXiv.2005.14165 
[49] Yan, H., Liu, Y., Jin, L., Bai, X.: The development, application, and future of LLM similar to ChatGPT. Journal of Image and Graphics 28(9), 2749–2762 (2023)  
[50] Ribeiro, M., Singh, S., Guestrin, C.: “Why should I trust you?” Explaining the predictions of any classifier. In: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 1135–1144 (2016)
[51] Knijnenburg, B., Willemsen, M., Gantner, Z., Soncu, H., Newell, C.: Explaining the user experience of recommender systems. User Modeling and User-Adapted Interaction 22(4–5), 441–504 (2012)
[52] Peña, O., Aguilera, U., López-de Ipiña, D.: Linked open data visualization revisited: A survey. Semantic Web Journal (2014)
[53] Global Biodiversity Information Facility: Home page. https://www.gbif.org/ (Accessed 2025)
[54] Yang, W., Liu, M., Wang, Z., & [et al.]. (2024). Foundation models meet visualizations: Challenges and opportunities. Computational Visual Media, 10, 399–424. https://doi.org/10.1007/s41095-023-0393-x
