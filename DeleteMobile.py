'''Write a program to accept prodid, display the mobile data and ask
"Do you want to delete?" if "yes" delete the mobile from the table'''

import pymysql

try:
    id=int(input('Enter ProdID to delete : '))
    con=pymysql.connect(host='bpelctufd9hwmp3j1why-mysql.services.clever-cloud.com',user='udybjaddk8vk0nqx',password='fWqdqHYBWSVaZ0mAfFMQ',database='bpelctufd9hwmp3j1why')
    curs=con.cursor()
    
    curs.execute("select * from MOBILES where ProdID=%d" %id)
    data=curs.fetchone()

    if data:
        print(data)
        cho=input('Do you really want to delete? (yes/no) : ')
        if cho.upper()=='YES':
            curs.execute("delete from MOBILES where ProdID=%d" %id)
            con.commit()
            print(' mobile deleted')
        else:
            print('delete operation cancelled')
    else:
        print('ProdID does not exist')

    con.close()
except:
    print('failed')
