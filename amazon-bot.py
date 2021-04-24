from selenium import webdriver
import time
from datetime import datetime
import json

browser = webdriver.Chrome()

# Amazon RTX 3070 Page
browser.get("https://www.amazon.com/dp/B08MT6B58K/ref=oos_itemTitle_0")

# browser.get("https://www.amazon.com/COMeap-Adapter-Corsair-Modular-24-inch/dp/B07CZBZN5R/ref=bmx_2?pd_rd_w=5fPZM&pf_rd_p=b56a886c-2bb4-4e74-b4cf-23d7a76693c8&pf_rd_r=8DV4J8B0DVT8K3MS6QZ6&pd_rd_r=503471ab-640c-4908-b632-5f7ce1bcc8e3&pd_rd_wg=hMP03&pd_rd_i=B07CZBZN5R&psc=1")

myCards = """[
    {
        "brand":"asus",
        "cartUrl": "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08L8LG4M3&Quantity.1=1",
        "model": "dual",
        "series": "3070",
        "url": "https://www.amazon.com/dp/B08L8LG4M3",
    },
    {
        "brand": "asus",
        "cartUrl": "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08L8HPKR6&Quantity.1=1",
        "model": "dual",
        "series": "3070",
        "url": "https://www.amazon.com/dp/B08L8HPKR6",
    },
    {
        "brand": "evga",
        "cartUrl": "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08LW46GH2&Quantity.1=1",
        "model": "xc3 black",
        "series": "3070",
        "url": "https://www.amazon.com/dp/B08LW46GH2",
    },
    {
        "brand": "asus",
        "cartUrl":
            "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08L8JNTXQ&Quantity.1=1",
        "model": "strix",
        "series": "3070",
        "url": "https://www.amazon.com/dp/B08L8JNTXQ",
    },
    {
        "brand": "asus",
        "cartUrl": "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08L8KC1J7&Quantity.1=1",
        "model": "tuf",
        "series": "3070",
        "url": "https://www.amazon.com/dp/B08L8KC1J7",
    },
    {
        "brand": "gigabyte",
        "cartUrl":
            "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08KY266MG&Quantity.1=1",
        "model": "gaming oc",
        "series": "3070",
        "url": "https://www.amazon.com/dp/B08KY266MG",
    },
    {
        "brand": "msi",
        "cartUrl": "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08KWN2LZG&Quantity.1=1",
        "model": "gaming",
        "series": "3070",
        "url": "https://www.amazon.com/dp/B08KWN2LZG",
    },
    {
        "brand": "pny",
        "cartUrl": "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08HBJB7YD&Quantity.1=1",
        "model": "xlr8 revel",
        "series": "3070",
        "url": "https://www.amazon.com/dp/B08HBJB7YD",
    },
    {
        "brand": "pny",
        "cartUrl": "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08HBF5L3K&Quantity.1=1",
        "model": "xlr8 uprising",
        "series": "3070",
        "url": "https://www.amazon.com/dp/B08HBF5L3K",
    },
    {
        "brand": "msi",
        "cartUrl": "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08KWPDXJZ&Quantity.1=1",
        "model": "ventus 2x oc",
        "series": "3070",
        "url": "https://www.amazon.com/dp/B08KWPDXJZ",
    },
    {
        "brand": "msi",
        "cartUrl": "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08KWLMZV4&Quantity.1=1",
        "model": "ventus 3x oc",
        "series": "3070",
        "url": "https://www.amazon.com/dp/B08KWLMZV4",
    },
    {
        "brand": "zotac",
        "cartUrl": "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08LF1CWT2&Quantity.1=1",
        "model": "twin edge oc",
        "series": "3070",
        "url": "https://www.amazon.com/dp/B08LF1CWT2",
    },
    {
        "brand": "zotac",
        "cartUrl": "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08LF32LJ6&Quantity.1=1",
        "model": "gaming",
        "series": "3070",
        "url": "https://www.amazon.com/dp/B08LF32LJ6",
    },
    {
        "brand": "evga",
        "cartUrl": "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08L8L71SM&Quantity.1=1",
        "model": "xc3 ultra",
        "series": "3070",
        "url": "https://www.amazon.com/dp/B08L8L71SM",
    },
]"""


priceButton = False

while not priceButton:

    try:
        # If this works when the button is not pytopen
        priceTag = browser.find_element_by_xpath('//*[@id="availability"]/span').text

        #Price is not ready
        if priceTag == "No disponible por el momento.":
            print("La tarjeta no está disponible:", priceTag)
        else:
            raise Exception("Tarjeta encontrada")

        time.sleep(1)
        browser.refresh()

    except:

        priceTag = browser.find_element_by_xpath('//*[@id="priceblock_saleprice"]')

        # Take a screenshot to see if the price is real
        botTime = datetime.now().strftime('%Y%m%d_%H%M%S')
        print(priceTag)
        print("Tomando captura de pantalla")
        browser.save_screenshot("captura_" + str(botTime) + ".png")
        priceButton = True
