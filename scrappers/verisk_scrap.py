# scrappers/verisk_scrap.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://fa-ewmy-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/jobs?location=Nepal&locationId=300000000464166&locationLevel=country&mode=location"


def scrape_verisk():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)

    wait = WebDriverWait(driver, 10)

    jobs = []

    try:
        job_cards = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "li[data-qa='searchResultItem']")
            )
        )

        for job in job_cards:
            try:
                title = job.find_element(
                    By.CSS_SELECTOR, ".job-tile__title"
                ).text.strip()

                location = job.find_element(
                    By.CSS_SELECTOR,
                    ".job-list-item__job-info-item .job-list-item__job-info-value span"
                ).text.strip()

                apply_link = job.find_element(
                    By.CSS_SELECTOR,
                    "a.job-grid-item__link"
                ).get_attribute("href")

                jobs.append((
                    "Verisk",
                    title,
                    location,
                    apply_link,
                    "verisk"   # source
                ))

            except Exception as e:
                print("Item error:", e)
                continue

    finally:
        driver.quit()

    return jobs