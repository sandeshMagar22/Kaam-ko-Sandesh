# scrappers/esewa_scrap.py

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://career.esewa.com.np/jobs"


def scrape_esewa():

    driver = webdriver.Chrome()
    driver.get(URL)

    wait = WebDriverWait(driver, 10)

    jobs = []

    try:
        job_cards = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "jobs-item"))
        )

        for job in job_cards:
            try:
                # Title
                title = job.find_element(By.TAG_NAME, "h6").text.strip()

                # Location
                location = job.find_element(
                    By.CLASS_NAME, "jobs-location"
                ).text.strip()

                # Apply link
                link = job.find_element(
                    By.CLASS_NAME, "btn-apply-now"
                ).get_attribute("href")

                jobs.append((
                    "eSewa",
                    title,
                    location,
                    link,
                    "esewa"   # source
                ))

            except Exception as e:
                print("Item error:", e)
                continue

    finally:
        driver.quit()

    return jobs