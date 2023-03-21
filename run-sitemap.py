from selenium import webdriver
import random
import time
import requests
import xml.etree.ElementTree as ET

# Website URL and sitemap.xml URL
website_url = 'https://kevintan.pro'
sitemap_url = website_url + '/sitemap.xml'

# Define user-agent list, visit count and visit interval
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; Pixel 5 Build/RQ3A.210805.001.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 Build/OPD1.170811.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1',
    'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1',
    'Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
    'Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
]
num_visits = 10
min_interval = 1
max_interval = 10

# Get sitemap.xml content from website
response = requests.get(sitemap_url)
sitemap_content = response.content

# Parse the XML content of sitemap.xml to extract URLs
sitemap_tree = ET.fromstring(sitemap_content)
sitemap_urls = [element[0].text for element in sitemap_tree]

# Create a list to hold the ChromeDriver objects
drivers = []

# Loop to create ChromeDriver objects and open windows
for i in range(num_visits):
    # Create ChromeOptions object with a random user-agent
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'user-agent={random.choice(user_agents)}')

    # Create a new ChromeDriver object with the ChromeOptions
    driver = webdriver.Chrome(options=chrome_options)
    drivers.append(driver)

    # Open a random URL from the sitemap
    url = random.choice(sitemap_urls)
    driver.get(url)
    print(f'[Window {i+1}] Current URL: {driver.current_url}')

# Loop to scroll the pages and wait for a random interval
for i, driver in enumerate(drivers):
    # Randomly scroll up or down by a random distance
    scroll_distance = random.randint(100, 300)
    scroll_direction = random.choice(['up', 'down'])
    if scroll_direction == 'up':
        driver.execute_script(f'window.scrollBy(0, -{scroll_distance})')
    else:
        driver.execute_script(f'window.scrollBy(0, {scroll_distance})')

    # Wait for a random interval before scrolling again
    time_interval = random.randint(min_interval, max_interval)
    print(f'[Window {i+1}] Waiting {time_interval} seconds before scrolling again...')
    time.sleep(time_interval)

# Loop to wait for a random interval and then close the windows
for i, driver in enumerate(drivers):
    # Wait for a random interval before closing the window
    time_interval = random.randint(min_interval, max_interval)
    print(f'[Window {i+1}] Waiting {time_interval} seconds before closing the window...')
    time.sleep(time_interval)

    # Close the Chrome window
    driver.quit()
