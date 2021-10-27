from json import loads
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import randint

# reading from career dictionary
with open('careers.txt', 'r') as f:
    careerMap = loads(f.read())
jobs = list(careerMap.values())[0]

# options to skip printing unnecessary chrome reports
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# creates instance of Chrome WebDriver
driver = webdriver.Chrome(options=options)

def login(browser):
    # implement login functionality
    browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    #Enter login info:
    elementID = browser.find_element(By.ID, "username")
    elementID.send_keys("Enter LinkedIn Username")
    elementID = browser.find_element(By.ID, "password")
    elementID.send_keys("Enter Password")
    elementID.submit()


def urlGenerate(keyword: str):
    keyword = keyword.lower().replace("engineers", "engineering").replace(" ", "%20")
    return "https://in.linkedin.com/jobs/search?keywords=%s&position=1&pageNum=0" %keyword

def locationFilter(s: str):
    for i in range(len(s)):
        if s[i].isdigit():
            return s[:i-1]
    return s

driver.maximize_window()

try: login(driver)
except Exception as e: print(e)

# fetching first 25 jobs data to avoid being restricted
for job in jobs[:25]:
    print("\n" + job + "\n")
    
    jobUrl = urlGenerate(job)
    driver.get(jobUrl)

    # wait until page loads properly
    try:
        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results")))
        sleep(2)
    except:
        print("No Jobs Available")
        continue
    try:
        jobSection = driver.find_element(By.CLASS_NAME, "jobs-search-results")
    except:
        print("No Jobs Available")
        continue

    # jobTiles holds a list of job cards in the jobSection
    jobTiles = driver.find_elements(By.CLASS_NAME, "job-card-container")
    
    # showing results for a maximum of 3 jobs
    Jobcount = min(len(jobTiles), 3)

    companies = []
    # loop 1, scraping job data
    for i in range(Jobcount):
        sleep(randint(1,2))
        # Rebuilding jobTiles since elements get stale when company page is visited
        jobTiles = driver.find_elements(By.CLASS_NAME, "job-card-container")

        # JobInfo - A list storing - a. Position b. Company Name c. Location 
        jobInfo = jobTiles[i].text.split("\n")[0:3]
        print("Job Name: " + jobInfo[0])
        print("Company Name: " + jobInfo[1])
        print("Location - " + jobInfo[2])
        print("________________________\n")
        companies.append(jobInfo[1])
        
        sleep(randint(2, 5))
    
    companies = list(set(companies))

    # loop 2, scraping company data
    for company in companies:
        try:
            companyLink = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, company)))
            companyLink.click()

        except Exception as e: 
            print("Company Data Unavailable")
            continue
        
        sleep(randint(2,5))
        # Checking company data availability
        try:
            companyData = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ph5")))
        except Exception as e:
            print("Company Data Unavailable")
            driver.back()
            continue

        # checking company summary availability
        try:
            description = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "org-top-card-summary__tagline")))
            desc = description.text
        except Exception as e:
            desc = "No Summary given"

        # checking company location availability
        try:
            loc = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "org-top-card-summary-info-list")))
            loc = locationFilter(loc.text)
        except Exception as e:
            loc = "Location Unavailable"

        # Checking company employee count availability
        try:
            emp = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "mt1")))
            emp = emp.text.split()[2]
        except Exception as e:
            emp = "Employee Count Unavailable"


        print("Company description: " + desc)
        print("Company Location: " + loc)
        print("No. of Employee's: " + emp)
        print("________________________\n")

        sleep(2)
        driver.back()