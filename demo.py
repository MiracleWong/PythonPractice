import requests
import json
import time
from lxml import etree
import threading

headers ={
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

News_set = ([])

def getData():
    url = "https://news.163.com/special/epidemic/"
    html=requests.get(url, headers=headers)
    soup=etree.HTML(html.text)
    cover_data=soup.xpath('//div[@class="cover_data"]/div[starts-with(@class,"cover")]')
    current_time=soup.xpath('//div[@class="cover_li"]/span/text()')[0]

    #XPath 语法： //div[@class="cover_data"]/div[starts-with(@class,"cover")]/div[@class="number"]

    print(current_time)
    # while True:
    for cover in cover_data:
        title = cover.xpath('h4/text()')[0]
        number = cover.xpath('div[@class="number"]/text()')[0]
        result = current_time + "" + title + "" + number
        # print(result)

        if result not in News_set:
            News_set.add(result)
            print(title, number, end=" ")

        # time.sleep(60*1)


def getNews():
    url = "https://opendata.baidu.com/data/inner?tn=reserved_all_res_tn&dspName=iphone&from_sf=1&dsp=iphone&resource_id=28565&alr=1&query=%E8%82%BA%E7%82%8E&cb=jsonp_1580992074077_99412"
    html = requests.get(url, headers=headers)
    html_text= html.text
    # print(html_text)
    start = html_text.find('{"ResultCode":')
    end = html_text.find(r'k_recall_srcids\u0000\u0000"}"}')
    # print(str(start) + ":" + str(end))
    #
    json_data = json.loads(html_text[start:end])
    # print(json_data['Result'][0]['DisplayData']['result']['items'])
    data_news = json_data['Result'][0]['DisplayData']['result']['items']
    # while True:
    for data in data_news:
        news_title = data['eventDescription']
        news_time = data['eventTime']
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(news_time)))
        url=data['eventUrl']
        site = data['siteName']
        print(url)
        result = news_title +" 时间为： "+ current_time + " 网站为： "+site
        print(result)
        
        # time.sleep(60*1)


def main():
    # getData()
    getNews()
    # threading.Thread(target=getData()).start()
    # threading.Thread(target=getNews()).start()


if __name__ == "__main__":
    main()
