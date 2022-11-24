from extractors.weworkremotely import extract_weworkremotely_jobs
from extractors.indeed import extractors_indeed_jobs

keyword = input("What do you want to search for ???")

indeed = extractors_indeed_jobs(keyword)
weworkremotely = extract_weworkremotely_jobs(keyword)

jobs = indeed + weworkremotely

for job in jobs:
  print(jobs)
  print("//////////////////////////////////////////")