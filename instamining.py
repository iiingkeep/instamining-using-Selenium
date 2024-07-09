from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
service = webdriver.ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(options=options, service=service)

main_hashtag = 'dog'
browser.get(f"https://www.instagram.com/explore/tags/{main_hashtag}")
time.sleep(3)
