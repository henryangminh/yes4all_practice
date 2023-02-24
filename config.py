from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.best_seller.best_seller import get_best_seller_by_list
from app.product_detail.product_detail import get_product_detail_by_list
from app.product_wayfair.product_wayfair import get_product_in_pages
import json

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver.exe")


# # Get best seller in amazon
best_seller_by_list = get_best_seller_by_list(driver, ['16225007011', '172456', '193870011'])
print(best_seller_by_list)


# # Get product detail in amazon
products = get_product_detail_by_list(driver, ['B07MFZXR1B', 'B07CRG7BBH', 'B07VS8QCXC'])
print(products)

# Get product detail in wayfair
products_wayfair = get_product_in_pages(driver)
# products_wayfair_json = json.dumps(products_wayfair, indent=4)
# with open("/result/products_wayfair.json", "w") as outfile:
#     outfile.write(products_wayfair_json)
print(products)