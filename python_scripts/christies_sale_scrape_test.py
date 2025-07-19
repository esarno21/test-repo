import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = "https://www.christies.com/en/calendar"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

data = []

# Loop over full tile container
for container in soup.select('.container-fluid.chr-event-tile__container--full'):
    try:
        # Sale type
        sale_type_elem = container.select_one('.chr-event-tile__event-type')
        sale_type = sale_type_elem.get_text(strip=True) if sale_type_elem else None

        # Sale name and URL
        title_elem = container.select_one('.chr-event-tile__title')
        sale_name = title_elem.get_text(strip=True) if title_elem else None
        sale_url = None
        if title_elem and title_elem.has_attr('href'):
            href = title_elem['href']
            sale_url = 'https://www.christies.com' + href if not href.startswith('http') else href

        # Auction number from URL
        auction_number = None
        if sale_url:
            match = re.search(r'-(\d+)/?$', sale_url)
            if match:
                auction_number = match.group(1)

        # Sale status (event date)
        status_elem = container.select_one('.chr-event-tile__status span[aria-hidden="true"]')
        sale_status = status_elem.get_text(strip=True) if status_elem else None

        # Location
        location_elem = container.select_one('.chr-event-tile__location')
        sale_location = location_elem.get_text(strip=True) if location_elem else None

        # Department
        dept_elem = container.select_one('.chr-event-tile__department')
        sale_department = dept_elem.get_text(strip=True) if dept_elem else None

        # Image URL
        img_elem = container.select_one('.chr-event-tile__image img')
        image_url = img_elem['src'] if img_elem and img_elem.has_attr('src') else None
        if image_url and image_url.startswith('//'):
            image_url = 'https:' + image_url

        # Collect data
        data.append({
            'sale_type': sale_type,
            'sale_name': sale_name,
            'sale_url': sale_url,
            'auction_number': auction_number,
            'sale_status': sale_status,
            'sale_location': sale_location,
            'sale_department': sale_department,
            'image_url': image_url
        })

    except Exception as e:
        print("Error parsing container:", e)

# Output
df = pd.DataFrame(data)
print(df)

# Optional: save to CSV
df.to_csv("christies_calendar_full.csv", index=False)
