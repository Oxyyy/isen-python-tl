import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


@pytest.mark.selenium
def test_dark_mode_toggle():
    # Setup
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ne pas ouvrir de fenêtre graphique
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("http://localhost:8000/")  # Remplace avec l'URL de test locale

        # Assure-toi que le body n’a pas la classe dark-mode
        body = driver.find_element(By.TAG_NAME, "body")
        assert "dark-mode" not in body.get_attribute("class")

        # Clique sur le bouton Dark Mode
        toggle = driver.find_element(By.ID, "darkModeToggle")
        toggle.click()

        # Attends un peu pour laisser le JS s'exécuter
        time.sleep(1)

        # Vérifie que la classe 'dark-mode' est maintenant présente
        body = driver.find_element(By.TAG_NAME, "body")
        assert "dark-mode" in body.get_attribute("class")

    finally:
        driver.quit()
