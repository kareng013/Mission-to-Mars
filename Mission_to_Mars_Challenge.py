# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


df.to_html()

# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

browser.visit(url)

html_hemisphere = browser.html
soup1 = soup(html_hemisphere, 'html.parser')
# Retrieve each hemisphere
check = soup1.find_all('a', class_='itemLink product-item')
print(check)
items = soup1.find_all('div', class_='item')

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
org_url = 'https://astrogeology.usgs.gov'

for i in items:
    # Extract title
    title = i.find('h3').text
    # Extract url for each hemisphere
    link = i.find('a', class_='itemLink product-item')['href']
    new_url = org_url + link
    # print(new_url)
    # Visit url for each hemisphere
    browser.visit(new_url)
    html1 = browser.html
    soup2 = soup(html1, 'html.parser')
    # Select jpg image
    hem_img = soup2.find('div', class_='downloads')
    # Extract url of hemisphere jpg image
    img_url = hem_img.find('a')['href']
    # img_url = org_url + soup2.find('img', class_='wide-image')['src']
    print(img_url)
    # Append to dictionary
    hemispheres=dict({'img_url':img_url, 'title':title})
    # Append to list
    hemisphere_image_urls.append(hemispheres)
    
   
 # 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls
 
# 5. Quit the browser
browser.quit()





