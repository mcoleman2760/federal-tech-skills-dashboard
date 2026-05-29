import pandas as pd

skills = pd.read_csv("data/cleaned/skill_demand.csv")
salary = pd.read_csv("data/cleaned/salary_by_skill.csv")

print("\nTOP 10 MOST REQUESTED SKILLS")
print(skills.head(10))

print("\nTOP 10 HIGHEST PAYING SKILLS")
print(
    salary.sort_values(
        "avg_salary",
        ascending=False
    ).head(10)
)