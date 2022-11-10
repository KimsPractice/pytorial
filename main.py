from requests import get

BASE_URL = "https://weworkremotely.com/remote-jobs/search?term="
SEARCH = "python"


response = get(f"{BASE_URL}{SEARCH}")

if response.status_code != 200:
   print("Can't request website")
else:
   print(response.text)
