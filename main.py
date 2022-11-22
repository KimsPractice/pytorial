from requests import get
from bs4 import BeautifulSoup
from extractors.weworkremotely import extract_weworkremotely_jobs

jobs = extract_weworkremotely_jobs("python")
print(jobs)