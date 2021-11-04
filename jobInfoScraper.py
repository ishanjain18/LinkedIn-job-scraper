from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint
from json import dumps
from time import sleep
import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', host = 'localhost', port = '3306', password = '1234', database='task2db')
    cursor = cnx.cursor()
except Exception as e:
    print(e)
    print("Database error")

# creates instance of Chrome WebDriver
driver = webdriver.Chrome()

# .get navigates to webpage
driver.get("https://www.mymajors.com/career-list/")

# A list of career types
careerTypes = driver.find_elements(By.CLASS_NAME, "hasChildMenu")


for career in careerTypes[:-1]:

    cursor.execute(f'insert into careers (career) VALUES ("{career.text}")')

    career.click()

    # curate list of all jobs within a career into a list variable called jobs
    jobList = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/a")

    id = cursor.lastrowid
    jobs = []
    for job in jobList:
        jobs.append((f'{job.text}', id))

    cursor.executemany('insert into subcareers (subcareer, career_id) VALUES (%s, %s)', jobs)

cnx.commit()

driver.close()