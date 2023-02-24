from time import sleep
from selenium.webdriver.common.by import By

def scroll_page(driver):
    total_page_height = driver.execute_script("return document.body.scrollHeight")
    browser_window_height = driver.get_window_size(windowHandle='current')['height']
    current_position = driver.execute_script('return window.pageYOffset')
    while (current_position + browser_window_height) < total_page_height:
        driver.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
        current_position = driver.execute_script('return window.pageYOffset')
        total_page_height = driver.execute_script("return document.body.scrollHeight")
        sleep(2)

def check_if_element_exist(element, by, name):
    try:
        element.find_element(by, name)
        return True
    except:
        return False