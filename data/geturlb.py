import requests
from lxml import etree
from bs4 import BeautifulSoup
from multiprocessing.pool import Pool
import optparse
import time

def _write(url):
    f=open('key.txt','a')
    f.write(url + '\n')

def baidu(keyword,page):
    L = []
    url=('http://www.baidu.com/s?wd=%s&pn=%s') % (keyword,page)
    r=requests.get(url)
    p=etree.HTML(r.content)
    time.sleep(2)
    tags=p.xpath(u'//a[@class="c-showurl"]')
    print ("baidu start")
    for tag in tags:
    # berbool = df.tags.contains('\.html')
    # filter_data = df[berbool]
    # for tag in filter_data:
        try:
            urll=tag.get('href')
            rr=requests.get(urll)
            soup = BeautifulSoup(rr.content, 'html.parser')
            time.sleep(2)
            title = soup.title.string
            gbkutf = soup.original_encoding
            if gbkutf == "utf-8":
                if rr.url:
                    print('[baidu] %s %s' % (rr.url,title) , gbkutf)
                    L.append(rr.url)
        except:
            pass
    return L

# bool = df.str.contains('\.html')
# filter_data = df[bool]

def _bing(keyword,page):
    BL = []
    burl=('https://www.bing.com/search?q=%s&qs=0&first=%s&FORM=BESBTB') % (keyword,page)
    br=requests.get(burl)
    bp=etree.HTML(br.content)
    # print (br.content)
    time.sleep(2)
    btags=bp.xpath(u'//h2/a')
    print ("bing start")
    for btag in btags:
        try:
            burll=btag.get('href')
            brr=requests.get(burll)
            bingup = BeautifulSoup(brr.content, 'html.parser')
            time.sleep(2)
            btitle = bingup.title.string
            bgbkutf = bingup.original_encoding
            if bgbkutf == "utf-8":
                if brr.url:
                    print('[bing] %s %s' % (brr.url,btitle) , bgbkutf)
                    BL.append(brr.url)
        except:
            pass
    return BL


def yahoo(keyword,page):
    YL = []
    print ("n Yahoo start")
    yahoourl=("https://hk.search.yahoo.com/search?fr=yfp-search-sb&p=%s&fr=yfp-search-sb&b=%s&pz=10&xargs=0") % (keyword,page)
    yahoord=requests.get(yahoourl)
    yahoosoup = BeautifulSoup(yahoord.content, "html.parser")
    time.sleep(2)
    yahoot=yahoosoup.select('h3 a[referrerpolicy="origin"]')
    for yahooi in yahoot:
            if yahooi["href"]:
                print('[Yahoo] %s %s' % (yahooi["href"],yahooi.string))
                YL.append(yahooi["href"])
    return YL

#
#
# def bing(keyword,page):
#     L=[]
#     url=("https://www.bing.com/search?q=%s&pn=%s") % (keyword,page)
#     r=requests.get(url)
#     bingp = BeautifulSoup(r.content, "html.parser")
#     t=bingp.select('a[rel="noopener"]')
#     for i in t:
#         if i["data-url"]:
#             print('[Bing] %s %s' % (i["data-url"],i.string))
#             L.append(i["data-url"])
#     return L


#
# def _360(keyword,page):
#     L=[]
#     url=("https://www.so.com/s?q=%s&pn=%s&fr=so.com") % (keyword,page)
#     r=requests.get(url)
#     soup = BeautifulSoup(r.content, "html.parser")
#     t=soup.select('a[rel="noopener"]')
#     for i in t:
#         if i["data-url"]:
#             print('[360] %s %s' % (i["data-url"],i.string))
#             L.append(i["data-url"])
#     return L

def main(keyword,page):
    pool = Pool()
    #num=[x*10 for x in range(0,page)]
    num=[[keyword,page] for page in map(lambda x :x*10,range(page))]
    numm=[[keyword,page] for page in map(lambda x :x,range(page))]
    tmp_K=pool.starmap(_bing,num)
    for k in tmp_K:
        for t in k:
            print(t)
            if t.find("htm") == -1:
                pass
            else:
                _write(str(t))

    tmp_L=pool.starmap(baidu,num)
    for x in tmp_L:
        for a in x:
            if a.find("htm") == -1:
                pass
            else:
                _write(str(a))
    # tmp_Y=pool.starmap(yahoo,num)
    # for y in tmp_Y:
    #     for ya in y:
    #         if ya.find("htm") == -1:
    #             pass
    #         else:
    #             _write(str(ya))


    pool.close()
    pool.join()






if __name__=='__main__':

    banner='''
░░░░░░▄▄▄░░▄██▄        __________________________________________________
░░░░░▐▀█▀▌░░░░▀█▄      __________________________________________________⣿⡇⣿⣿⣿⠛⠁⣴⣿⡿⠿⠧⠹⠿⠘⣿⣿⣿⡇⢸⡻⣿⣿⣿⣿⣿⣿⣿
░░░░░▐█▄█▌░░░░░░▀█▄    _____________________________    ____             ⢹⡇⣿⣿⣿⠄⣞⣯⣷⣾⣿⣿⣧⡹⡆⡀⠉⢹⡌⠐⢿⣿⣿⣿⡞⣿⣿⣿
░░░░░░▀▄▀░░░▄▄▄▄▄▀▀    |_   _ _ _ _ _ _ _ _ _ _         /   /            ⣾⡇⣿⣿⡇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣄⢻⣦⡀⠁⢸⡌⠻⣿⣿⣿⡽⣿⣿
░░░░▄▄▄██▀▀▀▀            | |                            /_/              ⡇⣿⠹⣿⡇⡟⠛⣉⠁⠉⠉⠻⡿⣿⣿⣿⣿⣿⣦⣄⡉⠂⠈⠙⢿⣿⣝⣿
░░░█▀▄▄▄█░▀▀             | |    _______    _______    ______             ⠤⢿⡄⠹⣧⣷⣸⡇⠄⠄⠲⢰⣌⣾⣿⣿⣿⣿⣿⣿⣶⣤⣤⡀⠄⠈⠻⢮
░░░▌░▄▄▄▐▌▀▀▀            | |   /  ___  \  /  _____|  |  ____|            ⠄⢸⣧⠄⢘⢻⣿⡇⢀⣀⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠄⢀
▄░▐░░░▄▄░█░▀▀            | |   | |   | |  | |_____   | |___              ⠄⠈⣿⡆⢸⣿⣿⣿⣬⣭⣴⣿⣿⣿⣿⣿⣿⣿⣯⠝⠛⠛⠙⢿⡿⠃⠄⢸
▀█▌░░░▄░▀█▀░▀        __  | |   | |   | |  \_____  \  |  ___|             ⠄⠄⢿⣿⡀⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⡾⠁⢠⡇⢀
░░░░░░░▄▄▐▌▄▄        \ \_| |   | |___| |   _____| |  | |____             ⠄⠄⢸⣿⡇⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣫⣻⡟⢀⠄⣿⣷⣾
░░░░░░░▀███▀█░▄       \___/    \_______/  |_______/  |______|            ⠄⠄⢸⣿⡇⠄⠈⠙⠿⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣿⣿⡿⢠⠊⢀⡇⣿⣿
░░░░░░▐▌▀▄▀▄▀▐▄       __________________________________________________ ⠒⠤⠄⣿⡇⢀⡲⠄⠄⠈⠙⠻⢿⣿⣿⠿⠿⠟⠛⠋⠁⣰⠇⠄⢸⣿⣿⣿
░░░░░░▐▀░░░░░░▐▌
░░░░░░█░░░░░░░░█                                                          Coded By José Jang (v1.0 RELEASE)
░░░░░▐▌░░░░░░░░░█       使用方法: 把关键词保存在keywords.txt中每行一个            python3 geturlb.py -p [参数]
░░░░░█░░░░░░░░░░▐▌    _____________________________________________________________________________________


                                '''


    print(banner)
    file=open('key.txt','a+')
    file.truncate()
    file.close()
    usage="usage %prog -p/-P <target pages>"
    parser=optparse.OptionParser(usage)
    parser.add_option('-P','-p', type="int", dest="page", default='10', help="search for page")
    # parser.add_option('-K','-k', type="string", dest="keyword", default='', help="search for keywords")
    (options, args)=parser.parse_args()
    #keyword=options.keyword
    keyword = open('keywords.txt','r').readlines()
    page=options.page
    for key in keyword:
        main(key,page)
