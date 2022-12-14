from flask import Flask,render_template,request
from extractors.indeed import extractors_indeed_jobs
from extractors.weworkremotely import extract_weworkremotely_jobs

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search")
def hello():
  keyword = request.args.get("keyword")
  if keyword in db:
    jobs = db[keyword]
  else:
    indeed = extractors_indeed_jobs(keyword)
    weworkremotly = extract_weworkremotely_jobs(keyword)
    jobs = weworkremotly
    db[keyword] = jobs
  return render_template("search.html" , keyword=keyword, jobs=jobs)


app.run("0.0.0.0")