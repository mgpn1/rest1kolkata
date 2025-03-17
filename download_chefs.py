import os
import urllib.request
import time
import sys

def download_image(url, filename):
    try:
        print(f"Downloading: {filename}")
        # Add Unsplash parameters for better quality images
        if 'unsplash.com' in url:
            url = url + '?q=80&w=1000&auto=format&fit=crop'
        # Add custom headers to avoid 403 errors
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://unsplash.com/'
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                with open(filename, 'wb') as f:
                    f.write(response.read())
                print(f"Successfully downloaded: {filename}")
                return True
            else:
                print(f"Failed to download {filename}: HTTP {response.status}")
                return False
        time.sleep(1)  # Add a small delay between downloads
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")
        return False

# Create directory if it doesn't exist
os.makedirs('images/about', exist_ok=True)

# Chef image URLs - Updated with Indian people's photos
chef_images = {
    'images/about/chef1.jpg': 'https://images.unsplash.com/photo-1480429370139-e0132c086e2a',  # Rajesh Kumar - Indian male professional
    'images/about/chef2.jpg': 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d',  # Amit Patel - Indian male professional
    'images/about/chef3.jpg': 'https://images.unsplash.com/photo-1603415526960-f7e0328c63b1',  # Vikram Singh - Indian male professional
}

print("Starting to download chef images...")
success_count = 0
# Download chef images
for filename, url in chef_images.items():
    if download_image(url, filename):
        success_count += 1

print(f"Finished downloading chef images. Successfully downloaded {success_count} out of {len(chef_images)} images.")
if success_count < len(chef_images):
    print("Some images failed to download. Please check the error messages above.") 