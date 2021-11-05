import json
import os
import pdb

import datefinder as datefinder
import scrapy
from scrapy import Selector
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from scrapy import Request


class BlogSpider(scrapy.Spider):
    name = 'blogspider'

    def start_requests(self):
        url_list = []
        global returns_page1
        options = Options()
        options.headless = False
        options.add_argument("--window-size=1920,1200")

        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

        # Code to Fetch the List of Links Online through WebDriver#

        # driver = webdriver.Chrome(executable_path=DRIVER_BIN, chrome_options=options)
        # driver.get('https://www.goodreads.com/book/popular_by_date')
        # for x in range(15):
        #     try:
        #         WebDriverWait(driver, 10).until(
        #             EC.element_to_be_clickable((By.XPATH, "//button[@class:'Button Button--transparent Button--small Button--rounded']"))).click()
        #     except Exception:
        #         print(Exception)
        #     try:
        #         WebDriverWait(driver, 10).until(
        #             EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Show more books')]"))).click()
        #     except:
        #         print("Reached bottom of page")
        # data = Selector(text=driver.page_source)
        # d = data.xpath('//div[@class="BookListItem__title"]/h3[@class="Text Text__title3 Text__umber"]/strong/a/@href').getall()
        # for item in d:
        #     url_list.append(item)
        # output_file = open('link_list.json', 'w', encoding='utf-8', )
        # json_object = json.dumps(url_list, indent=4)
        # output_file.write(json_object)

        # Code to Get the Link list As saved in the local json file from web driver#
        with open('link_list.json') as f:
            url_list = json.load(f)

        # Code the make request to each url in the link list#
        for url in url_list:
            yield Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        books = {}

        # Publish Date
        pub_date = response.xpath(
            '//div[@class="uitext darkGreyText"]/div[@class="row"]/following-sibling::div[1]/text()').get().strip()
        matches = datefinder.find_dates(pub_date)
        for match in matches:
            books['publish_date'] = match.strftime("%Y %b %d")

        # book ISBN
        books['ISBN'] = response.xpath('.//meta[@property="books:isbn"]/@content').get()

        # Book Title
        books['title'] = response.xpath('//h1[@id="bookTitle"]/text()').get().strip()

        # Book Author
        books['author'] = response.xpath('.//span[@itemprop="name"]/text()').get()

        # Rating Score
        books['rating_score'] = response.xpath('.//span[@itemprop="ratingValue"]/text()').get().strip()

        #  Rating Count
        books['rating_count'] = response.xpath('.//meta[@itemprop="ratingCount"]/@content').get()

        # Genre
        books['genre'] = response.xpath(
            '//div[@class="elementList "]/div[@class="left"]/a[@class="actionLinkLite bookPageGenreLink"]/text()').getall()

        # Description
        dsec_data = response.xpath('//div[@id="description"]/span/text()').getall()
        desc = str(' '.join(dsec_data))
        books['Description'] = desc

        # the list that contain the data of all books
        booklist=[]

        # if the file with data is present than try will work otherwise it will go to exception where new file willbe genrated
        try:
            with open('book_list.json', 'r') as fp:
                information = json.load(fp)
            information.append(books)

            with open('book_list.json', 'w') as fp:
                json.dump(information, fp, indent=4)


        except:
            output_file = open('book_list.json', 'w', encoding='utf-8', )
            booklist.append(books)
            json_object = json.dumps(booklist, indent=4)
            output_file.write(json_object)



