'''Write a program to accept modelname and purpose, update all
mobiles of the model with the purpose''' 

import pymysql

try:
    nm=input('Enter Prodnm  : ')
    pur=input('Enter Purpose : ')

    con=pymysql.connect(host='bpelctufd9hwmp3j1why-mysql.services.clever-cloud.com',user='udybjaddk8vk0nqx',password='fWqdqHYBWSVaZ0mAfFMQ',database='bpelctufd9hwmp3j1why')
    curs=con.cursor()

    curs.execute("select * from MOBILES where ProdNm='%s'" %nm)
    data=curs.fetchone()

    if data:
        curs.execute("update MOBILES set Purpose='%s' Where ProdNm='%s'" %(pur,nm))
        con.commit()
        print('Purpose updated...')
        
    else:
        print('mobile does not exist')
        con.close()
except:
    print('failed')