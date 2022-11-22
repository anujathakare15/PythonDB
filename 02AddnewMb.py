#Write a program to take new mobile data as input and add mobile tothe DB table
import pymysql

try:
    id=int(input('Enter ProdID : '))
    nm=input('Enter ProdNm : ')
    cmp=input('Enter Company : ')
    rm=input('Enter Ram : ')
    rom=input('Enter Rom : ')
    col=input('Enter Colour : ')
    bt=input('Enter Battery : ')
    pro=input('Enter Processor : ')
    pri=int(input('Enter Price : '))
    rat=float(input('Enter Ratings : '))
    pur=input('Enter Purpose : ')
    con=pymysql.connect(host='bpelctufd9hwmp3j1why-mysql.services.clever-cloud.com',user='udybjaddk8vk0nqx',password='fWqdqHYBWSVaZ0mAfFMQ',database='bpelctufd9hwmp3j1why')
    curs=con.cursor()

    curs.execute("insert into MOBILES (ProdID, ProdNm,Company, Ram, Rom, Colour, Battery, Processor,Price,Ratings,Purpose) values(%d,'%s','%s','%s','%s','%s','%s','%s',%d,%.2f,'%s')" %(id,nm,cmp,rm,rom,col,bt,pro,pri,rat,pur))
    con.commit()
    print('Mobile Added successfully')
    con.close()
except Exception as e:
    print('FAILED...',e)