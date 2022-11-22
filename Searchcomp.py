'''Write a program to accept company like "samsung" and display list
of mobiles of that category in the ascending order of price'''

import pymysql

con=pymysql.connect(host='bpelctufd9hwmp3j1why-mysql.services.clever-cloud.com',user='udybjaddk8vk0nqx',password='fWqdqHYBWSVaZ0mAfFMQ',database='bpelctufd9hwmp3j1why')
curs=con.cursor()

try:
    cmp=input('Enter Company ')
except:
    cmp=0

curs.execute("select * from MOBILES Where Company='%s' Order By Price ASC" %cmp) 
data=curs.fetchall()

if data:
    print(data)
else:
    print('Product does not Found')


con.close()
