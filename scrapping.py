import requests
from bs4 import BeautifulSoup
import sys
import time

files_type = ['.com', '.css', '.js', '.png', '.ico']
css_files = []
js_files = []
img_files = []

# Make a request to the website
response = requests.get(sys.argv[1])

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

def get_resourses_links():
    print()
    print(" Resourses ".center(20, "#"))
    print()
    links = soup.find_all('link')
    for link in links:
        if link.get('href') != None:
            print(">> "+link.get('href'))
            time.sleep(.3)
        

def get_other_pages_links():
    print()
    print(" Other Sites ".center(20, "#"))
    print()
    links = soup.find_all('a')
    for link in links:
        if link.get('href') != None:
            print(">> "+link.get('href'))
            time.sleep(.3)

def get_imgs():
    print()
    print(" Images ".center(20, "#"))
    print()
    links = soup.find_all('img')
    for link in links:
        if link.get('src') != None:
            print(">> "+link.get('src'))
            time.sleep(.3)

def get_vids():
    print()
    print(" Videos ".center(20, "#"))
    print()
    links = soup.find_all('video')
    for link in links:
        if link.get('src') != None:
            print(">> "+link.get('src'))
            time.sleep(.3)

get_other_pages_links()
get_imgs()
get_resourses_links()
get_vids()

# print(soup.prettify())

fs = open('hello.html', 'w')
fs.write(str(response.content))
fs.close()