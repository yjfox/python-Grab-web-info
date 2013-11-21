# This program is grabbing weather information from a webstie, and transfering F into C

import urllib2
import re

def getUrlRespHtml():
    url = 'http://www.weather.com/weather/tenday/USPA1290'
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    respHtml = resp.read()
    return respHtml

def getVoteLists(html):
    patternmax = re.compile('<p class="wx-temp"> (.*)<sup>')
    patternmin = re.compile('<p class="wx-temp-alt"> (.*)<sup>')
    matchlistmax = re.findall(patternmax, html)
    matchlistmin = re.findall(patternmin, html)
    
    maxtem = []
    mintem = []
    for item in matchlistmax:
    	maxtem.append((int(item)-32)*5/9)
    for item in matchlistmin:
    	mintem.append((int(item)-32)*5/9)
    
    print 'The highest temperature for next few days are:'
    print maxtem
    print 'The lowest temperature for next few days are:'
    print mintem
    
def main():
    print '\nCentigrade = (Fahrenheit-32)*5/9\n'
    print 'loading...'
    html = getUrlRespHtml()
    getVoteLists(html)
   

if __name__ == '__main__':
    main()
