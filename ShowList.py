 #Write a program to show list of all mobiles

import pymysql

con=pymysql.connect(host='bpelctufd9hwmp3j1why-mysql.services.clever-cloud.com',user='udybjaddk8vk0nqx',password='fWqdqHYBWSVaZ0mAfFMQ',database='bpelctufd9hwmp3j1why')
curs=con.cursor()

curs.execute("select * from MOBILES")
data=curs.fetchall()
print(data)

con.close()