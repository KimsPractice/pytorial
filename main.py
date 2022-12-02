from extractors.weworkremotely import extract_weworkremotely_jobs
from extractors.indeed import extractors_indeed_jobs
from file import save_to_file

keyword = input("What do you want to search for ???")

indeed = extractors_indeed_jobs(keyword)
weworkremotely = extract_weworkremotely_jobs(keyword)

jobs = indeed + weworkremotely

save_to_file(keyword,jobs)

print("done")