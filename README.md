# Federal Technology Workforce Analytics Dashboard

## Overview

This project analyzes federal technology job postings from the USAJobs API to identify trends in technical skill demand, salary ranges, hiring agencies, and geographic distribution. The goal was to use real government workforce data to understand which technical skills are most valuable in the federal technology job market.

## Objectives

* Identify the most frequently requested technical skills in federal technology positions.
* Analyze salary trends across technology-related roles.
* Determine which government agencies hire the most technology professionals.
* Explore geographic patterns in federal technology hiring.
* Create an interactive Power BI dashboard for workforce analytics.

## Technologies Used

* Python
* Pandas
* Regular Expressions (Regex)
* Requests
* Power BI
* Git/GitHub
* USAJobs API

## Data Source

Job posting data was collected from the USAJobs API, the official job portal for the United States Federal Government.

Data included:

* Job titles
* Agencies
* Locations
* Salary ranges
* Job summaries
* Requirements and evaluations

## Project Workflow

1. Pulled job postings using the USAJobs API.
2. Cleaned and standardized salary and job posting data using Python.
3. Extracted technical skills from job descriptions using regular expressions.
4. Generated datasets measuring skill demand and salary trends.
5. Built an interactive Power BI dashboard to visualize findings.

## Dashboard Metrics

The dashboard includes:

* Total technology job postings
* Average salary
* Top hiring agencies
* Most requested technical skills
* Salary by skill
* Geographic distribution of jobs

## Key Findings

* Java and Javascript were among the most frequently requested technical skills.
* Skills such as SQL and data visualization were associated with higher salaries.
* Federal technology hiring was concentrated in major government employment hubs.


## Future Improvements

* Expand skill extraction using NLP techniques.
* Add trend analysis over time.
* Build predictive models for salary estimation.
* Incorporate additional federal workforce datasets.

## Author

Michael Coleman

