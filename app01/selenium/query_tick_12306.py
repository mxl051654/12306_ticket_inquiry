#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
from app01.selenium import resource
import logging


class QueryTicket:
    @classmethod
    def getRandomHeaders(self):
        # 随机选取User-Agent头
        return random.choice(resource.UserAgents)

    def main(self, url):
        # 构建返回数据JSON
        result = {
            "describe": None,
            "data": None,
        }
        logging.captureWarnings(True)
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-infobars')
        options.add_argument('--start-maximized')
        options.add_argument('user-agent={}'.format(self.getRandomHeaders))
        options.add_argument('--headless')
        browser = webdriver.Chrome(chrome_options=options)
        try:
            all_train_number_list = []
            # url = self.splicing_url(start_city, end_city, start_time)
            browser.get(url)
            browser.implicitly_wait(10)
            button = (By.XPATH, "//tbody[@id='queryLeftTable']/tr")
            WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located(button))
            # 获取总信息
            train_number_describe = browser.find_element_by_xpath("//div[@id='sear-result']/p").text
            result["describe"] = train_number_describe
            element = browser.find_element_by_xpath("//tbody[@id='queryLeftTable']")
            # 找到所有车次
            lists = element.find_elements_by_xpath("./tr[@class='bgc'] | tr[@class='']")
            for i in lists:
                all_train_number_dict = {}
                # 车次
                train_number = i.find_element_by_xpath(".//a[@class='number']").text
                # 出发站
                departure_station = i.find_elements_by_xpath(".//div[@class='cdz']/strong")[0].text
                # 到达站
                destination = i.find_elements_by_xpath(".//div[@class='cdz']/strong")[1].text
                # 出发时间
                departure_time = i.find_elements_by_xpath(".//div[@class='cds']/strong")[0].text
                # 到达时间
                arrival_time = i.find_elements_by_xpath(".//div[@class='cds']/strong")[1].text
                # 历时 ,总时间
                duration_total_time = i.find_element_by_xpath(".//div[@class='ls']/strong").text
                # 历时，是否当日到达
                duration_describe = i.find_element_by_xpath(".//div[@class='ls']/span").text
                # 商务座,特等座
                business_seat = i.find_elements_by_xpath(".//td")[1].text
                # 一等座
                first_class_seat = i.find_elements_by_xpath(".//td")[2].text
                # 二等座
                two_class_seat = i.find_elements_by_xpath(".//td")[3].text
                # 高级软卧
                high_grade_soft_berth = i.find_elements_by_xpath(".//td")[4].text
                # 软卧一等卧
                first_class_sleeping = i.find_elements_by_xpath(".//td")[5].text
                # 动卧
                moving_position = i.find_elements_by_xpath(".//td")[6].text
                # 硬卧二等卧
                two_class_sleeping = i.find_elements_by_xpath(".//td")[7].text
                # 软座
                soft_seats = i.find_elements_by_xpath(".//td")[8].text
                # 硬座
                hard_seat = i.find_elements_by_xpath(".//td")[9].text
                # 无座
                no_seat = i.find_elements_by_xpath(".//td")[10].text
                # 其它
                other = i.find_elements_by_xpath(".//td")[11].text

                all_train_number_dict.setdefault("车次", train_number)
                all_train_number_dict.setdefault("出发站", departure_station)
                all_train_number_dict.setdefault("到达站", destination)
                all_train_number_dict.setdefault("出发时间", departure_time)
                all_train_number_dict.setdefault("到达时间", arrival_time)
                all_train_number_dict.setdefault("历时总时间", duration_total_time)
                all_train_number_dict.setdefault("历时是否当日到达", duration_describe)
                all_train_number_dict.setdefault("商务座特等座", business_seat)
                all_train_number_dict.setdefault("一等座", first_class_seat)
                all_train_number_dict.setdefault("二等座", two_class_seat)
                all_train_number_dict.setdefault("高级软卧", high_grade_soft_berth)
                all_train_number_dict.setdefault("软卧一等卧", first_class_sleeping)
                all_train_number_dict.setdefault("动卧", moving_position)
                all_train_number_dict.setdefault("硬卧二等卧", two_class_sleeping)
                all_train_number_dict.setdefault("软座", soft_seats)
                all_train_number_dict.setdefault("硬座", hard_seat)
                all_train_number_dict.setdefault("无座", no_seat)
                all_train_number_dict.setdefault("其它", other)
                all_train_number_list.append(all_train_number_dict)
            result['data'] = all_train_number_list
            return result
        except Exception as e:
            print(e)
            return result
        finally:
            browser.quit()


if __name__ == '__main__':
    pass
    # st = QueryTicket()
    # ret = st.main('上海', '武汉', '2019-05-28')
    # print(ret)
