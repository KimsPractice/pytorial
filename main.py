from extractors.weworkremotely import extract_weworkremotely_jobs
from extractors.indeed import extractors_indeed_jobs

keyword = input("What do you want to search for ???")

indeed = extractors_indeed_jobs(keyword)
weworkremotely = extract_weworkremotely_jobs(keyword)

jobs = indeed + weworkremotely

file = open(f"{keyword}.csv","w",encoding="utf-8-sig")

file.write("Position,Comapny,Location,URL\n")

for job in jobs:
  file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()

print("done")