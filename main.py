import requests as req
import random
import json
import string
from lxml import etree

def get_ip():
    url="https://www.xicidaili.com/"
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    page=req.get(url,headers=header)
    page.encoding='utf-8'
    print(page.text)
    html=etree.HTML(page.text)
    tree=etree.tostring(html)
    #print(tree.decode('utf-8'))
    ip_list=[]
    for i in range(3,23):
        addr=html.xpath('//*[@id="ip_list"]/tr['+str(i)+']/td[2]/text()')
        port=html.xpath('//*[@id="ip_list"]/tr['+str(i)+']/td[3]/text()')
        protocol=html.xpath('//*[@id="ip_list"]/tr['+str(i)+']/td[6]/text()')
        ip_list.append(protocol[0]+"://"+addr[0]+':'+port[0])
    return ip_list
def test_proxy(proxy):
    url = "http://cmglkw.ltd/"
    header = {"host":"obs-c0ba.obs.cn-east-2.myhuaweicloud.com","User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",}
    proxies={}
    proxies[proxy[:proxy.index(':')]]=proxy[proxy.index(':')+3:]
    try:
        response = req.get(url, headers=header, proxies=proxies, timeout=2)
        if response.status_code == 200:
            print("该代理IP可用：", proxy)
            return proxies
        else:
            print("该代理IP不可用：", proxy)
            return False
    except Exception:
        print("该代理IP无效：", proxy)
        return False

#url
url=''  
header={"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",'Content-Type':'application/json'}
flag=False
count=0
while flag==False:
    proxies=test_proxy(get_ip()[random.randint(0,19)])
    flag=True
while(count<100):
    qq='0'
    while qq[0]=='0':
        qq=''
        qqnum_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        random.shuffle(qqnum_list)
        for i in qqnum_list:
            qq+=str(i)

        #键如果不对请自行更改
        data={"u":qq,"p":''.join(random.sample(string.ascii_letters + string.digits, random.randint(7,11)))}

    try:
        response=req.get(url,headers=header,proxies=proxies,params=data)
    except:
        flag=False
        while flag==False:
            proxies=test_proxy(get_ip()[random.randint(0,19)])
            flag=True
        count+=1
        print('数据发送失败,尝试更换ip')
    else:
        if response.status_code==200:
            print('数据发送成功')
        else:
            print('数据发送失败,HTTP_ERR:'+str(response.status_code))

