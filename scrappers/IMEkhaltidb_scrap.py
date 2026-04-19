from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://blog.khalti.com/careers/"

def scrape_khalti():

    driver = webdriver.Chrome()
    driver.get(URL)

    wait = WebDriverWait(driver, 10)

    jobs = []

    try:
        # 🎯 Target ONLY job links
        job_links = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div.et_pb_section_3 li a")
            )
        )

        for link_element in job_links:

            title = link_element.text.strip()
            link = link_element.get_attribute("href")

            if title:
                jobs.append((
                    "Khalti",
                    title,
                    "Not specified",
                    link,
                    "khalti"
                ))

    finally:
        driver.quit()

    return jobs