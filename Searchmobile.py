''' Write a program to accept modelname, search mobile in the table,
show the mobile details if found else display "not found" message'''

import pymysql

con=pymysql.connect(host='bpelctufd9hwmp3j1why-mysql.services.clever-cloud.com',user='udybjaddk8vk0nqx',password='fWqdqHYBWSVaZ0mAfFMQ',database='bpelctufd9hwmp3j1why')
curs=con.cursor()

try:
    nm=input('Enter ProdNM ')
except:
    nm=0

curs.execute("select * from MOBILES where ProdNm='%s'" %nm)
data=curs.fetchone()

if data:
    print(data)
else:
    print('Product does not Found')


con.close()
