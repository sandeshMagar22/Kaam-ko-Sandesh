from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://extensodata.com/career"


def scrape_extensodata():

    driver = webdriver.Chrome()
    driver.get(URL)

    wait = WebDriverWait(driver, 10)

    jobs = []

    try:
        job_cards = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "col-sm-4"))
        )

        for job in job_cards:
            try:
                title = job.find_element(By.TAG_NAME, "h3").text.strip()
                link = job.find_element(By.TAG_NAME, "a").get_attribute("href")

                # Some cards may not be jobs → filter
                if not title:
                    continue

                jobs.append((
                    "Extenso Data",
                    title,
                    "Not specified",
                    link,
                    "extensodata"   # source
                ))

            except Exception as e:
                print("Item error:", e)
                continue

    finally:
        driver.quit()

    return jobs