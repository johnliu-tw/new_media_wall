import pymysql.cursors
import pprint

pp = pprint.PrettyPrinter(indent=4)

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='python_visual',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `*` FROM `datas` "
        cursor.execute(sql)
        result = cursor.fetchall()


        
        pp.pprint(result)
connection.close()



