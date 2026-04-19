# main.py

from scrappers.cedargate_scrap import scrape_cedargate_nepal
from scrappers.esewa_scrap import scrape_esewa
from scrappers.extensodata_scrap import scrape_extensodata
from scrappers.f1soft_scrap import scrape_f1soft
from scrappers.fusemachine_scrap import scrape_fusemachines
from scrappers.IMEkhaltidb_scrap import scrape_khalti
from scrappers.leapfrog_scrap import scrape_lftechnology 
from scrappers.verisk_scrap import scrape_verisk

from utils.load import load_to_mysql


def run_pipeline():

    all_jobs = []

    # 🔹 Run each scraper
    try:
        all_jobs.extend(scrape_cedargate_nepal())
        print("Cedargate done")
    except Exception as e:
        print("Cedargate error:", e)

    try:
        all_jobs.extend(scrape_esewa())
        print("Esewa done")
    except Exception as e:
        print("Esewa error:", e)

    try:
        all_jobs.extend(scrape_extensodata())
        print("Extenso done")
    except Exception as e:
        print("Extenso error:", e)

    try:
        all_jobs.extend(scrape_f1soft())
        print("F1Soft done")
    except Exception as e:
        print("F1Soft error:", e)

    try:
        all_jobs.extend(scrape_fusemachines())
        print("Fusemachines done")
    except Exception as e:
        print("Fusemachines error:", e)

    try:
        all_jobs.extend(scrape_khalti())
        print("Khalti done")
    except Exception as e:
        print("Khalti error:", e)

    try:
        all_jobs.extend(scrape_lftechnology())
        print("Leapfrog done")
    except Exception as e:
        print("Leapfrog error:", e)

    try:
        all_jobs.extend(scrape_verisk())
        print("Verisk done")
    except Exception as e:
        print("Verisk error:", e)

    # 🔥 Final result
    print(f"\nTotal jobs collected: {len(all_jobs)}\n")

    # 🔹 Load to DB
    load_to_mysql(all_jobs)


if __name__ == "__main__":
    run_pipeline()