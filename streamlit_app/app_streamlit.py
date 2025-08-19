# copied from app.py --> trying to make it look more better

## Making few changes 
import streamlit as st
import streamlit.components.v1 as components
import os

# --- PAGE CONFIG ---
# This must be the first Streamlit command in your script
st.set_page_config(
    page_title="LinkedIn Job Analysis Dashboard",
    page_icon="📊",
    layout="wide" # Use the full page width
)

# --- HEADER ---
st.title("📊 LinkedIn Job Analysis: The Impact of AI")
st.write("""
This dashboard provides an analysis of LinkedIn job postings to uncover insights into the evolving job market, with a focus on the rise of AI-related roles.
""")

# --- DEFINE FILE PATHS ---
# Define the path to your graphs folder
GRAPH_DIR = "graphs_new"

# ==============================================================================
# --- SECTION 1: INTERACTIVE OVERVIEW ---
st.header("Interactive Job Market Overview")
st.write("These charts provide a high-level, interactive view of the job market. Click on segments to zoom in and hover for more details.")

# --- CHART 1.1: HIERARCHICAL TREEMAP ---
st.subheader("Hierarchical View by AI Relevance")
html_path = os.path.join(GRAPH_DIR, "nested_treemap_ai_colored_no_other.html")
try:
    with open(html_path, 'r', encoding='utf-8') as f:
        html_data = f.read()
    components.html(html_data, height=500, scrolling=True)
except FileNotFoundError:
    st.error(f"Error: The file '{os.path.basename(html_path)}' was not found in the 'graphs' folder.")
    
# Add your note below the image/caption
st.markdown(
    "<span style='text-align: center; display: block; color: gray; font-size: 0.95em; margin-top:-15px;'>"
    "**Note:** The graph above considers the 87,106 jobs with a clearly defined main category.<br>"
    "The 'Other' category, containing 36,743 jobs, has been excluded for clarity."
    "</span>",
    unsafe_allow_html=True
)
    
st.divider()

# --- CHART 1.2: SUNBURST SALARY MAP ---
st.subheader("Interactive Salary Landscape")
html_path = os.path.join(GRAPH_DIR, "sunburst_max_salary_by_category.html")
try:
    with open(html_path, 'r', encoding='utf-8') as f:
        html_data = f.read()
    components.html(html_data, height=500)
except FileNotFoundError:
    st.error(f"Error: The file '{os.path.basename(html_path)}' was not found in the 'graphs' folder.")

st.markdown(
    "<span style='text-align: center; display: block; color: gray; font-size: 0.95em; margin-top:-15px;'>"
    "**Note:** This analysis is based on the 22,336 jobs (out of 123,849 total) that provided valid maximum salary information and a 'YEARLY' or 'HOURLY' pay period.<br>"
    "The 'Other' job category has been excluded for clarity."
    "</span>",
    unsafe_allow_html=True
)    
st.divider()
# ==============================================================================
# --- SECTION 2: AI ROLES AND SKILLS ANALYSIS ---
st.header("AI Roles, Skills, and Compensation")
col1, col2 = st.columns(2)

with col1:
    # --- CHART 2.1: SKILLS RELEVANCE HEATMAP ---
    with st.container():
        st.subheader("Skills Relevance Heatmap")
        # Corrected the filename extension to .png as requested
        image_path = os.path.join(GRAPH_DIR, "skills_relevance_heatmap.png")
        try:
            st.image(image_path, caption="Average AI relevance score for top skills by role type.", use_container_width=True)
        except Exception as e:
            st.error(f"Error loading image '{os.path.basename(image_path)}': {e}")
        
    # --- CHART 2.2: EXPERIENCE BY AI ROLE ---
    with st.container():
        st.subheader("Experience Level by AI Role")
        image_path = os.path.join(GRAPH_DIR, "experience_by_ai_role.png")
        try:
            st.image(image_path, caption="Distribution of experience levels across different AI role types.", use_container_width=True)
        except Exception as e:
            st.error(f"Error loading image '{os.path.basename(image_path)}': {e}")

with col2:
    # --- CHART 2.3: AI LIFT SKILLS ---
    with st.container():
        st.subheader("The Defining Skills of AI")
        image_path = os.path.join(GRAPH_DIR, "top_skills_by_ai_lift.png")
        try:
            st.image(image_path, caption="Top skills with the highest importance to AI roles compared to traditional roles.", use_container_width=True)
        except Exception as e:
            st.error(f"Error loading image '{os.path.basename(image_path)}': {e}")
            
        st.markdown(
        "<span style='text-align: center; display: block; color: gray; font-size: 0.95em; margin-top:-15px;'>"
        "**Note:** The analysis above considers only the 65176 jobs out of the 123849 total jobs that had a specified experience level."
        "</span>",
        unsafe_allow_html=True
    )    
    

    # --- CHART 2.4: SALARY BY AI ROLE ---
    with st.container():
        st.subheader("Salary by AI Role Type")
        image_path = os.path.join(GRAPH_DIR, "salary_by_ai_role.png")
        try:
            st.image(
                image_path,
                caption="Comparing average minimum salaries across role types and experience levels.",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Error loading image '{os.path.basename(image_path)}': {e}")
        st.markdown(
        "<span style='text-align: center; display: block; color: gray; font-size: 0.95em; margin-top:-15px;'>"
        "**Note:** The salary analysis above is based on the 23096 jobs out of the 123849 total jobs that provided salary information."
        "</span>",
        unsafe_allow_html=True
    )    

    # # Add your note below the image/caption
    # st.markdown("""
    # <span style='text-align: center; display: block; color: gray; font-size: 0.95em;'>
    # **Note:** The analysis above considers the 87,106 jobs with a clearly defined main category.  
    # The 'Other' category, containing 36,743 jobs, has been excluded for clarity.
    # </span>
    # """, unsafe_allow_html=True)    

st.divider()

# --- CHART 2.5: AI TITLES WORD CLOUD ---
st.subheader("Most Common Titles in AI-Related Roles")
image_path = os.path.join(GRAPH_DIR, "ai_roles_title_wordcloud_150.png")
try:
    st.image(image_path, caption="A word cloud of the top 150 most frequent job titles in AI-Impacted and Core AI roles.", use_container_width=True)
except Exception as e:
    st.error(f"Error loading image '{os.path.basename(image_path)}': {e}")
    
st.divider()
    


# ==============================================================================
# --- SECTION 3: GEOGRAPHIC & CATEGORY ANALYSIS ---
st.header("Geographic & Category Distribution")

# --- CHART 3.1: US MAP OF ALL JOBS ---
st.subheader("Job Openings Across the United States")
html_path = os.path.join(GRAPH_DIR, "us_job_openings_map.html")
try:
    with open(html_path, 'r', encoding='utf-8') as f:
        html_data = f.read()
    components.html(html_data, height=500)
except FileNotFoundError:
    st.error(f"Error: The file '{os.path.basename(html_path)}' was not found in the 'graphs' folder.")
st.divider()
    
   
# --- CHART 3.2: JOBS BY CATEGORY ---
st.subheader("Job Distribution by Main Category")
image_path = os.path.join(GRAPH_DIR, "jobs_by_category_enhanced.png")
try:
    st.image(image_path, caption="The overall distribution of jobs across different industries.", use_container_width=True)
except Exception as e:
    st.error(f"Error loading image '{os.path.basename(image_path)}': {e}")