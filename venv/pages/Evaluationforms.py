import streamlit as st
import pandas as pd

st.title("📝 Evaluation Forms")

st.info("""
### **How did you like our app?**
Please fill in one of the following forms (or both) to help us improve. Your response would be appreciated.  

**Note:** Both forms will open in a new window.
""")

st.markdown("---")

col1, col2 = st.columns(2)

# URLs
kobotoolbox_url = "https://ee.kobotoolbox.org/x/zZ3tUhbQ"
google_form_url = "https://forms.gle/DhyHTy7F2iNpYJQH8"

# Kobotoolbox Column
with col1:
    st.image("data/kobotoolbox.png", width=100)
    if st.button("Open Kobotoolbox Form", type="primary"):
        # Auto-redirect using JS
        redirect_script = f"""
            <meta http-equiv="refresh" content="0; url={kobotoolbox_url}">
            <a href="{kobotoolbox_url}" target="_blank">Click here if not redirected</a>
        """
        st.markdown(redirect_script, unsafe_allow_html=True)

# Google Forms Column
with col2:
    
    st.image("https://www.gstatic.com/images/branding/product/1x/forms_2020q4_48dp.png", width=100)
    if st.button("Open Google Form", type="primary"):
        redirect_script = f"""
            <meta http-equiv="refresh" content="0; url={google_form_url}">
            <a href="{google_form_url}" target="_blank">Click here if not redirected</a>
        """
        st.markdown(redirect_script, unsafe_allow_html=True)
