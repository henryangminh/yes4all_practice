from selenium.webdriver.common.by import By
from app.util import check_if_element_exist

def get_product_detail(driver, url):
    driver.get(url)

    alt_image = driver.find_element(By.XPATH, ' \
        //div[@id="imageBlock"] \
        /div[@class="a-fixed-left-grid"] \
        /div[@class="a-fixed-left-grid-inner"] \
        /div[contains(@class, "a-text-center")] \
        /div[contains(@class, "a-row")] \
        /div[@id="main-image-container"] \
        /ul \
        /li \
        /span \
        /span \
        /div[@id="imgTagWrapperId"] \
        /img \
    ')

    img_url = alt_image.get_attribute('src')

    product_name = alt_image.get_attribute('alt')

    price = driver.find_element(By.XPATH, ' \
        //div[@id="corePriceDisplay_desktop_feature_div"] \
        /div[contains(@class, "a-spacing-none")] \
        /span[contains(@class, "a-price")] \
        /span \
    ').get_attribute('innerHTML')

    list_price_xpath = ' \
        //div[@id="corePriceDisplay_desktop_feature_div"] \
        /div[contains(@class, "a-spacing-small")] \
        /span \
        /span[contains(@class, "a-color-secondary")] \
        /span \
        /span[contains(@class, "a-offscreen")] \
    '

    if check_if_element_exist(driver, By.XPATH, list_price_xpath):
        list_price = driver.find_element(By.XPATH, list_price_xpath).get_attribute('innerHTML')
    else:
        list_price = ''

    rating = driver.find_element(By.XPATH, ' \
        //div[@id="averageCustomerReviews"] \
        /span[@data-action="acrStarsLink-click-metrics"] \
        /span \
    ').get_attribute('title')

    rating_count = driver.find_element(By.XPATH, ' \
        //span[@id="acrCustomerReviewText"] \
    ').get_attribute('innerHTML')

    product_detail_obj = {
        'title': product_name,
        'new_price': price,
        'list_price': list_price,
        'rating': rating,
        'rating_count': rating_count,
        'main_image_url': img_url
    }

    return product_detail_obj

def get_product_detail_by_list(driver, list_product):
    products = []
    for product in list_product:
        url = f"https://www.amazon.com/dp/{product}"
        products.append(get_product_detail(driver, url))

    return products
