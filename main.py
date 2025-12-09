import streamlit as st
import pandas as pd

# Page setup
Dashboard_page = st.Page(
    page="pages/Dashboard.py",
    title="Dashboard",
    icon="📈"
)

Download_data = st.Page(
    page="pages/Download data.py",
    title="Download Data",
    icon="📥"
)

Scrape_data = st.Page(
    page="pages/Scrape data.py",
    title="Scrape Data",
    icon="🔍"
)

Evaluation_form = st.Page(
    page="pages/Evaluationforms.py",
    title="Evaluation Forms",
    icon="📝"
)

# Custom Home Page Function
def home_page():
    st.set_page_config(
        page_title="Dakar-Auto Data App",
        layout="wide"
    )
    
    # Header with logo and title
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>Dakar-Auto Data App</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; font-size: 20px; color: #475569;'>Access to vehicle listings in Senegal made easy</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Welcome section
    st.markdown("""
    <div style='background-color: #F0F9FF; padding: 20px; border-radius: 10px; margin-bottom: 30px;'>
        <h3 style='color: #0369A1;'>Welcome to Dakar-Auto Data App!</h3>
        <p>This application helps you collect, analyze, and manage vehicle listing data from 
        <a href='https://dakar-auto.com' target='_blank' style='color: #0369A1; text-decoration: underline;'>Dakar-Auto</a>.
        Use the shortcuts below to navigate to different sections of the app.</p>
    </div>
    """, unsafe_allow_html=True)
        
    # Create shortcut cards in columns
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 25px; 
                    border-radius: 15px; 
                    text-align: center;
                    color: white;
                    height: 200px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;'>
            <h2>📈</h2>
            <h4>Dashboard</h4>
            <p>View analytics & insights</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Go to Dashboard", key="dashboard_btn", use_container_width=True):
            st.switch_page("pages/Dashboard.py")
    
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    padding: 25px; 
                    border-radius: 15px; 
                    text-align: center;
                    color: white;
                    height: 200px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;'>
            <h2>🔍</h2>
            <h4>Scrape Data</h4>
            <p>Collect fresh listings</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Go to Scrape", key="scrape_btn", use_container_width=True):
            st.switch_page("pages/Scrape data.py")
    
    with col3:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                    padding: 25px; 
                    border-radius: 15px; 
                    text-align: center;
                    color: white;
                    height: 200px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;'>
            <h2>📥</h2>
            <h4>Download Data</h4>
            <p>Get datasets in CSV</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Go to Download", key="download_btn", use_container_width=True):
            st.switch_page("pages/Download data.py")
    
    with col4:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); 
                    padding: 25px; 
                    border-radius: 15px; 
                    text-align: center;
                    color: white;
                    height: 200px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;'>
            <h2>📝</h2>
            <h4>Evaluation</h4>
            <p>Submit feedback forms</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Go to Forms", key="forms_btn", use_container_width=True):
            st.switch_page("pages/Evaluationforms.py")
    
    st.markdown("---")

# Create a Home Page entry
Home_page = st.Page(
    page=home_page,
    title="Home",
    default=True,
    icon="🏠"
)

# Navigation setup with Home as first page
pg = st.navigation(pages=[Home_page, Dashboard_page, Download_data, Scrape_data, Evaluation_form])

# Sidebar (will only show on non-home pages)
if st.get_option("client.showSidebarNavigation"):
    st.sidebar.info("""
    **App Features:**
    - Dashboard with data visualization
    - Direct data scraping
    - Data download options
    - Evaluation forms integration
    """)

# Run navigation
pg.run()