import requests
from bs4 import BeautifulSoup

# set usl root
url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

# This is for checking request success
# print(response.status_code)

soup = BeautifulSoup(
    response.content, 
    "html.parser",
    )

# to find class in html, you have to use class_
# soup can use find method after use it.
jobs = soup.find("section", class_="jobs").find_all("li")[1:-1] # [1:-1] is just for passing first and end things of "li"

# This variable saves job_data dictionary
all_jobs = []

# find_all method return list
# The data type of jobs is List
for job in jobs:
    title = job.find("span", class_="title").text

    # named contain 'company' class was three, so I made three variable
    company, contract_type, region = job.find_all("span", class_="company")

    # get text data from <span>
    company = company.text
    contract_type = contract_type.text
    region = region.text

    # if can't find it, return None
    url = job.find("div", class_="tooltip--flag-logo").next_sibling
    
    # This is for checking success
    if url:
        url = url["href"]


    job_data = {
        "title":title,
        "company":company,
        "Contract_type":contract_type,
        "region":region,
        "url":f"https://weworkremotely.com" + url,
    }

    # add job information in all_jobs
    all_jobs.append(job_data)

# check the all_jobs
for i in all_jobs:
    print(i)