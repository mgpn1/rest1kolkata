import os
import urllib.request
import time

def download_image(url, filename):
    try:
        print(f"Downloading: {filename}")
        # Add Unsplash parameters for better quality images
        if 'unsplash.com' in url:
            url = url + '?q=80&w=1000&auto=format&fit=crop'
        # Add custom headers to avoid 403 errors
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            with open(filename, 'wb') as f:
                f.write(response.read())
        print(f"Successfully downloaded: {filename}")
        time.sleep(1)  # Add a small delay between downloads
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")

# Create directories if they don't exist
directories = ['images', 'images/menu', 'images/about', 'images/reservations']
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Image URLs from Unsplash and other free sources
images = {
    # Main images
    'images/hero-bg.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4',
    'images/contact-bg.jpg': 'https://images.unsplash.com/photo-1552566626-52f8b828add9',
    
    # Menu images
    'images/menu/samosa.jpg': 'https://images.unsplash.com/photo-1601050690597-df0568f70950',
    'images/menu/pakora.jpg': 'https://images.unsplash.com/photo-1606491956689-2ea866880c84',
    'images/menu/biryani.jpg': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8',
    'images/menu/butter-chicken.jpg': 'https://images.unsplash.com/photo-1603894584373-5ac82b2ae398',
    # Updated dessert and beverage images
    'images/menu/rasgulla.jpg': 'https://images.unsplash.com/photo-1589302574356-111c401b9613',  # Updated Rasgulla image
    'images/menu/gulab-jamun.jpg': 'https://images.unsplash.com/photo-1582716401301-b2407dc7563d',  # Updated Gulab Jamun image
    'images/menu/mango-lassi.jpg': 'https://images.unsplash.com/photo-1553530979-7ee52a2670c4',
    'images/menu/masala-chai.jpg': 'https://images.unsplash.com/photo-1561336313-0bd5e0b27ec8',
    'images/menu-header.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4',
    
    # About page images
    'images/about/header-bg.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4',
    'images/about/restaurant-interior.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4',
    'images/about/chef1.jpg': 'https://images.unsplash.com/photo-1577219491135-ce391730fb2c',  # Rajesh Kumar
    'images/about/chef2.jpg': 'https://images.unsplash.com/photo-1583394293214-28ded15ee548',  # Amit Patel
    'images/about/chef3.jpg': 'https://images.unsplash.com/photo-1583394293214-28ded15ee548',  # Priya Sharma
    
    # Reservations page images
    'images/reservations/header-bg.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4',
    'images/reservations/wedding.jpg': 'https://images.unsplash.com/photo-1519741497674-611481863552',
    'images/reservations/corporate.jpg': 'https://images.unsplash.com/photo-1497366216548-37526070297c',
    'images/reservations/party.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4',
    
    # Specialty images - Updated Indian Thali image
    'images/specialty1.jpg': 'https://images.unsplash.com/photo-1598023696416-0193a0bcd302',  # Updated Indian Thali
    'images/specialty2.jpg': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8',
    'images/specialty3.jpg': 'https://images.unsplash.com/photo-1606491956689-2ea866880c84'
}

print("Starting to download updated images...")
# Download all images
for filename, url in images.items():
    download_image(url, filename)
print("Finished downloading updated images.") 