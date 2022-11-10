from requests import get
from bs4 import BeautifulSoup

BASE_URL = "https://weworkremotely.com/remote-jobs/search?utf8=✓&term="
SEARCH = "python"


response = get(f"{BASE_URL}{SEARCH}")

if response.status_code != 200:
   print("Can't request website")
else:
   soup = BeautifulSoup(response.text,'html.parser')
   jobs = soup.find_all('section',class_='jobs')
   print(jobs)
