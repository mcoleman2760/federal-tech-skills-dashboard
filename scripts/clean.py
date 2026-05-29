import pandas as pd
import re

RAW_FILE = "data/raw/usajobs_tech_jobs_raw.csv"
CLEANED_FILE = "data/cleaned/usajobs_tech_jobs_cleaned.csv"
SKILL_FILE = "data/cleaned/skill_demand.csv"
SALARY_SKILL_FILE = "data/cleaned/salary_by_skill.csv"

df = pd.read_csv(RAW_FILE)

# Rename columns to simpler names
df = df.rename(columns={
    "position_title": "job_title",
    "job_summary": "summary"
})

# Remove duplicate job postings
df = df.drop_duplicates(subset=["job_title", "organization", "location", "url"])

# Clean salary columns
df["min_salary"] = pd.to_numeric(df["min_salary"], errors="coerce")
df["max_salary"] = pd.to_numeric(df["max_salary"], errors="coerce")

# Create average salary even if one side is missing
df["avg_salary"] = df[["min_salary", "max_salary"]].mean(axis=1)

# Keep rows with salary data
df = df.dropna(subset=["avg_salary"])

# Fill missing text values
text_columns = [
    "job_title",
    "summary",
    "requirements",
    "evaluations"
]

for col in text_columns:
    df[col] = df[col].fillna("")

# Combine text into one searchable column
df["full_text"] = (
    df["job_title"] + " " +
    df["summary"] + " " +
    df["requirements"] + " " +
    df["evaluations"]
).str.lower()

# Skills to search for
skills = {
    "python": r"\bpython\b",
    "sql": r"\bsql\b",
    "excel": r"\bexcel\b|\bmicrosoft excel\b",
    "power_bi": r"\bpower bi\b|\bpowerbi\b",
    "tableau": r"\btableau\b",
    "r": r"\br programming\b|\blanguage r\b",
    "aws": r"\baws\b|\bamazon web services\b",
    "azure": r"\bazure\b",
    "java": r"\bjava\b",
    "javascript": r"\bjavascript\b|\bjs\b",
    "react": r"\breact\b|\breact.js\b|\breactjs\b",
    "node_js": r"\bnode.js\b|\bnodejs\b|\bnode js\b",
    "machine_learning": r"\bmachine learning\b|\bml\b",
    "statistics": r"\bstatistics\b|\bstatistical\b",
    "data_visualization": r"\bdata visualization\b|\bvisualization\b",
    "dynamodb": r"\bdynamodb\b",
    "api": r"\bapi\b|\bapis\b",
    "etl": r"\betl\b",
    "dashboard": r"\bdashboard\b|\bdashboards\b"
}

# Create True/False columns for each skill
for skill, pattern in skills.items():
    df[skill] = df["full_text"].apply(
        lambda text: bool(re.search(pattern, text))
    )

skill_columns = list(skills.keys())

# Count how many skills each job has
df["skill_count"] = df[skill_columns].sum(axis=1)

# Skill demand table
skill_demand_rows = []

for skill in skill_columns:
    count = int(df[skill].sum())
    percent = round((count / len(df)) * 100, 2) if len(df) > 0 else 0

    skill_demand_rows.append({
        "skill": skill,
        "job_count": count,
        "percent_of_jobs": percent
    })

skill_demand_df = pd.DataFrame(skill_demand_rows)
skill_demand_df = skill_demand_df.sort_values("job_count", ascending=False)

# Salary by skill table
salary_skill_rows = []

for skill in skill_columns:
    skill_jobs = df[df[skill]]

    salary_skill_rows.append({
        "skill": skill,
        "jobs_with_skill": len(skill_jobs),
        "avg_salary": round(skill_jobs["avg_salary"].mean(), 2),
        "avg_min_salary": round(skill_jobs["min_salary"].mean(), 2),
        "avg_max_salary": round(skill_jobs["max_salary"].mean(), 2)
    })

salary_by_skill_df = pd.DataFrame(salary_skill_rows)
salary_by_skill_df = salary_by_skill_df.sort_values("avg_salary", ascending=False)

# Save files
df.to_csv(CLEANED_FILE, index=False)
skill_demand_df.to_csv(SKILL_FILE, index=False)
salary_by_skill_df.to_csv(SALARY_SKILL_FILE, index=False)

print("Cleaning complete.")
print("Rows in cleaned dataset:", len(df))
print("Saved:", CLEANED_FILE)
print("Saved:", SKILL_FILE)
print("Saved:", SALARY_SKILL_FILE)

print("\nTop skills:")
print(skill_demand_df.head(10))