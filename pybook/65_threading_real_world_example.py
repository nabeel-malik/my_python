import requests
import time
import concurrent.futures

"""
Following are 2 scripts to download 15 high-res images from https://images.unsplash.com/:
    - Script 1: SYNCHRONOUS download of images
    - Script 2: THREADING to download images
"""

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

print('\n################################ Script 1: SYNCHRONOUS download of images ################################\n')

t1 = time.perf_counter()

for img_url in img_urls:
    img_bytes = requests.get(img_url).content
    img_name = img_url.split("/")[-1] + ".jpg"
    with open(f'work_directory/threading_real_world_example/synchronous/{img_name}', 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} downloaded.')

t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds.')

print('\n################################ Script 2: THREADING to download images ################################\n')


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split("/")[-1] + ".jpg"
    with open(f'work_directory/threading_real_world_example/threading/{img_name}', 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} downloaded.')

t1 = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds.')

"""
Corey's code reduced the time used to download images from about 30 seconds to 5 seconds using THREADING.
However, in our case, we hardly see any difference. This is not an issue with our script, but rather a wider problem
with Python's threading, where it is considered to be inefficient.

Read the following Stack Overflow thread for more information on this:
https://stackoverflow.com/questions/10154487/how-to-get-a-faster-speed-when-using-multi-threading-in-python
"""