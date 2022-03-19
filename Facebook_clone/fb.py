from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# => creat a file .py
chromeOption = webdriver.ChromeOptions()
pref = {
  #load img
  'profile.managed_default_content_setting_images' : 1
}
chromeOption.add.add_experimental_option('pref', pref)
driver = webdriver.Chrome('./chromedriver', Option = chromeOption)