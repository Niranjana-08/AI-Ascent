# <img src=https://user-images.githubusercontent.com/55955478/235878802-1c423764-f355-47b0-b926-f9380334defd.png height=40 width=40> AI-Ascent: LinkedIn Job Analysis


This repository contains an end-to-end project analyzing the impact of Artificial Intelligence on the job market, based on data from LinkedIn job postings. The core of the project involves classifying jobs into different categories based on their relevance to AI, performing in-depth analysis using SQL, and visualizing the findings. The culmination of this analysis is an interactive web dashboard built with Streamlit, which showcases key insights about AI-related roles, salary distributions, required skills, and geographical trends.

<br>

## <img src=https://user-images.githubusercontent.com/106439762/181935629-b3c47bd3-77fb-4431-a11c-ff8ba0942b63.gif height=50 width=50 > Project Structure

| File/Folder | Description |
|---|---|
| `data_cleaning_01.ipynb` | Merges 11 raw CSV files into a single master DataFrame for initial processing. |
| `data_cleaning_02.ipynb` | Performs crucial cleaning and preprocessing, creating a combined text column for classification. |
| `data_cleaning_03.ipynb` | Classifies jobs into main and sub-categories using Sentence Transformer embeddings for semantic similarity. |
| `analysing_csvs.ipynb` | Engineers an 'AI Relevance' score and classifies jobs into 'Traditional', 'AI-Impacted', or 'Core AI' roles. |
| `sql_analysis_and_hypothesis_testing.ipynb` | Conducts in-depth analysis and hypothesis testing on the classified data using SQL queries. |
| `visualization_notebook.ipynb` | Creates a series of insightful charts and graphs from the analyzed data for the dashboard. |
| `app_streamlit.py` | The Streamlit application that builds and serves the interactive analysis dashboard. |
| `keywords.py` | Contains a hierarchical dictionary of keywords used for the job classification models. |
| `requirements.txt` | A list of the Python libraries and dependencies required to run the project. |
| `README.md` | This README file, providing an overview of the project. |

<br>

## <img src=https://user-images.githubusercontent.com/106439762/181937125-2a4b22a3-f8a9-4226-bbd3-df972f9dbbc4.gif height=40 width=40> Tools & Technology Used:


<a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white"></a>
<a href="#"><img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-F37626.svg?logo=jupyter&logoColor=white"></a>
<a href="#"><img alt="Pandas" src="https://img.shields.io/badge/Pandas-150458.svg?logo=pandas&logoColor=white"></a>
<a href="#"><img alt="NumPy" src="https://img.shields.io/badge/Numpy-013243.svg?logo=numpy&logoColor=white"></a>
<a href="#"><img alt="Scikit-learn" src="https://img.shields.io/badge/scikit_learn-F7931E.svg?logo=scikitlearn&logoColor=white"></a>
<a href="#"><img alt="Sentence Transformers" src="https://img.shields.io/badge/Sentence_Transformers-8A2BE2.svg?logo=huggingface&logoColor=white"></a>
<a href="#"><img alt="SQL" src="https://img.shields.io/badge/SQL-4479A1.svg?logo=postgresql&logoColor=white"></a>
<a href="#"><img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?logo=streamlit&logoColor=white"></a>
<a href="#"><img alt="Plotly" src="https://img.shields.io/badge/Plotly-3F4F75.svg?logo=plotly&logoColor=white"></a>
<a href="#"><img alt="Seaborn" src="https://img.shields.io/badge/Seaborn-3776AB.svg?logo=seaborn&logoColor=white"></a>
<a href="#"><img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-006DB2.svg?logo=matplotlib&logoColor=white"></a>



<br>

## <img src=https://user-images.githubusercontent.com/106439762/178428775-03d67679-9aa4-4b08-91e9-6eb6ed8faf66.gif height=40 width=40> Project Pipeline:
#### 1️⃣  Data Integration & Cleaning
<details>
<summary> Consolidate and prepare the raw job data</summary>

- Merged 11 raw CSV files into a single master DataFrame.
- Handled missing values and standardized data types across columns.
- Created a unified `combined_text` column (from title, description, skills) for NLP processing.

</details>

#### 2️⃣  Job Classification & Feature Engineering
<details>
<summary> Classify jobs and engineer the AI relevance feature</summary>

- Utilized a **Sentence Transformer** model to encode job descriptions and a keyword hierarchy into vector embeddings.
- Calculated cosine similarity to classify each job into a `main_category` and `sub_category`.
- Engineered an `ai_relevance_score` by comparing job text to a vector representing the concept of "Artificial Intelligence".
- Categorized jobs into `ai_relevance_tier` (Core AI, AI-Impacted, Traditional) based on score thresholds.

</details>

#### 3️⃣  SQL Analysis & Hypothesis Testing
<details>
<summary> Perform deep-dive analysis using SQL</summary>

- Loaded the classified dataset into a SQL database for efficient querying.
- Wrote complex queries to aggregate data and extract summary statistics (e.g., median salaries by tier, top skills per category).
- Performed statistical analysis to validate initial hypotheses about salary and skill distributions.

</details>

#### 4️⃣  Visualization & Dashboard Creation
<details>
<summary> Build the interactive dashboard</summary>

- Developed a range of visualizations (treemaps, bar charts, maps, word clouds) using Plotly and Seaborn.
- Assembled the visualizations into a cohesive and interactive web application using **Streamlit**.
- Deployed the dashboard to the cloud for public access.

</details>

<!---

1.  **Data Integration and Cleaning:** Loaded and merged 11 separate raw CSV files containing job data. Performed extensive data cleaning, handling missing values, and standardizing text fields to prepare a unified dataset.

2.  **Job Classification with Sentence Transformers:** Utilized a sophisticated Sentence Transformer model to classify each job. This involved:
    * Encoding job descriptions and a predefined hierarchy of keywords into vector embeddings.
    * Calculating the cosine similarity between job descriptions and keyword embeddings.
    * Assigning each job to a main and sub-category based on the highest similarity score, achieving a robust, context-aware classification.

3.  **AI Relevance Scoring:** Engineered a feature to quantify how closely each job relates to Artificial Intelligence. Based on this relevance score, jobs were categorized into three distinct tiers:
    * **Core AI Role:** Jobs centered directly on AI development and research.
    * **AI-Impacted Role:** Traditional roles that now require AI skills or interact with AI systems.
    * **Traditional Role:** Roles with little to no direct relation to AI.

4.  **In-depth SQL Analysis:** Imported the cleaned and classified data into a SQL database to perform complex queries. Leveraged SQL to analyze salary distributions, geographic trends, experience requirements, and skill demands across different job categories and AI relevance tiers.

5.  **Visualization and Dashboard Development:** Created a wide range of visualizations using libraries like Matplotlib, Seaborn, and Plotly to uncover patterns and insights. These visualizations were then integrated into an interactive dashboard using **Streamlit** to present the findings in an accessible and engaging way.

    <img src=https://github.com/Niranjana-08/AI-Ascent/raw/main/assets/dashboard_screenshot.png height=400 width=700 >

---->
<br>

## <img src=https://user-images.githubusercontent.com/106439762/178803205-47a08ce7-2187-4f96-b301-a2b68690619a.gif height=40 width=40> Key Insights from the Dashboard:

1.  **Hierarchical View of the Job Market:** An interactive treemap that visualizes the job market, segmented by main categories, sub-categories, and AI relevance, providing a clear overview of where AI is having the most impact.

2.  **Salary Insights by AI Relevance:** Analysis of how median salaries differ between Core AI, AI-Impacted, and Traditional roles. The data shows a clear salary premium for roles with higher AI relevance, even after accounting for experience levels.

4.  **Geographic Distribution of AI Jobs:** A map of the United States highlighting hotspots for AI-related job opportunities. The visualization reveals key tech hubs and emerging regions for AI talent.

5.  **Most In-Demand Skills for AI Roles:** Word clouds and bar charts showcasing the most frequently mentioned skills in job descriptions for Core AI and AI-Impacted positions, offering valuable insights for job seekers.


<br>

## <img src=https://cdn1.vectorstock.com/i/1000x1000/45/70/dashboard-icon-vector-22894570.jpg height=50 width=50> Interactive Dashboard

An interactive Streamlit dashboard has been developed to bring the analysis to life. It consolidates data from multiple sources and showcases visually engaging and interactive charts, maps, and graphs. This allows users to explore key metrics, filter data, and extract valuable insights on their own. The dashboard enhances data-driven decision-making and provides a clear, compelling narrative about the rise of AI in the job market.

Dashboard Preview :
![Dashboard Preview](https://raw.githubusercontent.com/Niranjana-08/AI-Ascent/main/streamlit_app/graphs_new/preview_dashboard.png)
<br>
## <img src=https://user-images.githubusercontent.com/108053296/185756908-fbb62168-d923-48f2-992f-b8e2fde848fe.gif height=50 width=50> Conclusions:

<!---

1.  **AI is Reshaping the Job Market:** The analysis clearly shows a significant and growing number of "AI-Impacted" roles, indicating that AI is not just creating new jobs but fundamentally changing existing ones.
2.  **Significant Salary Premium for AI Skills:** There is a demonstrable financial benefit to having AI skills, with Core AI and AI-Impacted roles commanding higher salaries than traditional roles at similar experience levels.
3.  **Data-Related Roles Dominate AI:** Roles such as Data Scientist, Machine Learning Engineer, and Data Analyst are at the forefront of the AI job landscape.
4.  **Tech Hubs Lead in AI Opportunities:** Major technology centers remain the primary locations for AI-related jobs, though opportunities are beginning to spread geographically.
5.  **Continuous Learning is Crucial:** The most in-demand skills highlight the need for continuous learning and adaptation, as proficiency in areas like Python, SQL, and specific machine learning frameworks is essential.
   --->

- **AI's Influence is Widespread**: A significant portion of modern roles are now "AI-Impacted," demonstrating that AI skills are becoming essential across various industries, not just in core tech positions.
- **Clear Salary Advantage**: There is a distinct salary premium for both **Core AI** and **AI-Impacted** roles when compared to Traditional roles, even at the same experience level.
- **Geographic Concentration**: AI job opportunities are heavily concentrated in traditional tech hubs like California and Washington, but emerging hotspots are appearing in states like Texas and Virginia.
- **Top In-Demand Skills**: Beyond foundational skills like **Python** and **SQL**, expertise in **Machine Learning**, **Cloud Computing (AWS/Azure)**, and **Data Visualization (Tableau/PowerBI)** are critical for high-relevance AI roles.
- **Data Roles are Central**: Job titles like **Data Scientist**, **Machine Learning Engineer**, and **Data Analyst** consistently appear as the most common roles within the Core AI and AI-Impacted tiers.

<br>

## Check out the live interactive dashboard here: 
[AI-Ascent Analysis Dashboard](http://ai-ascentgit-c2gtfbzhdrbgk7cztxguuk.streamlit.app/)

<!---# AI-Ascent
A Data-Driven Analysis of the Rise of AI Careers on LinkedIn.

## Live Interactive Dashboard

This project culminates in a fully interactive dashboard built with Streamlit. It allows users to explore the key findings of the analysis, including geographic trends, skill demand, and salary comparisons.

**[Click here to access the live dashboard](https://ai-ascentgit-c2gtfbzhdrbgk7cztxguuk.streamlit.app/)**
--->
