import time
import string
import datetime
import os
import urllib
from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import traceback
import psycopg2
import re
import http.client  


conn = psycopg2.connect(database="d9ptbtijvjtpr0", 
                        user="xmklahsxcdzulp", 
                        password="62ae1f5695b01bc7070aabc07a557c6f196b5ad89ba7fb22abadb1645931bf37", 
                        host="ec2-54-163-234-99.compute-1.amazonaws.com", 
                        port="5432")

currentPath = os.getcwd()+'/geckodriver'
options = webdriver.firefox.options.Options()
options.add_argument('-headless')

headers = { 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }  

driver = webdriver.Firefox(executable_path=currentPath, firefox_options=options)
now = datetime.datetime.now()
now = now.strftime("%Y%m%d")


try:
## Get Technews data
    driver.get('https://technews.tw/')
    time.sleep(1)

    sourceCode = BeautifulSoup(driver.page_source, "html.parser")
    contents = sourceCode.find_all("div","content")
    for content in contents:
        sourceCode2 = BeautifulSoup(str(content), "html.parser")
        span = sourceCode2.findAll("span","body")
        date = span[1].text
        #start to parse date
        date = re.sub("[^0-9]", "", date)
        date = date[:8]
        if(date==now):
            # set title, share, tags, preText, link
            # set title
            title = sourceCode2.findAll("h1","entry-title")[0].text
            # set link
            link = sourceCode2.findAll("a")[0]['href']
            # set share
            fbIframe = sourceCode2.findAll("iframe")[1]
            response = urllib.urlopen(fbIframe.attrs['src'])
            iframe_soup = BeautifulSoup(response)
            share = iframe_soup.findAll("span", "_5n6h _2pih")[0].text
            # set preText
            aTags = sourceCode2.findAll("a")
            for aTag in aTags:
                aTag.extract()
            preText = sourceCode2.findAll("p")[0].text
            sourceCode3 = BeautifulSoup(str(span[2]), "html.parser")
            tags = ""
            childKeywords = sourceCode3.findAll("a")
            for childKeyword in childKeywords:
                tags += childKeyword.text
            with conn.cursor() as cursor:
                # Read a single record
                sql = '''INSERT INTO `new_media`.`news`
                        (`title`, `date`, `tag`,`share`,`link`,`preText`,`brand`)
                        VALUES ('{}', '{}', '{}', '{}', '{}','{}','{}'); '''.format(title,date,tags,share,link,preText,'technews')
                cursor.execute(sql)
                conn.commit()
                result = cursor.fetchall()
## Get TechOrange data
    driver.get('https://buzzorange.com/techorange/')
    time.sleep(1)

    sourceCode = BeautifulSoup(driver.page_source, "html.parser")
    articles = sourceCode.find_all("article")
    for article in articles:
        sourceCode2 = BeautifulSoup(str(article), "html.parser")
        date = sourceCode2.findAll("time","entry-date")[0].text
        date = date.replace("/","")
        if (date==now):
            title = sourceCode2.findAll("h4","entry-title")[0].text
            link = sourceCode2.findAll("a")[0]['href']
            share = sourceCode2.findAll("span","shareCount")[0].text
            share = share.translate(DD)
            with conn.cursor() as cursor:
                # Read a single record
                sql = '''INSERT INTO `new_media`.`news`
                        (`title`, `date`,`share`,`link`,`brand`)
                        VALUES ('{}', '{}', '{}', '{}','{}'); '''.format(title,date,share,link,'techorange')
                cursor.execute(sql)
                conn.commit()
                result = cursor.fetchall()
## Get Inside data
    driver.get('https://www.inside.com.tw/')
    time.sleep(1)

    sourceCode = BeautifulSoup(driver.page_source, "html.parser")
    articles = sourceCode.find_all("div","post_list_item")
    for article in articles:
        sourceCode2 = BeautifulSoup(str(article), "html.parser")
        if (sourceCode2.findAll("li","post_date")):
            date = sourceCode2.findAll("li","post_date")[0].text
            date = date.replace("\n","")
            date = datetime.datetime.strptime(date, "%Y/%m/%d")
            date = date.strftime("%Y%m%d")
            if (date==now):
                title = sourceCode2.findAll("a","js-auto_break_title")[0].text
                link = sourceCode2.findAll("a")[0]['href']
                preText = sourceCode2.findAll("p","post_description")[0].text
                with conn.cursor() as cursor:
                    # Read a single record
                    sql = '''INSERT INTO `new_media`.`news`
                            (`title`, `date`,`preText`,`link`,`brand`)
                            VALUES ('{}', '{}', '{}', '{}','{}'); '''.format(title,date,preText,link,'inside')
                    cursor.execute(sql)
                    conn.commit()
                    result = cursor.fetchall()

    driver.quit()
    conn.close()
except:
    driver.quit()
    exc_type, exc_value, exc_traceback_obj = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback_obj)    
    conn.close()



