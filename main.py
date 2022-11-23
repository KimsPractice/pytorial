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

print(browser.page_source)