#!/usr/bin/env python3
#coding=utf-8

from selenium import webdriver
import requests
import csv
import sys
import re

browser = webdriver.PhantomJS()
browser.implicitly_wait(10)
csvfile = open("JD_Product.csv", "w", newline= '')
writer = csv.writer(csvfile)
writer.writerow(['商品名', '价格', '好评率'])

#爬虫主体
def crow_jd():
    url = str(sys.argv[1])#获取命令行输入的url
    praise_url = "https://sclub.jd.com/comment/productPageComments.action?&productId=3133817&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"#评价页url
    browser.get(url)
    name = browser.find_element_by_css_selector(".sku-name").text
    price = browser.find_element_by_css_selector(".p-price").text
    r = requests.get(praise_url).text
    praise = re.findall(r'\d{1,3}',r)[0]#提取好评率
    writer.writerow([name, price, praise+'%'])
    csvfile.close()
    browser.quit()
    print("商品名:" + name)
    print("价格:" + price)
    print("好评率:" + praise + '%')

if __name__ == '__main__':
    print("正在爬取数据中......")
    crow_jd()
