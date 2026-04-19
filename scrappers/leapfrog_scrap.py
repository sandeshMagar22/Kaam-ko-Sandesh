# scrappers/leapfrog_scrap.py

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.lftechnology.com/careers#currentOpenings"


def scrape_lftechnology():

    driver = webdriver.Chrome()
    driver.get(URL)

    wait = WebDriverWait(driver, 10)

    jobs = []

    try:
        job_cards = wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "vaccancy__list")
            )
        )

        for job in job_cards:
            try:
                title = job.find_element(By.TAG_NAME, "h3").text.strip()

                location = job.find_element(
                    By.TAG_NAME, "p"
                ).text.strip()

                link = job.find_element(
                    By.TAG_NAME, "a"
                ).get_attribute("href")

                jobs.append((
                    "LF Technology",
                    title,
                    location,
                    link,
                    "lftechnology"   # source
                ))

            except Exception as e:
                print("Item error:", e)
                continue

    finally:
        driver.quit()

    return jobs