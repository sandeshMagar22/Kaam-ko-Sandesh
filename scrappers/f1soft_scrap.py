# scrappers/f1soft_scrap.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://career.f1soft.com/jobs"


def scrape_f1soft():

    driver = webdriver.Chrome()
    driver.get(URL)

    wait = WebDriverWait(driver, 10)

    jobs_data = []

    try:
        # 🔁 Click "Load More" until it disappears
        while True:
            try:
                load_more = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.tf-button.style-1"))
                )
                driver.execute_script("arguments[0].click();", load_more)

                # small wait for new jobs to load
                wait.until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.features-job"))
                )

            except:
                break  # no more button

        # ✅ Now scrape all jobs
        jobs = driver.find_elements(By.CSS_SELECTOR, "div.features-job")

        for job in jobs:
            try:
                title_element = job.find_element(By.CSS_SELECTOR, "h3 a")

                title = title_element.text.strip()
                link = title_element.get_attribute("href")

                location = job.find_element(
                    By.CSS_SELECTOR, ".location-div span.small"
                ).text.strip()

                jobs_data.append((
                    "F1Soft",
                    title,
                    location,
                    link,
                    "f1soft"   # source
                ))

            except Exception as e:
                print("Item error:", e)
                continue

    finally:
        driver.quit()

    return jobs_data