#coding=utf-8
from selenium import webdriver
import csv

#网易云音乐歌单第一页的url
url = 'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'

#用PhantomJS接口创建一个Selenium的WebDriver
driver = webdriver.PhantomJS()

#准备好存储歌单的CSV文件
csv_file = open("playlist.csv", "w", newline='')
writer = csv.writer(csv_file)
writer.writerow(['title', 'number', 'site'])

#解析每一页，直到下一页为空
while url != 'javascript:void(0)':
    #用WebDriver加载页面
    driver.get(url)
    #切换到内容的iframe
    driver.switch_to.frame("contentFrame")
    #定位歌单标签
    data = driver.find_element_by_id("m-pl-container").\
        find_elements_by_tag_name("li")
    #解析每一页中的歌单
    for i in range(len(data)):
        #获取播放量
        nb = data[i].find_element_by_class_name("nb").text
        if "万" in nb and int(nb.split("万")[0]) > 500:
            #获取播放数大于500万的歌单的封面
            msk = data[i].find_element_by_css_selector("a.msk")
            #把封面上的标题和链接连同播放数一起写到文件中
            writer.writerow([msk.get_attribute('title'),
                             nb, msk.get_attribute('href')])
    #定位下一页的url
    url = driver.find_element_by_css_selector("a.zbtn.znxt").\
        get_attribute('href')
csv_file.close()
