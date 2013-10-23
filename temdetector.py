
import urllib2
import re

# 获取页面数据
def getUrlRespHtml():
    url = 'http://www.weather.com/weather/tenday/USPA1290'
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    respHtml = resp.read()
    # 由于存在汉字，将页面转码成utf-8
    return respHtml

def getVoteLists(html):
    # 编译正则表达式模式
    pattern = re.compile('<p class="wx-temp">')
    matchlist = re.findall(pattern, html)

    vlist = []
    # 将用户ID和票数由str型转换成int型，由于findall()函数得到的列表元素是元组不可改，因此需要转换成可修改的列表
    for item in matchlist:
        itemlist = list(item)
        itemlist[1] = int(itemlist[1])
        itemlist[4] = int(itemlist[4])
        vlist.append(itemlist)
    # 根据票数进行排序
    return sorted(vlist, key=lambda x:x[4], reverse=True)
    
def main():
    print 'loading...'
    html = getUrlRespHtml()
    mList = getVoteLists(html)

    # 显示前16位
    print 'Rank\tID\tVoteNums\tAuthor\t\tContent'
    print '-' * 60
    for i in range(16):
        print '%d\t%d\t%d\t\t%s\t\t%s' % (i+1, mList[i][1], mList[i][4], mList[i][3], mList[i][0])
    

if __name__ == '__main__':
    main()