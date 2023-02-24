import app.const as const
from app.util import scroll_page, check_if_element_exist
from selenium.webdriver.common.by import By

def get_best_seller_in_page(driver):
    scroll_page(driver)

    if not check_if_element_exist(driver, By.CLASS_NAME, 'p13n-gridRow'):
        return []

    products = driver.find_element(By.CLASS_NAME, 'p13n-gridRow').find_elements(By.ID, 'gridItemRoot')

    list_products = []

    for product in products:
        rank_no = product.find_element(By.CSS_SELECTOR, "[id^='p13n-asin-index-']") \
            .find_element(By.CLASS_NAME, 'zg-bdg-ctr') \
            .find_element(By.CLASS_NAME, 'zg-bdg-body') \
            .find_element(By.CLASS_NAME, 'zg-bdg-text')\
            .text

        product_name = product.find_element(By.CSS_SELECTOR, "[id^='p13n-asin-index-']") \
            .find_element(By.XPATH, 
                './div[@class="zg-grid-general-faceout"] \
                /div[@class="p13n-sc-uncoverable-faceout"] \
                /a[@class="a-link-normal"] \
                /span'
            ).text
        
        price = product.find_element(By.CSS_SELECTOR, "[id^='p13n-asin-index-']") \
            .find_element(By.XPATH, 
                './div[@class="zg-grid-general-faceout"] \
                /div[@class="p13n-sc-uncoverable-faceout"] \
                /div[@class="a-row"][position()=2] \
                '
            ).text
        
        product_url = product.find_element(By.CSS_SELECTOR, "[id^='p13n-asin-index-']") \
            .find_element(By.XPATH, 
                './div[@class="zg-grid-general-faceout"] \
                /div[@class="p13n-sc-uncoverable-faceout"] \
                /a[@class="a-link-normal"]\
                '
            ).get_attribute('href')

        product_obj = {
            'rank': rank_no,
            'product_name': product_name,
            'price': price,
            'product_url': product_url
        }

        list_products.append(product_obj)

    return list_products

def get_best_seller_in_pages(driver, category):

    list_products = []

    url = f"https://www.amazon.com/gp/bestsellers/hi/{category}"

    while True:
        driver.get(url)
        list_products.append(get_best_seller_in_page(driver))

        if check_if_element_exist(driver, By.XPATH, '//li[@class="a-last"]/a'):
            url = driver.find_element(By.XPATH, '//li[@class="a-last"]/a').get_attribute('href')
        else:
            return list_products

def get_best_seller_by_list(driver, list_category):
    best_seller_by_category = []

    for category in list_category:
        best_seller_by_category.append(get_best_seller_in_pages(driver, category))

    return best_seller_by_category
