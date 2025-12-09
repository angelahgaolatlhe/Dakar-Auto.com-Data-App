# pages/Scrape_data.py
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Scrape Data",
    page_icon="🔍",
    layout="wide"
)

# Title and description
st.markdown("<h2 style='text-align:center; color: #1E3A8A; '>Dakar-Auto.com Data Scraper</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Scrape data directly from <a href='https://dakar-auto.com' target='_blank'>Dakar-Auto.com</a></p>", unsafe_allow_html=True)
st.markdown("---")

# Sections to scrape data from
vehicle_type = st.radio(
    "Select Section:",
    ["Cars", "Motorcycles & Scooters", "Car Rentals"],
    horizontal=True
)

st.markdown("---")

# Common scraping function
def scrape_data(url_template, num_pages_to_scrape, vehicle_category="cars"):
    df = pd.DataFrame()
    scraped_data = []
    
    # Progress bar and status
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for index in range(1, num_pages_to_scrape + 1):
        # Update progress
        progress = index / num_pages_to_scrape
        progress_bar.progress(progress)
        status_text.text(f"Scraping page {index} of {num_pages_to_scrape}...")
        
        url = url_template.format(index)
        
        try:
            # Get page content
            res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(res.content, "html.parser")
            containers = soup.find_all("div", "listings-cards__list-item mb-md-3 mb-3")
            
            # Scrape each container
            for container in containers:
                try:
                    # Container URL
                    container_url = "https://dakar-auto.com" + container.find("a")["href"]
                    
                    # Get container page
                    res_container = requests.get(container_url, headers={'User-Agent': 'Mozilla/5.0'})
                    soup_container = BeautifulSoup(res_container.content, "html.parser")
                    
                    # Get model information
                    model_info = soup_container.find("h1", "listing-item__title")
                    if model_info:
                        model_text = model_info.text.strip().split()
                        brand = " ".join(model_text[0:2]) if len(model_text) >= 2 else model_text[0] if model_text else ""
                    else:
                        brand = ""
                    
                    # Get price
                    price_element = soup_container.find("h4", "listing-item__price font-weight-bold text-uppercase mb-2")
                    price = "".join(price_element.text.strip().replace(" F CFA", "").split()) if price_element else ""
                    
                    # Get address
                    address_element = soup_container.find("span", "listing-item__address-location")
                    if address_element:
                        address = address_element.text.strip().split()
                        town_suburb = address[0] if address else ""
                        region = address[-1] if len(address) > 1 else ""
                    else:
                        town_suburb = ""
                        region = ""
                    
                    # Get vehicle details
                    gen_info_element = soup_container.find("div", "listing-item__properties my-3")
                    
                    # Get owner
                    owner_element = soup_container.find("h4", "listing-item-sidebar__author-name")
                    owner = owner_element.text.strip() if owner_element else ""
                    
                    if vehicle_category == "cars":
                        # Car-specific fields
                        if gen_info_element:
                            gen_info = gen_info_element.text.strip().split()
                        else:
                            gen_info = []
                        
                        kilometerage = gen_info[0] if gen_info else ""
                        fuel = gen_info[-1] if len(gen_info) > 1 else ""
                        gearbox = gen_info[-2] if len(gen_info) > 2 else ""
                        year = gen_info[-3] if len(gen_info) > 3 else ""
                        
                        record = {
                            "vehicle_type": "Car",
                            "brand": brand,
                            "year": year,
                            "price": price,
                            "town_suburb": town_suburb,
                            "region": region,
                            "kilometerage": kilometerage,
                            "fuel": fuel,
                            "gearbox": gearbox,
                            "owner": owner,
                            "page_scraped": index,
                            "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                    
                    elif vehicle_category == "motorcycles":
                        # Motorcycle-specific fields
                        if gen_info_element:
                            gen_info = gen_info_element.text.strip().split()
                        else:
                            gen_info = []
                        
                        kilometerage = gen_info[0] if gen_info else ""
                        year = gen_info[3] if len(gen_info) > 3 else ""
                        
                        record = {
                            "vehicle_type": "Motorcycle",
                            "brand": brand,
                            "year": year,
                            "price": price,
                            "town_suburb": town_suburb,
                            "region": region,
                            "kilometerage": kilometerage,
                            "owner": owner,
                            "page_scraped": index,
                            "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                    
                    else:  # rentals
                        # Rental-specific fields
                        if gen_info_element:
                            gen_info = gen_info_element.text.strip().split()
                            year = gen_info[3] if len(gen_info) > 3 else ""
                        else:
                            year = ""
                        
                        record = {
                            "vehicle_type": "Car Rental",
                            "brand": brand,
                            "year": year,
                            "price": price,
                            "town_suburb": town_suburb,
                            "region": region,
                            "owner": owner,
                            "page_scraped": index,
                            "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                    
                    scraped_data.append(record)
                    
                except Exception as e:
                    continue
                    
            # Small delay to be respectful to the server
            time.sleep(1)
            
        except Exception as e:
            st.warning(f"Error scraping page {index}: {str(e)}")
            continue
    
    # Clear progress indicators
    progress_bar.empty()
    status_text.empty()
    
    # Create DataFrame
    if scraped_data:
        df = pd.DataFrame(scraped_data)
    else:
        st.warning(f"No {vehicle_category} data was scraped.")
    
    return df

# Set page limits
if "Rentals" in vehicle_type:
    max_pages = 9
    default_pages = 1
else:
    max_pages = 50
    default_pages = 1

num_pages = st.number_input(
    f"Enter number of pages to scrape (1-{max_pages}):",
    min_value=1,
    max_value=max_pages,
    value=default_pages,
    step=1,
    key=f"num_pages_{vehicle_type}"
)

# Display the URL pattern based on selection
if "Cars" in vehicle_type:
    url_display = "https://dakar-auto.com/senegal/voitures-4?&page=[1-{num_pages}]"
    vehicle_category = "cars"
    vehicle_name = "cars"
elif "Motorcycles" in vehicle_type:
    url_display = "https://dakar-auto.com/senegal/motos-and-scooters-3?&page=[1-{num_pages}]"
    vehicle_category = "motorcycles"
    vehicle_name = "motorcycles"
else:
    url_display = "https://dakar-auto.com/senegal/location-de-voitures-19?&page=[1-{num_pages}]"
    vehicle_category = "rentals"
    vehicle_name = "car rentals"

st.info(f"Scraping from: `{url_display.replace('{num_pages}', str(num_pages))}`")

# Scrape button
if st.button("Start Scraping", type="primary", key="scrape_button"):
    # Start scraping based on selection
    with st.spinner("Scraping in progress..."):
        if "Cars" in vehicle_type:
            url_template = 'https://dakar-auto.com/senegal/voitures-4?&page={}'
        elif "Motorcycles" in vehicle_type:
            url_template = 'https://dakar-auto.com/senegal/motos-and-scooters-3?&page={}'
        else:
            url_template = 'https://dakar-auto.com/senegal/location-de-voitures-19?&page={}'
        
        df_result = scrape_data(url_template, num_pages, vehicle_category)
        
        # Display results
        if not df_result.empty:
            st.success(f"Successfully scraped {len(df_result)} {vehicle_name} from {num_pages} pages!")
            
            # Show data preview
            st.subheader("Data Preview")
            st.dataframe(df_result.head(), use_container_width=True)
            
            # Download section
            st.markdown("---")
            st.subheader("Download Data")
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M")
            filename = f"dakar_auto_{vehicle_category}_{timestamp}.csv"
            
            # Convert DataFrame to CSV
            csv_data = df_result.to_csv(index=False).encode('utf-8')
            
            # Download button
            st.download_button(
                label=f"Download {vehicle_name.title()} Data",
                data=csv_data,
                file_name=filename,
                mime="text/csv",
                key=f"download_{vehicle_category}"
            )
            
            # Also show data in an expander
            with st.expander("View All Data"):
                st.dataframe(df_result, use_container_width=True)
                st.write(f"**Total records:** {len(df_result)}")
            
        else:
            st.error(f"No {vehicle_name} data was scraped. The website structure might have changed.")