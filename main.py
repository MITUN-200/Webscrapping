# Integerate this with your fastApi project

from bs4 import BeautifulSoup
import requests


url = requests.get('https://internshala.com/internships/work-from-home-internships/').text
soup = BeautifulSoup(url,'lxml')
containers = soup.find_all('div', class_= 'container-fluid individual_internship visibilityTrackerItem')
for index,container in enumerate(containers):
    # Use strip function to remove unnessarcy spaces
    company_name = container.find('h4', class_ ='heading_6 company_name').strip()
    position = container.find('h3',class_ ='heading_4_5 profile').text
    location = container.find('a', class_ ='location_link view_detail_button').text
    published = container.find('div', class_ ='status-container').text
    more_info=container.div.h3.a['href']
    # Please return the following through a fast api response
