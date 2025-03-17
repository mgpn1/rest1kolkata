import os
import urllib.request
import time

def download_image(url, filename):
    try:
        print(f"Downloading: {filename}")
        urllib.request.urlretrieve(url, filename)
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
    'images/logo.png': 'https://raw.githubusercontent.com/your-username/your-repo/main/logo.png',  # You'll need to replace this with an actual logo
    'images/hero-bg.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4',
    'images/contact-bg.jpg': 'https://images.unsplash.com/photo-1552566626-52f8b828add9',
    
    # Menu images
    'images/menu/samosa.jpg': 'https://images.unsplash.com/photo-1601050690597-df0568f70950',
    'images/menu/pakora.jpg': 'https://images.unsplash.com/photo-1606491956689-2ea866880c84',
    'images/menu/biryani.jpg': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8',
    'images/menu/butter-chicken.jpg': 'https://images.unsplash.com/photo-1603894584373-5ac82b2ae398',
    'images/menu/rasgulla.jpg': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe',
    'images/menu/gulab-jamun.jpg': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe',
    'images/menu/mango-lassi.jpg': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe',
    'images/menu/masala-chai.jpg': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe',
    'images/menu-header.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4',
    
    # About page images
    'images/about/header-bg.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4',
    'images/about/restaurant-interior.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4',
    'images/about/chef1.jpg': 'https://images.unsplash.com/photo-1577219491135-ce391730fb2c',
    'images/about/chef2.jpg': 'https://images.unsplash.com/photo-1577219491135-ce391730fb2c',
    'images/about/chef3.jpg': 'https://images.unsplash.com/photo-1577219491135-ce391730fb2c',
    
    # Reservations page images
    'images/reservations/header-bg.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4',
    'images/reservations/wedding.jpg': 'https://images.unsplash.com/photo-1519741497674-611481863552',
    'images/reservations/corporate.jpg': 'https://images.unsplash.com/photo-1497366216548-37526070297c',
    'images/reservations/party.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4',
    
    # Specialty images
    'images/specialty1.jpg': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8',
    'images/specialty2.jpg': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8',
    'images/specialty3.jpg': 'https://images.unsplash.com/photo-1606491956689-2ea866880c84'
}

# Download all images
for filename, url in images.items():
    download_image(url, filename) 