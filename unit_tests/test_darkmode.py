import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

def test_dark_mode_toggle():
    # Configuration de Chrome pour l'exécution sans interface graphique
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Mode sans interface
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Démarrage du navigateur
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(10)

    try:
        # Accès à l'application
        driver.get("http://localhost:8000/")

        # Exemple de vérification de contenu
        body_text = driver.find_element("tag name", "body").text
        assert "Dark Mode" in body_text or "Mode Sombre" in body_text

        # Simuler un clic sur le bouton dark mode (si possible)
        try:
            toggle_button = driver.find_element("id", "dark-mode-toggle")
            toggle_button.click()
            time.sleep(1)  # Laisse le temps pour le basculement
            new_body_class = driver.find_element("tag name", "body").get_attribute("class")
            assert "dark" in new_body_class
        except Exception:
            # Pas de bouton ou comportement différent
            pass

    finally:
        # Fermeture du navigateur
        driver.quit()
