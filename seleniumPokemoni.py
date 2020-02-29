from selenium import webdriver
from urllib.request import urlretrieve

import urllib.request
from pokemon import Pokemon

import requests
import json

print("ispis")

options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome('C:\\POKEMONI\\chromedriver.exe')
driver.get('https://gamepress.gg/pokemongo/pokemon-list')

tableBody = driver.find_elements_by_id('pokemon-list')
listOfRows = driver.find_elements_by_class_name('pokemon-row')
counter = 0
listOfLinks = []
listOfPokemons = []
for oneRowElement in listOfRows:
    pokemonName = oneRowElement.get_attribute('data-name')
    tds = oneRowElement.find_elements_by_tag_name('td')
    hp = tds[3].text
    atk = tds[4].text
    defense = tds[5].text
    cp = tds[9].text
    pokemonRating = tds[10].text
    res = pokemonRating.find("-")
    if res >= 0:
        pokemonRating = 0

    links = tds[1].find_elements_by_tag_name('a')
    for link in links:
        linkToGo = link.get_attribute("href")
        imageName = "D:/slikePokemoni/" + pokemonName + ".png"

        linkObject = {}
        linkObject["name"] = imageName
        linkObject["link"] = linkToGo
        listOfLinks.append(linkObject)
        pokemonObject = Pokemon(pokemonName, hp, atk, defense, cp, pokemonRating, imageName)
        listOfPokemons.append(pokemonObject)
        print(linkToGo)

        # images = link.find_elements_by_tag_name("img")
        # for one_image in images:
        #     pokemonImagePath = one_image.get_attribute('src')
        #     #print(pokemonImagePath)
        #     imageName = "D:/slikePokemoni/" + pokemonName + ".png"
        #     # try:
        #     opener = urllib.request.URLopener()
        #     opener.addheader('User-Agent', 'stefan')
        #     filename, headers = opener.retrieve(pokemonImagePath, imageName)

        break

    counter += 1

#kod za testiranje da ne radi na velikom skupu
    # if counter == 5:
    #     break


#     imageName = playersNameLabel.replace(" ","_")
#     imageName = "football/" + imageName + ".png"
#     image = ahref.find_element_by_xpath(".//div[@class='klzc']//img")
#     src = image.get_attribute('src')
#     urlretrieve(src, imageName)
#     print(image.get_attribute("class"))


#print(listOfLinks)
# for one_pokemon in listOfPokemons:
#     print(one_pokemon)
json_string = json.dumps([ob.__dict__ for ob in listOfPokemons])

#pozovi endpoint na java backu
resp = requests.post('http://localhost:8081/api/pokemon/all/string', json=json_string)
if resp.status_code != 200:
    # This means something went wrong.
    print('los')
else:
    print("uspeo")

#kod za skidanje slika kad skinem sve slike mogu ga zakomentarisati
# for linkObject in listOfLinks:
#     driver.get(linkObject["link"])
#
#     highImages = driver.find_elements_by_id('tab-1-img')
#     for highImage in highImages:
#         images = highImage.find_elements_by_tag_name("img")
#         for image in images:
#             src = image.get_attribute('src')
#             imageName = linkObject["name"]
#             opener = urllib.request.URLopener()
#             opener.addheader('User-Agent', 'stefan')
#             filename, headers = opener.retrieve(src, imageName)
print("zavrsio")