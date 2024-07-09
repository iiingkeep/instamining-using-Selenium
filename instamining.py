from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

load_dotenv()
INSTA_ID = os.environ.get('INSTA_ID')
INSTA_PW = os.environ.get('INSTA_PW')

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
service = webdriver.ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(options=options, service=service)

browser.get("https://www.instagram.com/accounts/login/")

main_hashtag = 'dog'
#browser.get(f"https://www.instagram.com/explore/tags/{main_hashtag}")

WebDriverWait(browser,3).until(EC.presence_of_element_located((By.CLASS_NAME, "_ab3b")))

id_input = browser.find_element(By.NAME, 'username')
pw_input = browser.find_element(By.NAME, 'password')

id_input.send_keys(INSTA_ID)
pw_input.send_keys(INSTA_PW)
pw_input.send_keys(Keys.ENTER)
time.sleep(1)

