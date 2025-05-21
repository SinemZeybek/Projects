        #Dosya Islemleri

f = open("text_for_prac6.txt", "r")    #Once dosyayi aciyoruz.
icerik = f.read()                      #Islemleri yaziyoruz.
print(icerik) 
f.close()                              #Dosyayi kapatiyoruz.


with open("text_for_prac6.txt", "r") as f:     #Dosyayi manuel kapamaya gerek yok.
    icerik = f.read()
    print(icerik)                              

 #readlines: her satiri bir eleman gibi alip liste seklinde verir.


with open("text_for_prac6.txt") as f:
    icerik = f.readlines()
    print(icerik)
    for satir in icerik:
        print(satir,end="")          #ekstra bosluk vermeden yazmasi icin sonuna ekleyip devam ediyor.


with open("text_for_prac6.txt") as f:        #aynisi
    for satir in f:
        print(satir,end="")


with open("text_for_prac6.txt") as f:       #tek bir satir
    satir = f.readline()
    print(satir, end="")    
  # satir = f.readline()
  # print(satir, end="")
  # satir = f.readline()
  # print(satir, end="")
  # satir = f.readline()
  # print(satir, end="")
    pozisyon = f.tell()
    print(pozisyon)                #imlec nerede gosteriyor
    f.seek(0)                      #0 pozisyonuna gonderiyor
    satir = f.readline()                
    print(satir, end="")



with open("text_for_prac6.txt", "r") as f:  
    icerik = f.read(10)        #10 karakter okuyor.
    print(icerik, end="")
    icerik = f.read(10)
    print(icerik, end="")
    icerik = f.read(10)
    print(icerik, end="") 
                     

with open("text_for_prac6.txt", "r") as f:
    okunacak_miktar = 10
    icerik = f.read(okunacak_miktar)
    while len(icerik) > 0: 
        print(icerik, end= "")
        icerik = f.read(okunacak_miktar)


with open("text2_for_prac6.txt", "w") as f:
    f.write("Hello")        #Her seferinde sadece buraya yazilani yaziyor. Eklemiyor.

with open("text2_for_prac6.txt", "a") as f:
    f.write("AAAA") 


 #Bir dosyayi digerine kopyalamak icin:
with open("text_for_prac6.txt") as okunacak:
    with open("text2_for_prac6.txt", "w") as yazilacak:
        for satir in okunacak:
            yazilacak.write(satir)

        