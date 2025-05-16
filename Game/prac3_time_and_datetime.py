       #Time ve Datetime 

#Epoch = Kabul edilen başlangıç zamanı (01.01.1970)
import time

#Bir iş için geçen süre(saniye)
baslangic = time.time()
liste = []
for i in range(10000):
    liste.append(i)
bitis = time.time()
print(bitis - baslangic)

#Şimdiki zaman veya epochtan itibaren belirtilen saniye sonrası tarih:
zaman = time.ctime()
print(zaman)

zaman = time.ctime(150000) #saniye cinsinden sonrası
print(zaman)

#.strftime() formatlayabiliyoruz.
zaman = time.strftime("%d/%m/%Y %H:%M:%S")  # % - day/month/Year Hour:Minute:Seconds
print(zaman)

#datetime
from datetime import date
from datetime import datetime
from datetime import timedelta

bugun = date.today()   
print(bugun)           #class type 
print(type(bugun))

print(bugun.day)
print(bugun.month)
print(bugun.year)
print(bugun.weekday())     #pazartesi: 0
print(bugun.isoweekday())  #pazartesi: 1 

gecmis_tarih = date(2012, 2, 21)
print(gecmis_tarih.isoweekday())

gecen_zaman = bugun - gecmis_tarih
print(gecen_zaman)
print(type(gecen_zaman))    #class 'datetime.timedelta' 

suan = datetime.now()
print(suan)
print(type(suan))           #class 'datetime.datetime'

print(suan.ctime())
print(datetime.ctime(suan))    #aynı şey

print(suan.date())
print(suan.time())

print(datetime.strftime(bugun,"%d/%m/%Y"))    #aynı şey
print(suan.strftime("%d/%m/%Y"))

#timedelta
suan = datetime.now()
tdelta = timedelta(days=5, hours=3, minutes=18)
print(suan - tdelta)
print(suan + tdelta)

#problem 19
pazar_sayisi = 0
for yil in range(1901,2001):
    for ay in range(1,13):
        if datetime(yil,ay,1).weekday() == 6:     #6 pazar gunu 0dan baslagi icin
            pazar_sayisi += 1 
print(pazar_sayisi)
