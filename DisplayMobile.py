'''Write a program to accept ram and rom, display list of mobiles of
the ram-rom storage space combination'''

import pymysql

con=pymysql.connect(host='bpelctufd9hwmp3j1why-mysql.services.clever-cloud.com',user='udybjaddk8vk0nqx',password='fWqdqHYBWSVaZ0mAfFMQ',database='bpelctufd9hwmp3j1why')
curs=con.cursor()

try:
    rm=input('Enter Ram : ')
    rom=input('Enter Rom :')
    curs.execute("select * from MOBILES Where Ram='%s'AND Rom='%s'" %(rm,rom))
    data=curs.fetchall()

    if data:
      print(data)
    else:
      print('Product does not Found')
      con.close()
except:
    print('failed')
    