from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


def get_page_count(keyword):
  base_url = "https://kr.indeed.com/jobs?q="

  browser = webdriver.Chrome(options=options)
  browser.get(f"{base_url}{keyword}")

  soup = BeautifulSoup(browser.page_source, "html.parser")
  pagination = soup.find("nav", {'aria-label': "pagination"})
  if pagination == None or len(pagination) == 0:
    print("don't find pagination")
    return 1
  pages = pagination.find_all("div", recursive=False)
  count = len(pages)
  if count > 5:
    return 5
  else:
    return count


def extractors_indeed_jobs(keyword):
  pages = get_page_count(keyword)
  results = []
  for page in range(pages):
    base_url = "https://kr.indeed.com/jobs?q="
    final_url = f"{base_url}{keyword}&start={page*10}"
    browser = webdriver.Chrome(options=options)
    browser.get(final_url)

    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_lists = soup.find('ul', class_='jobsearch-ResultsList')
    jobs = job_lists.find_all('li', recursive=False)

    for job in jobs:
      zone = job.find("div", class_="mosaic-zone")
      if zone == None:
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']

        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")

        job_data = {
          "link": f"https://kr.indeed.com{link}",
          "company": company.string.replace(",", " "),
          "location": location.string.replace(",", " "),
          "position": title.replace(",", " ")
        }
        results.append(job_data)
  return results