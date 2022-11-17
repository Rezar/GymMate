import traceback

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException


def get_selenium_driver():
    options = webdriver.ChromeOptions()
    options.headless = True
    try:
        driver = webdriver.Chrome(executable_path="tools\\chromedriver.exe", options=options)
        return driver
    except Exception:
        traceback.print_exc()
        print("Chrome Driver missing")
        return None
