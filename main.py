# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# brand_name = []
# model_name = []
# screen_size = []
# ram = []
# storage = []
# cpu_model = []
# operating_system = []
# price = []
# rating = []
# review_count = []
# graphics_card_description = []
#
# pages_number = 1
# url = 'https://www.amazon.in/s?k=laptops'
#
# for i in range(pages_number):
#     driver.get(url=url)
#     try:
#         next_button = driver.find_element(By.XPATH,
#                                           '//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator"]')
#         url = next_button.get_attribute("href")
#     except:
#         print("No next page found ! ! !")
#
#     laptop_links = driver.find_elements(By.XPATH,
#                                         '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
#
#     laptop_urls = []
#     for link in laptop_links:
#         laptop_urls.append(link.get_attribute("href"))
#     print(f'Number of laptops in a page: {len(laptop_urls)}\n')
#
#     for url in laptop_urls:
#         driver.get(url)
#         print('\n')
#         try:
#             laptop_brand = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
#                                                                                            '//tr [@class="a-spacing-small po-brand"] '
#                                                                                            '//td [@class="a-span9"]'  #TODO: Remove this part where its used and check if its work properly
#                                                                                            '//span [@class="a-size-base po-break-word"]'))).text
#
#         except:
#             laptop_brand = 'No brand name'
#         print(f'Brand: {laptop_brand}')
#         brand_name.append(laptop_brand)
#
#         try:
#             laptop_model = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
#                                                                                            '//tr [@class="a-spacing-small po-model_name"]'
#                                                                                            '//td [@class="a-span9"]'
#                                                                                            '//span [@class="a-size-base po-break-word"]'))).text
#
#         except:
#             laptop_model = 'No model'
#         print(f'Model: {laptop_model}')
#         model_name.append(laptop_model)
#
#         try:
#             laptop_screen = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
#                                                                                             '//tr [@class="a-spacing-small po-display.size"]'
#                                                                                             '//td [@class="a-span9"]'
#                                                                                             '//span [@class="a-size-base po-break-word"]'))).text
#
#         except:
#             laptop_screen = 'No screen size'
#         print(f'Screen size: {laptop_screen}')
#         screen_size.append(laptop_screen)
#
#
#         try:
#             laptop_ram = WebDriverWait(driver, 10).until(
#                 ec.presence_of_element_located((By.XPATH, '//tr/td[2]/span'))).text
#         except:
#             laptop_ram = "No RAM"
#         print(f'RAM: {laptop_ram}')
#         ram.append(laptop_ram)
#
#
#         try:
#             laptop_storage = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
#                                                                                              '//tr [@class="a-spacing-small po-hard_disk.size"]'
#                                                                                              '//td [@class="a-span9"]'
#                                                                                              '//span [@class="a-size-base po-break-word"]'))).text
#
#         except:
#             laptop_storage = 'No storage'
#         print(f'Storage: {laptop_storage}')
#         storage.append(laptop_storage)
#
#         try:
#             laptop_cpu = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
#                                                                                          '//tr [@class="a-spacing-small po-cpu_model.family"]'
#                                                                                          '//td [@class="a-span9"]'    #TODO: Remove this part where its used and check if its work properly
#                                                                                          '//span [@class="a-size-base po-break-word"]'))).text
#
#         except:
#             laptop_cpu = 'No CPU'
#         print(f'CPU: {laptop_cpu}')
#         cpu_model.append(laptop_cpu)
#
#         try:
#             laptop_system = WebDriverWait(driver, 15).until(
#                 ec.presence_of_element_located(
#                     (By.XPATH, '//tr[contains(@class, "po-operating_system")]'
#                                '/td[contains(@class, "a-span9")]'
#                                '/span[contains(@class, "po-break-word")]'))).text
#         except:
#             laptop_system = 'No operating system found'
#             print(f'Operating system: {laptop_system}')
#         operating_system.append(laptop_system)
#
#         try:
#             laptop_price = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
#                                                                                            '//span [@class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"]'
#                                                                                            '//span [@class="a-price-whole"]'))).text
#
#         except:
#             laptop_price = 'No price'
#         print(f'Price: {laptop_price}')
#         price.append(laptop_price)
#
#         try:
#             laptop_rating = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
#                                                                                             '//a [@class="a-popover-trigger a-declarative"]'
#                                                                                             '//span [@class="a-size-base a-color-base"]'))).text
#
#         except:
#             laptop_rating = 'No rating'
#         print(f'Rating: {laptop_rating}')
#         rating.append(laptop_rating)
#
#         try:
#             laptop_reviews = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
#                                                                                              '//a [@id="acrCustomerReviewLink"]'
#                                                                                              '//span [@id="acrCustomerReviewText"]'))).text
#
#         except:
#             laptop_reviews = 'No reviews'
#         print(f'Reviews: {laptop_reviews}')
#         review_count.append(laptop_reviews)
#
#         try:
#             laptop_gpu_element = WebDriverWait(driver, 10).until(
#                 ec.presence_of_element_located(
#                     (By.XPATH, "//tr[@class='a-spacing-small po-graphics_description']//td[@class='a-span9']//span")
#                 )
#             )
#
#             # Extract text using textContent
#             laptop_gpu = laptop_gpu_element.get_attribute("textContent").strip()
#             print(f"GPU Description: {laptop_gpu}")
#         except Exception as e:
#             print(f"Error: {e}")
#
#     driver.quit()
# # try:
# #     cpu = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
# #         (By.XPATH, "//tr[contains(@class, 'po-cpu_model.family')]"
# #                    "//td[@class='a-span9']"
# #                    "//span"))).text
# # except:
# #     cpu = ('No CPU model was not found!')
# # CPU_models.append(cpu)
# # print(f"CPU model:", cpu)



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


brand_name = []
model_name = []
screen_size = []
ram = []
storage = []
cpu_model = []
operating_system = []
price = []
rating = []
review_count = []
graphics_card_description = []



pages_number = 20
base_url = 'https://www.amazon.in/s?k=laptops'
current_page = 1

for i in range(1, pages_number+1):
    if current_page ==1:
        url = base_url
    else:
        url = f'{base_url}&page={current_page}'

    driver.get(url)
    print(f'\nScraping page {current_page}...')

    try:
        laptop_links = driver.find_elements(By.XPATH,
                                            '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')

        laptop_urls = [link.get_attribute('href') for link in laptop_links]
        print(f'Number of laptops on a page {current_page}: {len(laptop_urls)}')

        if len(laptop_urls) == 0:
            print(f'No laptops were found on the page {current_page}, skipping....')
            continue



        for url in laptop_urls:
            driver.get(url)
            print('\n')


            try:
                laptop_brand_element = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//tr[@class='a-spacing-small po-brand']//td[@class='a-span9']//span")
                    )
                )
                laptop_brand = laptop_brand_element.get_attribute('textContent').strip()
            except:
                laptop_brand = 'No brand'
            print(f'Brand: {laptop_brand}')
            brand_name.append(laptop_brand)

            try:
                laptop_model_element = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//tr[@class='a-spacing-small po-model_name']//td[@class='a-span9']//span")
                    )
                )
                laptop_model = laptop_model_element.get_attribute('textContent').strip()
            except:
                laptop_model = 'No model'
            print(f'Model: {laptop_model}')
            model_name.append(laptop_model)

            try:
                laptop_screen_element = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//tr[@class='a-spacing-small po-display.size']//td[@class='a-span9']//span")
                    )
                )
                laptop_screen = laptop_screen_element.get_attribute('textContent').strip()
            except:
                laptop_screen = 'No screen size'
            print(f'Screen size: {laptop_screen}')
            screen_size.append(laptop_screen)


            try:
                laptop_ram_element = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//tr[@class='a-spacing-small po-ram_memory.installed_size']//td[@class='a-span9']//span")
                    )
                )
                laptop_ram = laptop_ram_element.get_attribute('textContent').strip()
            except:
                laptop_ram = 'No RAM'
            print(f'RAM: {laptop_ram}')
            ram.append(laptop_ram)


            try:
                laptop_storage_element = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//tr[@class='a-spacing-small po-hard_disk.size']//td[@class='a-span9']//span")
                    )
                )
                laptop_storage = laptop_storage_element.get_attribute('textContent').strip()
            except:
                laptop_storage = 'No storage'
            print(f'Storage: {laptop_storage}')
            storage.append(laptop_storage)


            try:
                laptop_cpu_element = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//tr[@class='a-spacing-small po-cpu_model.family']//td[@class='a-span9']//span")
                    )
                )
                laptop_cpu = laptop_cpu_element.get_attribute('textContent').strip()
            except:
                laptop_cpu = 'No CPU'
            print(f'CPU: {laptop_cpu}')
            cpu_model.append(laptop_cpu)


            try:
                laptop_system_element = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//tr[@class='a-spacing-small po-operating_system']//td[@class='a-span9']//span")
                    )
                )
                laptop_system = laptop_system_element.get_attribute('textContent').strip()
            except:
                laptop_system = 'No system'
            print(f'System: {laptop_system}')
            operating_system.append(laptop_system)


            try:
                laptop_price_element = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']//span[@class='a-price-whole']")
                    )
                )
                laptop_price = laptop_price_element.get_attribute('textContent').strip()
            except:
                laptop_price = 'No price'
            print(f'Price: {laptop_price}')
            price.append(laptop_price)

            try:
                laptop_rating_element = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH,
                         "//a[@class='a-popover-trigger a-declarative']//span[@class='a-size-base a-color-base']")
                    )
                )
                laptop_rating = laptop_rating_element.get_attribute('textContent').strip()
            except:
                laptop_rating = 'No rating'
            print(f'Rating: {laptop_rating}')
            rating.append(laptop_rating)

            try:
                laptop_reviews_element = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH,
                         "//a[@id='acrCustomerReviewLink']//span[@id='acrCustomerReviewText']")
                    )
                )
                laptop_reviews = laptop_reviews_element.get_attribute('textContent').strip()
            except:
                laptop_reviews = 'No reviews'
            print(f'Reviews: {laptop_reviews}')
            review_count.append(laptop_reviews)

            try:
                laptop_gpu_element = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH,
                         "//tr[@class='a-spacing-small po-graphics_description']//td[@class='a-span9']//span")
                    )
                )
                laptop_gpu = laptop_gpu_element.get_attribute('textContent').strip()
            except:
                laptop_gpu = 'No GPU'
            print(f'GPU: {laptop_gpu}')
            graphics_card_description.append(laptop_gpu)

        current_page +=1

    except Exception as e:
        print(f'An error occurred on page {current_page}: {e}')
        break

driver.quit()


data = pd.DataFrame({
    'Brand': brand_name,
    'Model': model_name,
    'Screen Size': screen_size,
    'RAM': ram,
    'Storage': storage,
    'CPU': cpu_model,
    'Operating System': operating_system,
    'Price': price,
    'Rating': rating,
    'Reviews': review_count,
    'GPU': graphics_card_description
})
data.to_csv('laptops1.csv', index=False)
print('\nData saved to laptops.csv')
















































