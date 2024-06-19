import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "lxml")

results = soup.find(id="ResultsContainer") # This the container for all results

career = input("What Jobs Do You Want to Work With:")

available_jobs = results.find_all(
    "h2", string=lambda text: career in text.lower()
)

available_jobs_elements = [
    h2_element.parent.parent.parent for h2_element in available_jobs
]

if len(available_jobs) > 0:
    print("There's", len(available_jobs) ,"Jobs Available")
    for job_element in available_jobs_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print("Title:", title_element.text.strip())
        print("Company:", company_element.text.strip())
        print("Location:", location_element.text.strip())
        print()
else:
    print("No Jobs Avaialbel For This Career")



# job_elements = results.find_all("div", class_="card-content") # All Job Profile

# This find all the job we only need to find python jobs
# for job_element in job_elements:  # Enumerating on jobs like array seperating
    # title_element = job_element.find("h2", class_="title")
    # company_element = job_element.find("h3", class_="company")
    # location_element = job_element.find("p", class_="location")
    # print("Title:", title_element.text.strip())
    # print("Company:", company_element.text.strip())
    # print("Location:", location_element.text.strip())
    # print()