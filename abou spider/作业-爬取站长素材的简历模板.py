import requests
from lxml import etree
import os
#作业说明，爬取站长素材，简历模板，前5页的所有模板

#创建简历下载目录
file_path = './download_file/'
if not os.path.exists(file_path):
    os.mkdir(file_path)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
#根据url规则获取要爬取的页面url
url_list = []
for i in range(1, 6):
    if i == 1:
        url = 'http://sc.chinaz.com/jianli/free.html'
        url_list.append(url)
    else:
        i = str(i)
        url = 'http://sc.chinaz.com/jianli/free_'+i+'.html'
        url_list.append(url)

#遍历页面url获取的子页面的url地址
for url in url_list:
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    page_list = tree.xpath('//*[@id="container"]/div/a/@href')
    page_num = str(url_list.index(url)+1)
    print('正在下载第'+page_num+'页的模板，请稍后....')
    #遍历子页面的URL地址，获取要下载文件的的标题和下载地址
    for page in page_list:
        response = requests.get(url=page, headers=headers)
        response.encoding = 'utf-8'
        detail_page_text = response.text
        page_tree = etree.HTML(detail_page_text)
        down_url = page_tree.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
        title = page_tree.xpath('/html/head/title/text()')[0].split('_')[0]
        file_name = file_path+title + '.rar'
        #下载文件并保存到本地
        file = requests.get(url=down_url, headers=headers)
        with open(file_name, 'wb') as fp:
            fp.write(file.content)
        print(title+"下载完成")
    print(url+'的模板下载完毕')









