import requests
import pprint
from bs4 import BeautifulSoup

URL = 'https://www.linkedin.com/jobs/search/?f_L=San%20Francisco%20Bay%20Area&geoId=90000084&keywords=software%20engineer&location=San%20Francisco%20Bay%20Area'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_='results__list')
job_elems = results.find_all('li', class_="job-result-card")

for job_elem in job_elems:
    title_elem = job_elem.find('h3', class_='result-card__title')
    company_elem = job_elem.find('h4', class_='result-card__subtitle')
    location_elem = job_elem.find('span', class_='job-result-card__location')
    print(title_elem.text)
    print(company_elem.text)
    print(location_elem.text)
    print()

# print(len(job_elems))
