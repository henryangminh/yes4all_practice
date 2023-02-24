#//main//div[@data-hb-id='Grid']
from app.util import scroll_page, check_if_element_exist
from selenium.webdriver.common.by import By

def get_product_in_page(driver):
    scroll_page(driver)

    products = driver \
        .find_elements(By.XPATH, '//main//div[@data-hb-id="Grid"]/div[@data-hb-id="Grid.Item"]') \
    
    products = products[:len(products)-3]

    products_in_one_page = []
    for product in products:
        product_name = product.find_element(By.XPATH, './/span[@data-hb-id="BoxV2"]').get_attribute('innerHTML')
        brand = product.find_element(By.XPATH, './/p[@class="_1vgix4w0_6101 _1vgix4w2_6101 _1vgix4w6_6101"]').text
        price = product.find_element(By.XPATH, './/div[@data-enzyme-id="pricesSpacing"]/div/div/span').get_attribute('innerHTML')
        if price == 'From':
            price = product.find_element(By.XPATH, './/div[@data-enzyme-id="pricesSpacing"]/div/div/span[position()=2]').get_attribute('innerHTML')

        list_price_xpath = './/div[@data-enzyme-id="pricesSpacing"]/div/div/s'
        list_price = ''
        if check_if_element_exist(product, By.XPATH, list_price_xpath):
            list_price = product.find_element(By.XPATH, list_price_xpath).text

        rating = ''
        rating_count = ''
        review_xpath = './/div[@data-enzyme-id="reviewsSpacing"]/div/p'

        if check_if_element_exist(product, By.XPATH, review_xpath):
            review = product.find_element(By.XPATH, review_xpath).text
            rating = review.split('.')[0]
            rating_count = review.split('.')[1].split(' ')[0]

        shipping_xpath = './/div[@data-enzyme-id="shippingSpacing"]/div/p'
        if check_if_element_exist(product, By.XPATH, shipping_xpath):
            shipping = product.find_element(By.XPATH, shipping_xpath).text

        sponsored_xpath = './/div[@data-hb-id="Box"]/div[@class="kzv0b81eu_6101 kzv0b81yc_6101"]/div'
        sponsored = False
        if check_if_element_exist(product, By.XPATH, sponsored_xpath):
            sponsored = product.find_element(By.XPATH, sponsored_xpath).text
            if sponsored == 'Sponsored':
                sponsored = True


        # review = product.find_element(By.XPATH, './/div[@data-enzyme-id="reviewsSpacing"]/div/p').text
        # print(f"{rating} {rating_count}")

        product_detail_obj = {
            'title': product_name,
            'brand': brand,
            'new_price': price,
            'list_price': list_price,
            'rating': rating,
            'rating_count': rating_count,
            'shipping_fee': shipping,
            'sponsored': sponsored
        }

        products_in_one_page.append(product_detail_obj)

    # print(len(products_in_one_page))
    return products_in_one_page

    # print(len(products))

# //div[@data-enzyme-id="reviewsSpacing"]/div/p

def get_product_in_pages(driver):
    url = 'https://www.wayfair.com/furniture/sb0/sectionals-c413893.html'
    products = []
    
    while True:
        driver.get(url)
        products.extend(get_product_in_page(driver))

        # //main//nav//a[@data-enzyme-id="paginationNextPageLink"]

        next_page_xpath = '//main//nav//a[@data-enzyme-id="paginationNextPageLink"]'
        if check_if_element_exist(driver, By.XPATH, next_page_xpath):
            url = driver.find_element(By.XPATH, next_page_xpath).get_attribute('href')
        else:
            return products

        # print(len(products))
        if len(products) >= 300:
            return products[0:300]

    return products
    