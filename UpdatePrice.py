'''Write a program to accept prodid & new price and update price in
the mobile data in the table if found else display "mobile does not
exist'''

import pymysql

try:
    id=int(input('Enter ProdID : '))
    pri=int(input('Enter New Price :'))

    con=pymysql.connect(host='bpelctufd9hwmp3j1why-mysql.services.clever-cloud.com',user='udybjaddk8vk0nqx',password='fWqdqHYBWSVaZ0mAfFMQ',database='bpelctufd9hwmp3j1why')
    curs=con.cursor()

    curs.execute("select * from MOBILES where ProdID=%d" %id)
    data=curs.fetchone()

    if data:
        curs.execute("update MOBILES set Price=%d Where ProdID=%d" %(pri,id))
        con.commit()
        print('Price updated...')
        
    else:
        print('mobile does not exist')
        con.close()
except:
    print('failed')