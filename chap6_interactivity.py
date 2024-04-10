from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

# Code challenge (6.10 Interactivity class)
"""
1. make the lecture code to function
2. Revise code to work with keyword list
    # Example
    keyword = [
        "flutter",
        "java",
        "kotlin"
    ]
"""
def get_content_from_playwright(url):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    content = page.content()
    p.stop()
    return content

# This keyword get only one string
# If you want to use ths function with keyword list, use for loop
def web_scraper(keyword):
    url = f"https://www.wanted.co.kr/search?query={keyword}&tab=position"
    content = get_content_from_playwright(url)
    soup = BeautifulSoup(content, "html.parser")

    # 직업 목록에 해당하는 내용을 리스트로 받음
    jobs = soup.find_all("div", class_="JobCard_container__FqChn")

    jobs_db = []

    for job in jobs:
    
        link = f"https://www.wanted.co.kr{job.find('a')['href']}"
        title = job.find("strong", class_="JobCard_title__ddkwM").text
        company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
        reward = job.find("span", class_="JobCard_reward__sdyHn").text

        job = {
            "title":title,
            "company_name":company_name,
            "reward":reward,
            "link":link
        }
        jobs_db.append(job)

    # open jobs.csv if not, It make jobs.csv. Mode : write
    file = open(f"{keyword}.csv", "w") 
    writter = csv.writer(file)
    # writerow method는 리스트 형식의 데이터를 매개변수로 받음
    writter.writerow(
            [
                "Title",
                "Company",
                "Reward",
                "Link"
        ]
    )
    for job in jobs_db:
        writter.writerow(job.values())

    file.close()


keyword = [
    "flutter",
    "java",
    "kotlin"
]

for kw in keyword:
    web_scraper(kw)
