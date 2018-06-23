#coding=utf-8
from selenium import webdriver
import csv

#���������ָ赥��һҳ��url
url = 'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'

#��PhantomJS�ӿڴ���һ��Selenium��WebDriver
driver = webdriver.PhantomJS()

#׼���ô洢�赥��CSV�ļ�
csv_file = open("playlist.csv", "w", newline='')
writer = csv.writer(csv_file)
vriter.writerow(['title', 'number', 'site'])

#����ÿһҳ��ֱ����һҳΪ��
while url != 'javascript:void(0)':
    #��WebDriver����ҳ��
    driver.get(url)
    #�л������ݵ�iframe
    driver.swith_to.frame("contentFrame")
    #��λ�赥��ǩ
    data = driver.find_element_by_id("m-pl-container").\
        find_elements_by_tag_name("li")
    #����ÿһҳ�еĸ赥
    for i in range(len(data)):
        #��ȡ������
        nb = data[i].find_element_by_class_name("nb").text
        if "��" in nb and int(nb.split("��")[0]) > 500:
            #��ȡ����������500��ĸ赥�ķ���
            msk = data[i].find_element_by_css_selector("a.msk")
            #�ѷ����ϵı����������ͬ������һ��д���ļ���
            writer.writerow([msk.get_attribute('title'),
                             nb, msk.get_attribute('href')])
    #��λ��һҳ��url
    url = driver.find_element_by_css_selector("a.zbtn.znxt").\
        get_attribute('href')
csv_file.close()
