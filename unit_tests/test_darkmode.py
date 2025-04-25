from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_dark_mode_toggle():
    # Options pour le mode headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Supposons que chromedriver est dans le PATH
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("http://localhost:8080/") 

        # Clique sur le bouton dark mode (exemple)
        toggle_button = driver.find_element("id", "dark-mode-toggle")
        toggle_button.click()

        time.sleep(1)

        # Vérifie si la classe dark-mode est appliquée
        body = driver.find_element("tag name", "body")
        assert "dark-mode" in body.get_attribute("class")

    finally:
        driver.quit()
