import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("USAJOBS_EMAIL")
API_KEY = os.getenv("USAJOBS_API_KEY")

BASE_URL = "https://data.usajobs.gov/api/search"

headers = {
    "Host": "data.usajobs.gov",
    "User-Agent": EMAIL,
    "Authorization-Key": API_KEY
}

keywords = [
    "data analyst",
    "data scientist",
    "software developer",
    "software engineer",
    "IT specialist"
]

all_jobs = []

for keyword in keywords:
    print(f"Pulling jobs for: {keyword}")

    params = {
        "Keyword": keyword,
        "ResultsPerPage": 500,
        "Page": 1
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    data = response.json()

    jobs = data["SearchResult"]["SearchResultItems"]

    for job in jobs:
        item = job["MatchedObjectDescriptor"]

        all_jobs.append({
            "keyword_searched": keyword,
            "position_title": item.get("PositionTitle"),
            "organization": item.get("OrganizationName"),
            "department": item.get("DepartmentName"),
            "location": item.get("PositionLocationDisplay"),
            "min_salary": item.get("PositionRemuneration", [{}])[0].get("MinimumRange"),
            "max_salary": item.get("PositionRemuneration", [{}])[0].get("MaximumRange"),
            "salary_type": item.get("PositionRemuneration", [{}])[0].get("RateIntervalCode"),
            "start_date": item.get("PublicationStartDate"),
            "end_date": item.get("ApplicationCloseDate"),
            "job_summary": item.get("UserArea", {}).get("Details", {}).get("JobSummary"),
            "requirements": item.get("UserArea", {}).get("Details", {}).get("Requirements"),
            "evaluations": item.get("UserArea", {}).get("Details", {}).get("Evaluations"),
            "url": item.get("PositionURI")
        })

df = pd.DataFrame(all_jobs)

df.to_csv("data/raw/usajobs_tech_jobs_raw.csv", index=False)

print("Saved data/raw/usajobs_tech_jobs_raw.csv")
print(df.shape)