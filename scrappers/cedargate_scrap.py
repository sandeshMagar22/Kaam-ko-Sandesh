from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://workforcenow.adp.com/mascsr/default/mdf/recruitment/recruitment.html?cid=00938235-a9f7-41c8-88da-16d4f27e21c1&ccId=9200975014487_2&lang=en_US"

def scrape_cedargate_nepal():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)

    wait = WebDriverWait(driver, 15)

    jobs = []

    try:
        # ✅ Wait for job cards (not container)
        job_cards = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".current-openings-item")
            )
        )

        for job in job_cards:
            try:
                # ✅ Title (custom tag)
                title_element = job.find_element(By.CSS_SELECTOR, "sdf-link")
                title = title_element.text.strip()

                # ❗ No real href (it's "#")
                apply_link = URL   # fallback

                # ✅ Location
                location = job.find_element(
                    By.CSS_SELECTOR, ".current-opening-location-item span"
                ).text.strip()

                # Filter Nepal
                if "NP" in location or "Nepal" in location:

                    jobs.append((
                        "Cedargate",
                        title,
                        location,
                        apply_link,
                        "cedargate"
                    ))

            except Exception as e:
                print("Item error:", e)
                continue

    finally:
        driver.quit()

    return jobs