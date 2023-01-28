from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import base64
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:\\POKEMONI\\chromedriver.exe')

base_url = 'C:\\Users\\stefan\\Desktop\\slikeForPocket'
list_of_urls = [
    # films
    # 'https://www.imdb.com/title/tt1205537/?ref_=nv_sr_srsg_0',
    # 'https://www.imdb.com/title/tt17491040/',
    # 'https://www.imdb.com/title/tt10230994/?ref_=nv_sr_srsg_0',
    # 'https://www.imdb.com/title/tt4943218/?ref_=nv_sr_srsg_0',
    # 'https://www.imdb.com/title/tt10515864/?ref_=nv_sr_srsg_0',
    # 'https://www.imdb.com/title/tt18563148/?ref_=nv_sr_srsg_0',
    # 'https://www.imdb.com/title/tt13822738/?ref_=nv_sr_srsg_0',
    # 'https://www.imdb.com/title/tt14158554/?ref_=nv_sr_srsg_0',
    # 'https://www.imdb.com/title/tt7395114/?ref_=nv_sr_srsg_0',
    # 'https://www.imdb.com/title/tt14174940/?ref_=nv_sr_srsg_0',

    # limited series
    # 'https://www.imdb.com/title/tt5839454/?ref_=nv_sr_srsg_0',
    # 'https://www.imdb.com/title/tt1034007/?ref_=nv_sr_srsg_0'

    # normal series same as films
    # 'https://www.imdb.com/title/tt2193021/'
]
list_of_items_to_search = [
    # 'alias grace',
    # 'paranoid',
    # 'Almost Human'

    # 'paranoid',
    # 'paranoid',
    # 'paranoid',
    # 'paranoid',
    # 'paranoid',
]


def append_content_into_file(header, rating, tags, text_below_header):
    print('header ', header.text)
    print('rating ', rating.text)
    print('tags ', tags.text.replace('\n', ', '))
    print('textBelowHeader ', text_below_header.text)

    # Open a file with access mode 'a'
    file_object = open(base_url + '\\' + 'downloadedData.txt', 'a')
    # Append 'hello' at the end of file
    file_object.write('\n')
    file_object.write(header.text + '\n')
    file_object.write(text_below_header.text + '\n')
    file_object.write(tags.text.replace('\n', ', ') + '\n')
    file_object.write(rating.text + '\n')
    file_object.write(
        '-----------------------------------------------------------------------------------------------------------'
        + '\n')
    # Close the file
    file_object.close()


def search_for_words():
    url = 'https://www.google.com/'
    list_of_urls.clear()

    for item_to_search in list_of_items_to_search:
        driver.get(url)
        # identify search box
        search_field = driver.find_element_by_name("q")
        # enter search text
        search_field.send_keys(item_to_search + " imdb")
        # time.sleep(0.2)
        # perform Google search with Keys.ENTER
        search_field.send_keys(Keys.ENTER)

        # time.sleep(0.5)
        result = driver.find_element_by_tag_name('h3')
        result.click()

        list_of_urls.append(driver.current_url)
    print(list_of_urls)

def process_data():
    try:

        for url in list_of_urls:
            driver.get(url)
            header = driver.find_element(By.XPATH,
                                         '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1')
            rating = driver.find_element(By.XPATH,
                                         '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]')
            tags = driver.find_element(By.XPATH,
                                       '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/div')
            text_below_header = driver.find_element(By.XPATH,
                                                    '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div')

            try:
                image = driver.find_element(By.XPATH,
                                            '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div/div[1]/div/a/div')
            except Exception:
                image = driver.find_element(By.XPATH,
                                            '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div/div/a/div')

            append_content_into_file(header, rating, tags, text_below_header)

            image_as_bytes = str.encode(image.screenshot_as_base64)
            appendix_for_image = header.text.replace(' ', '_').replace(':', '_')
            url_for_image = base_url + '\\' + appendix_for_image + '.png'
            print('url_for_image', url_for_image)

            with open(url_for_image, "wb") as fh:
                fh.write(base64.decodebytes(image_as_bytes))
            fh.close()

    except Exception as exp:
        print(exp)

    finally:
        driver.close()

    print('kraj')


def main():
    search_for_words()
    process_data()


if __name__ == "__main__":
    main()


# import webbrowser
#
# webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")

# # # MacOS
# # chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
#
# # Windows
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#
# # Linux
# # chrome_path = '/usr/bin/google-chrome %s'
#
# url = 'https://www.imdb.com/title/tt1205537/?ref_=nv_sr_srsg_0'
# webbrowser.get(chrome_path).open(url)
