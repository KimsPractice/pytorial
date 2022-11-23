from requests import get
from bs4 import BeautifulSoup
from extractors.weworkremotely import extract_weworkremotely_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

browser = webdriver.Chrome(options=options)
browser.get(f"{base_url}{search_term}")

soup = BeautifulSoup(browser.page_source,"html.parser")
job_lists = soup.find('ul', class_='jobsearch-ResultsList')
jobs = job_lists.find_all('li',recursive=False)

for job in jobs:
  zone = job.find("div",class_="mosaic-zone")
  if zone == None:
    print("job li")