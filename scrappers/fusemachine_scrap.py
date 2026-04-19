# scrappers/fusemachine_scrap.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://fusemachines.com/company/careers/"


def scrape_fusemachines():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)

    wait = WebDriverWait(driver, 10)

    jobs = []

    try:
        job_cards = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "#jazzhr .row.py-3")
            )
        )

        for job in job_cards:
            try:
                title = job.find_element(By.CSS_SELECTOR, ".bold-s").text.strip()

                location = job.find_element(
                    By.CSS_SELECTOR, ".c-dark-grey"
                ).text.strip()

                apply_link = job.find_element(
                    By.CSS_SELECTOR, ".col-md-2 a"
                ).get_attribute("href")

                jobs.append((
                    "Fusemachines",
                    title,
                    location,
                    apply_link,
                    "fusemachines"   # source
                ))

            except Exception as e:
                print("Item error:", e)
                continue

    finally:
        driver.quit()

    return jobs