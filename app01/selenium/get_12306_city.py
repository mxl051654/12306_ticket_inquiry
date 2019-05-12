#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
import time
import json


class QueryTicket:
    def main(self):
        url = 'https://www.12306.cn/index/index.html'
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-infobars')
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        browser = webdriver.Chrome(chrome_options=options)
        city_number_dict = {}
        try:
            browser.get(url)
            browser.implicitly_wait(20)
            time.sleep(3)
            # 找到热门城市的标签
            elements = browser.find_elements_by_xpath("//ul[@class='popcitylist']/li")
            for i in elements:
                city_name = i.get_attribute('title')
                city_number = i.get_attribute('data')
                city_number_dict.setdefault(city_name, city_number)
            print(city_number_dict)
            with open("city_number.txt", encoding='utf-8', mode='w') as f:
                f.write(json.dumps(city_number_dict, ensure_ascii=False))

        except Exception as e:
            print(e)
        finally:
            browser.quit()


if __name__ == '__main__':
    st = QueryTicket()
    st.main()