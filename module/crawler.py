import time
from selenium import webdriver
from bs4 import BeautifulSoup

import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='python_visual',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

driver = webdriver.PhantomJS(executable_path
                             ='/Users/JohnLiu/CodeProject/'+
                              'Python_Visualize/phantomjs-2.1.1'+
                              '/bin/phantomjs')


try:
    for i in range(1,2):
        
        driver.get('https://technews.tw/category/internet/page/'+str(i))
        time.sleep(1)

    find_all("Tag Name","Class Name")

        sourceCode = BeautifulSoup(driver.page_source, "html.parser")
        headers = sourceCode.find_all("header","entry-header")
        for header in headers:
            sourceCode2 = BeautifulSoup(str(header), "html.parser")
            title = sourceCode2.findAll("h1","entry-title")[0].text
            span = sourceCode2.findAll("span","body")
            date = span[1].text
            print(date)
            sourceCode3 = BeautifulSoup(str(span[2]), "html.parser")
            keywords = ""
            childKeywords = sourceCode3.findAll("a")
            for childKeyword in childKeywords:
                keywords += childKeyword.text
            print(title)

            
            with connection.cursor() as cursor:
                # Read a single record
                sql = '''INSERT INTO `python_visual`.`datas`
                        (`title`, `date`, `keywords`)
                        VALUES ('{}', '{}', '{}'); '''.format(title,date,keywords)
                cursor.execute(sql)
                connection.commit()
                result = cursor.fetchall()


                
                print(result)
    driver.quit()
    connection.close()
except:
    driver.quit()
    exc_type, exc_value, exc_traceback_obj = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback_obj)    
    connection.close()
