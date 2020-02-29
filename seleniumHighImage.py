from selenium import webdriver
from urllib.request import urlretrieve
import urllib.request

print("ispis")

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:\\POKEMONI\\chromedriver.exe')
driver.get('https://gamepress.gg/pokemongo/pokemon/2')


highImages = driver.find_elements_by_id('tab-1-img')
for highImage in highImages:
    images = highImage.find_elements_by_tag_name("img")
    for image in images:
        src = image.get_attribute('src')
        imageName = "D:/probaSlike/" + "High" + ".png"
        opener = urllib.request.URLopener()
        opener.addheader('User-Agent', 'stefan')
        filename, headers = opener.retrieve(src, imageName)