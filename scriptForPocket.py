from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import base64
import time

import requests
from bs4 import BeautifulSoup
from types import SimpleNamespace

# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome('C:\\POKEMONI\\chromedriver.exe')

# Create ChromeOptions object
# options = webdriver.ChromeOptions()
#
# # Add options (e.g., headless mode, disable notifications)
# options.add_argument('--headless=new')  # Run Chrome in headless mode (without opening a window)
# # options.add_argument('--disable-notifications')  # Disable browser notifications
#
# # Path to your Chromedriver executable
chromedriver_path = 'C:\\POKEMONI\\chromedriver.exe'
#
# # Create Chrome WebDriver with the specified options
# driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=options)


options = webdriver.ChromeOptions()
options.add_argument("enable-automation")
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--dns-prefetch-disable")
options.add_argument("--disable-gpu")
options.add_argument('--headless=new')

driver = webdriver.Chrome(options=options, executable_path=chromedriver_path)

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
# 'kindnapping stella',
# 'emily the criminal',
# 'yara',
# 'rebel ridge',
# 'uglies',
# 'mirage',
# 'Nerve',
# 'Ferrari (2023)',
# 'Hypnotic',
# 'Molly\'s Game',
#  'Rush'

    # 'alias grace'
    # 'paranoid',
    # 'Almost Human'

    # 'paranoid',
    # 'paranoid',
    # 'paranoid',
    # 'paranoid',
    # 'paranoid',

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
    """
    Search for each item in list_of_items_to_search on Google, click the first IMDb link,
    and store the URLs of the visited pages.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        list_of_items_to_search (list): List of search terms to query on Google.

    Returns:
        list: List of URLs corresponding to IMDb pages of each search item.
    """
    base_url_search = 'https://www.google.com/'
    list_of_urls.clear()
    # imdb_urls = []

    def perform_google_search(search_term):
        """Perform a Google search for the given search term."""
        # Use the current page search field instead of reloading Google
        try:
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            search_box.clear()  # Clear the input box
            search_box.send_keys(search_term + " imdb")
            search_box.send_keys(Keys.ENTER)

        except Exception as e:
            print(f"Error with search box interaction: {e}")

    def get_first_result_url():
        """Retrieve the URL of the first result link without opening a new tab."""
        try:
            first_result_link = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.g a'))
            )
            return first_result_link.get_attribute("href")  # Get the link's URL

        except Exception as e:
            print(f"Error retrieving first result: {e}")
            return None

    # Start Google search and reuse the same session for subsequent queries
    driver.get(base_url_search)

    for search_item in list_of_items_to_search:
        print(f"Searching for: {search_item}")

        try:
            # Perform search and handle results
            perform_google_search(search_item)
            imdb_url = get_first_result_url()

            if imdb_url:
                list_of_urls.append(imdb_url)

        except Exception as e:
            print(f"Error occurred while searching for '{search_item}': {e}")
            continue

    print(list_of_urls)
    return list_of_urls


# OLD VERSION
# def search_for_words():
#     url = 'https://www.google.com/'
#     list_of_urls.clear()
#
#     for item_to_search in list_of_items_to_search:
#         driver.get(url)
#         print(item_to_search)
#         # identify search box
#         search_field = driver.find_element_by_name("q")
#         # enter search text
#         search_field.send_keys(item_to_search + " imdb")
#         # time.sleep(0.2)
#         # perform Google search with Keys.ENTER
#         search_field.send_keys(Keys.ENTER)
#
#         # time.sleep(0.5)
#         # Wait for search results to load and find the first search result link
#         first_result_link = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, 'div.g a'))
#             # EC.presence_of_element_located((By.TAG_NAME, 'h3'))
#         )
#
#         # Click on the first search result link
#         # first_result_link.click()
#         driver.execute_script("arguments[0].target='_blank'; arguments[0].click();", first_result_link)
#
#         # Switch to the new tab
#         driver.switch_to.window(driver.window_handles[1])
#
#
#         # ss = WebDriverWait(driver, 10).until(
#         #     EC.presence_of_element_located((By.CLASS_NAME, 'ipc-icon-button'))
#         #     # EC.presence_of_element_located((By.TAG_NAME, 'h3'))
#         # )
#         #
#         # ss.click()
#
#         # Get the current URL and append it to the list
#         list_of_urls.append(driver.current_url)
#
#         # Close the tab to return to the search results
#         driver.close()
#
#         # Switch back to the main tab
#         driver.switch_to.window(driver.window_handles[0])
#
#         # time.sleep(5)
#         # print('usao2')
#         # print(driver.current_url)
#         #
#         # list_of_urls.append(driver.current_url)
#
#     print(list_of_urls)

# OLD VERSION
# def process_data():
#     try:
#         for url in list_of_urls:
#             driver.get(url)
#             time.sleep(3)
#             print(url)
#             root_element_html = driver.page_source
#             print(root_element_html)
#
#             header = driver.find_element(By.XPATH,
#                                          '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1')
#             rating = driver.find_element(By.XPATH,
#                                          '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/span/div/div[2]/div[1]/span[1]')
#             tags = driver.find_element(By.XPATH,
#                                        '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/div[1]/div[2]')
#             text_below_header = driver.find_element(By.XPATH,
#                                                     '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/ul')
#             try:
#                 image = driver.find_element(By.XPATH,
#                                             '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div/div[1]/div/a/div')
#             except Exception:
#                 image = driver.find_element(By.XPATH,
#                                             '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div/div/a/div')
#
#             append_content_into_file(header, rating, tags, text_below_header)
#
#             image_as_bytes = str.encode(image.screenshot_as_base64)
#             appendix_for_image = header.text.replace(' ', '_').replace(':', '_')
#             url_for_image = base_url + '\\' + appendix_for_image + '.png'
#             print('url_for_image', url_for_image)
#
#             with open(url_for_image, "wb") as fh:
#                 fh.write(base64.decodebytes(image_as_bytes))
#             fh.close()
#
#     except Exception as exp:
#         print(exp)
#
#     finally:
#         driver.close()
#
#     print('kraj')


def process_data():
    # Custom headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    }
    try:
        for url in list_of_urls:
            # Send the GET request
            # The URL you want to scrape
            # url = 'https://www.imdb.com/title/tt1034007/'
            response = requests.get(url, headers=headers)

            # Check the status code
            if response.status_code == 200:
                # Parse the HTML content with BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')

                # find the header container
                # header_container = soup.find(class_=["sc-6291ae6f-0", "hYghoe"])
                # Find the <h1> tag
                header_container_h1_tag = soup.find('h1', {'data-testid': 'hero__pageTitle'})

                # Get the parent of the <h1> tag
                header_container = header_container_h1_tag.parent

                # Extracting the title
                title_tag = header_container.find('span', {'data-testid': 'hero__primary-text'})
                title_text = title_tag.get_text(strip=True) if title_tag else 'Title not found'
                # print(title_text)

                # Extracting the type (e.g., TV Mini Series)
                type_tag = header_container.find('ul', class_='ipc-inline-list').find_all('li')[0]
                type_text = type_tag.get_text(strip=True) if type_tag else 'Type not found'
                # print(type_text)

                # Extracting the year
                year_tag = header_container.find('ul', class_='ipc-inline-list').find_all('li')[1].find('a')
                year_text = year_tag.get_text(strip=True) if year_tag else 'Year not found'
                # print(year_text)
                # find the header container

                # Find the rating
                rating_container = soup.find(attrs={"data-testid": "hero-rating-bar__aggregate-rating__score"})

                rating_tag = rating_container.find('span', class_='sc-eb51e184-1 ljxVSS')
                rating_text = rating_tag.get_text(strip=True) if rating_tag else 'Rating not found'
                # print(rating_text)
                # Find the rating

                # Find the genres
                genres_container = soup.find(attrs={"data-testid": "interests"})

                genre_tags = genres_container.find_all('span', class_='ipc-chip__text')
                genres = [tag.get_text(strip=True) for tag in genre_tags]
                genres_text = ", ".join(genres)
                # print(genres_text)
                # Find the genres

                append_content_into_file(SimpleNamespace(text=title_text), SimpleNamespace(text=rating_text), SimpleNamespace(text=genres_text), SimpleNamespace(text=type_text + "\n" + year_text))

                # Find the image
                image_tag = soup.find(class_=["ipc-image"])
                # image_tag = image_container.find('img')
                image_src = image_tag['src']

                img_data = requests.get(image_src).content
                appendix_for_image = title_text.replace(' ', '_').replace(':', '_')
                url_for_image = base_url + '\\' + appendix_for_image + '.png'
                # print('url_for_image', url_for_image)
                with open(url_for_image, 'wb') as fh:
                    fh.write(img_data)
                fh.close()
                # Find the image

                # Remove <style> tags (CSS)
                # for style in soup.find_all('style'):
                #     style.decompose()  # Remove the <style> tag from the HTML
                #
                # # Remove <link> tags that reference CSS
                # for link in soup.find_all('link', {'rel': 'stylesheet'}):
                #     link.decompose()
                #
                # # Remove <script> tags (JavaScript)
                # for script in soup.find_all('script'):
                #     script.decompose()
                #
                # # Get the pure HTML content without CSS and JavaScript
                # pure_html = str(soup)
                #
                # # Output or save the cleaned HTML
                # print(pure_html)
            else:
                print(f"Failed to retrieve the page. Status code: {response.status_code}")
    except Exception as exp:
        print(exp)

    print("kraj")


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
