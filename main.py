import requests
from lxml import etree

# 1. 将目标网站的信息抓取下来
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 "
                  "Safari/537.36 ",
    'Referer': "https://movie.douban.com/"
}
url = "https://movie.douban.com/chart"
response = requests.get(url, headers=headers)
# print(response.text)
text = response.text


# 2. 将抓取下来的信息按一定的规则进行提取
html = etree.HTML(text)
trs = html.xpath("//tr[@class='item']")
movies = []
for tr in trs:
    # print(etree.tostring(tr, encoding='UTF-8').decode('UTF-8'))
    a_s = tr.xpath(".//a[@class='nbg']")    # xpath 永远返回的是一个列表
    for a in a_s:
        title = a.xpath("@title")   # 电影名
        img = a.xpath(".//img//@src")   # 图片
    divs = tr.xpath(".//div[@class='pl2']")
    for div in divs:
        actors = div.xpath(".//p[@class='pl']")
        for actor in actors:
            actor = actor.xpath(".//text()")    # 演员
        score = div.xpath(".//span[@class='rating_nums']//text()")  # 评分
    movie = {
        'title': title,
        'score': score,
        'img': img,
        'actor': actor,
    }
    movies.append(movie)
print(movies)