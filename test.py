from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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

pages_number = 5
base_url = 'https://www.amazon.in/s?k=laptops'
current_page = 1


for i in range(1, pages_number+1):

    if current_page == 1:
        url = base_url
    else:
        url = f'{base_url}&page={current_page}'

    driver.get(url)
    print(f'\nScraping page {current_page}...')

    try:
        laptop_links = driver.find_elements(By.XPATH,
                                            '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')

        laptop_urls = [link.get_attribute("href") for link in laptop_links]
        print(f'Number of laptops on page {current_page}: {len(laptop_urls)}')

        if len(laptop_urls) == 0:
            print("No laptops found on this page, skipping...")
            continue

        for url in laptop_urls:
            driver.get(url)

            print('\n')

            try:
                # Scrape laptop brand
                laptop_brand_element1 = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//tr[@class='a-spacing-small po-brand']//td[@class='a-span9']//span"))
                )
                laptop_brand1 = laptop_brand_element1.get_attribute("textContent").strip()
            except:
                laptop_brand1 = 'No brand name'
            print(f'Brand: {laptop_brand1}')
            brand_name.append(laptop_brand1)

            try:
                laptop_model_element1 = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//tr[@class='a-spacing-small po-model_name']//td[@class='a-span9']//span")))
                laptop_model1 = laptop_model_element1.get_attribute("textContent").strip()
            except:
                laptop_model1 = 'No model'
            print(f'Model: {laptop_model1}')
            model_name.append(laptop_model1)

            try:
                laptop_screen_element1 = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//tr[@class='a-spacing-small po-display.size']//td[@class='a-span9']//span")))
                laptop_screen1 = laptop_screen_element1.get_attribute("textContent").strip()
            except:
                laptop_screen1 = 'No screen size'
            print(f'Screen size: {laptop_screen1}')
            screen_size.append(laptop_screen1)

            try:
                laptop_ram_element1 = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH,
                         "//tr[@class='a-spacing-small po-ram_memory.installed_size']//td[@class='a-span9']//span")))
                laptop_ram1 = laptop_ram_element1.get_attribute("textContent").strip()
            except:
                laptop_ram1 = "No RAM"
            print(f'RAM: {laptop_ram1}')
            ram.append(laptop_ram1)

            try:
                laptop_storage_element1= WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//tr[@class='a-spacing-small po-hard_disk.size']//td[@class='a-span9']//span")))
                laptop_storage1 = laptop_storage_element1.get_attribute("textContent").strip()
            except:
                laptop_storage1 = 'No storage'
            print(f'Storage: {laptop_storage1}')
            storage.append(laptop_storage1)

            try:
                laptop_cpu_element1 = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//tr[@class='a-spacing-small po-cpu_model.family']//td[@class='a-span9']//span")))
                laptop_cpu1 = laptop_cpu_element1.get_attribute("textContent").strip()
            except:
                laptop_cpu1 = 'No CPU'
            print(f'CPU: {laptop_cpu1}')
            cpu_model.append(laptop_cpu1)

            try:
                laptop_system_element1 = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//tr[@class='a-spacing-small po-operating_system']//td[@class='a-span9']//span")))
                laptop_system1 = laptop_system_element1.get_attribute("textContent").strip()
            except:
                laptop_system1 = 'No operating system found'
            print(f'Operating system: {laptop_system1}')
            operating_system.append(laptop_system1)

            try:
                laptop_price_element1 = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH,
                         "//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']//span[@class='a-price-whole']")))
                laptop_price1 = laptop_price_element1.get_attribute("textContent").strip()
            except:
                laptop_price1 = 'No price'
            print(f'Price: {laptop_price1}')
            price.append(laptop_price1)

            try:
                laptop_rating_element1 = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH,
                         "//a[@class='a-popover-trigger a-declarative']//span[@class='a-size-base a-color-base']")))
                laptop_rating1 = laptop_rating_element1.get_attribute("textContent").strip()
            except:
                laptop_rating1 = 'No rating'
            print(f'Rating: {laptop_rating1}')
            rating.append(laptop_rating1)

            try:
                laptop_reviews_element1 = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//a[@id='acrCustomerReviewLink']//span[@id='acrCustomerReviewText']")))
                laptop_reviews1 = laptop_reviews_element1.get_attribute("textContent").strip()
            except:
                laptop_reviews1 = 'No reviews'
            print(f'Reviews: {laptop_reviews1}')
            review_count.append(laptop_reviews1)

            try:
                laptop_gpu_element1 = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH,
                         "//tr[@class='a-spacing-small po-graphics_description']//td[@class='a-span9']//span")))
                laptop_gpu1 = laptop_gpu_element1.get_attribute("textContent").strip()
            except:
                laptop_gpu1 = 'No GPU'
            print(f"GPU Description: {laptop_gpu1}")
            graphics_card_description.append(laptop_gpu1)


        current_page +=1
    except Exception as e:
        print(f'An error occurred on page {current_page}: {e}')
        break

driver.quit()


data1 = pd.DataFrame({
    'Brand': brand_name,
    'Model': model_name,
    'Screen Size': screen_size,
    'RAM': ram,
    'Storage': storage,
    'CPU': cpu_model,
    'Operating System': operating_system,
    'Price': price,
    'GPU': graphics_card_description
})
data.to_csv('laptops.csv', index=False)
print("\nData saved to laptops.csv")