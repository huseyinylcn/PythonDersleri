# name ="arin yazılımlar"
# x=6
# print(len(name)) değişkenin içindeki uzunluğununaldım harf sayısını

# print(name[0:5]) 0 ıncı karakteden baslayıp 5 karaktere kadar terminale yazdırmma

# print(name.title()) title kelimenin basşındakı harfi büyük yapar

# print(name.upper()) bütün harfleri büyük yapar

# print(name.lower()) bütün harfleri kücük yapar

# print(name.count("a")) değişkenin içinde kaç tane a olduğunu Buldum 

# print(name.find("m")) m harfinin kaçıncı sırada olduğunu buldum

# print(name.replace("arin","neos")) burada deişkenin içindeki kelimeyi değiştirdim 1 deger değiştireceğim kelimenin adı 2. değer istediğim kelime

# print(dir(name)) bu obje icin kullanılacak özelliklerii verir

#print(help(str)) #bu obje veya değişken için kullanılabilecek özellikleri verir

# print(help(str.lower)) girdiğimiz methpdun ne işe yaradıgına söyler

# print(abs(x)) sayının kendisini verir yani sayı -5 ise 5 verir


# print(round(x)) yuvarlama işlemi yapar ondalık sayıları hangisine eşit ise ona yuvarlar
# y="45";   y=int(y) string ifadeyi numbere cevirir

# name = input("lütfen isim giriniz:  ")
# soy = input("lütfen soyisim giriniz:  ")
# yas = int(input("lütfen yaş giriniz:  "))

# print(name,soy,yas)

#and oporetörü ve dmek or oporötörü veya demektir  

# isim= input("kullanici adi  ")
# password=input("password   ")
# print(isim=="hüseyin" or password=="123")
# isi="hüseyin"
# isim= input("isim giriniz  ")

# if isim == isi:
#     print("doğru bidiniz")
# elif isim == "hus":
#      print("yaklaştın")
# else:
#     print("yanlış")


# sayi =0
# while sayi <10:
#      sayi=sayi + 1
#      print("hüseyin")
  

# while True:
#     isim=input("isim giriniz:  ")
#     if isim == "cikis":
#         break
#     print(isim)


# liste =[2,4,6]

# for sero in liste:
    
#     print(sero)

# person ={
#     "isim":"hüseyin",
#     "soyisin":"yalçın",
#     "yas":19
# }
# person["renk"]="red"
# print(person)  
# if "renk" in person:
#     print(person["renk"])
# else:
#     print("yok")


# alacaklar =set()
# alacaklar.add("araba")
# alacaklar.add("ev")
# alacaklar.add("kitap")
# alacaklar.remove("araba")
# alacaklar.discard("armut")
# print(alacaklar)
# def bomba(r,t):

#      return r + t

# toplam=bomba(t=2,r=3)
# print(toplam)


# name ='hüseyin'
# hello=f'merhaba {name}'
# print(hello)

# değişkenleri birleştirip yazmak istersen  yukarıda ve aşağıda iki farklı örnekle yaptık 

# name ='hüseyin'
# hello='merhaba {}'
# print(hello.format(name))

 

# name ='hüseyin'
# uzunluğu yazar
# print(len(name))




# name ='hüseyin'

# print(name[0:5])




# name ='hüseyin'

# print(name.find('s'))



# DERS 5 SAYISAL VERİ METOTLARI

# aşagıda bir cümle yazrkrn ve o cümlenin içinde bir değişken kullanıcaksan 
# hepsi string ifade olması gerekir 
# age =22
# x ='ben ' + str(age) +' yaşındayım.'
# print(x)



#?DERS 6 UYGULAMA DERSİ


# z="23"
# x="hell'o word"
# y=f"merhaba {x} naber {z}" 

# print(y)
# abs mutlak degerini verir
# tam sayıya round yuvarlar
# pow kuvvetini alır
# max min en yüksek değeri ve enküçük değeri alır
# += str int

# name=["1","2","hüseyin",45]

# name.append("bomba")
# name[0]=""
# name.insert(0,"ben")
# del name[3]
# print(name)

# for x in name:
#     print(f"gezilen şehir: {x}")

# for ne in range(1,11):
#     print(ne)


# ko = list(range(1,20))
# print(ko)


# dersler=["bomba","boşver","nediyonla","affet"]
# print(dersler[1].upper())
# print(dersler[-1].upper())

#! tuple dizileri içini değiştiremeyiz
#!for dögüsünde gireceğin ilk deger istediğin bir değer olabilir 2. deger neyi döndürmek istiyorsan
# x={"tahran","edirne","istanbul","izmir","bilecik"}
# y=["jnjn","njnkjj"]
#! süslü parantezler ile yaptığın dizi aynı olan değerlerin 1 tanesini alır ve onu yokmuş gibi davranır
# x.add("edirne")
# x.discard("hello")
# x.update(y)
# x.clear()
# print(x)
# for c in x:
#     print(c)

# monster_1={"name":"bomba", "power":10,"color":"red"}


# monster_1["boy"]=1.80
# x=monster_1["name"]
# print(monster_1.get("kk"))
# z=monster_1.pop("name")
# monster_1["name"]="bomba"
# print(monster_1)
# print(z)
# for c in monster_1.items():
#     print(c)

# x=[
#     {"name":"bomba","age":25},
#     {"name":"hüseyin","age":25}

# ]
# print(x[0]["name"])
# x=36==36
# print(x)




# x={"name":"Hüseyin","surname":"yalçın","age":19}
# print(type(x))
# c=18
# k=int(input("yaşınızı giriniz: "))


# if c<=k:
#     print("oy kullanabilirsiniz")
#     for z in x.keys():
#         print(z)
        

# elif c>k:
#     v=c-k
   
#     print("yaşınız küçük",v,"yıl daha bekleyin")

 
# x= input("sayı girin:  ")
# y=int(x)**2

# print(y)


# z=5.8
# c=round(z)
# print(help(c))

# x=int(input("sayı girin: "))
# y=x%2
# if y==0:
#     print(f"{x} çift sayıdır")
# else:
#     print(f"{x} tek sayıdır")

# x=int(input("sayı giriniz: "))
# if x < 0:
#     print("negatif")
# elif x>=0:
#     print("pozitif")

# x=int(input("sayı: "))
# y=int(input("sayı: "))

# if x>y: print(f"{x} sayısı {y} sayısından büyüktür")

# else: print(f"{y} sayısı {x} sayısından büyüktür")



# x={"hüseyin":100,"ahmet":10,"mert":90,"ferudun":20}
# for z, c in x.items():
#     if c>=50:
#         print(f"{z} aldığı not {c} gecti")
#     else:
#          print(f"{z} aldığı not {c} kaldı")

# x="sherd"
# y=0
# while y<=10:
#     print(x)
#     y=y+1

#!Güzel bir Örnek

# m=True
# x=""
# y=4
# while m:
#     x=input("sayı: ")
#     y=y-1   
#     if y>0:
#         print(f"{y} hakkınız kaldı")

#     elif y<=0:
#         print("hakkınız kalmadı")
#         break
    
#     if x=="ben":        
#         print("doğru")

#         m=False
#     if y==0:
#         print("hakkınız kalmadı")
#         m=False


# x=-1
# while x<10:
#     x+=1
#     print(x)
#     if x==5:
#         break

# x=0
# while x<10:
#     x+=1
#     if x % 2==1:
#         continue
#     print(x)    

# v=["hüseyin","bomba","ahmet"]

# for x in v:
#     if x=="bomba":
#         continue
#     print(x) 

# x=int(input("min sayi: "))
# v=int(input("max sayi: "))

# for c in range(x,v):
#     if c%2 !=0:
#         continue
#     else:
#         print(c)




#!ders 20 tekrar et

# x=["hüseyin","mehmet","ali","ayşe","mustafa"]
# c=0
# while (c<len(x)):
#     z=x[c]
#     c+=1
#     if z=="ayşe":
#         continue
#     print(z) 
   

# for z in x:
#     if z=="ayşe":
#         continue
#     print(z)
# sacim=input("tekmi çiftmi ")



# if sacim=="cift":
#     sayi1=int(input("sayı1 girin :"))
#     sayi2=int(input("sayi2 girin :"))
#     if sayi1<sayi2:
#         for z in range(sayi1,sayi2):
#           if z%2==0:
#             print(z)

#     if sayi1>sayi2:
#         sayi1=int(input("sayı1 girin :"))
#         sayi2=int(input("sayi2 girin :"))
#         for z in range(sayi2,sayi1):
#            if z%2==0:
#              print(z)

# if sacim=="tek":
#      sayi1=int(input("sayı1 girin :"))
#      sayi2=int(input("sayi2 girin :"))
#      if sayi1<sayi2:
#         for z in range(sayi1,sayi2):
#           if z%2!=0:
#             print(z)

#      if sayi1>sayi2:
#         sayi1=int(input("sayı1 girin :"))
#         sayi2=int(input("sayi2 girin :"))
#         for z in range(sayi2,sayi1):
#            if z%2!=0:
#              print(z)


# import random
# x=random.randint(1,100)
# tahmin=int(input("1 ile 100 arasında sayı girin:  "))

# while x != tahmin:
         
#     if x < tahmin:
#         print("aşagı")
#         tahmin=int(input("1 ile 100 arasında sayı girin:  "))
        
#     elif x > tahmin:
#         print("yukarı")
#         tahmin=int(input("1 ile 100 arasında sayı girin:  "))
        
# if x==tahmin:
#         print("buldunuz")
# 



# for z in x:
#     print(z)

# x=["hüseyin","yalcın"]

# print(f"benim adım {x[0]} soyadım ise {x[1]}")
# print(" benim adım {0} soyadım ise {1}".format(x[0][0:5],x[1]))

# x=0
# y=0
# for z in range(0,100,5):
#     x=z**2
#     y=x**(1/2)
#     print(round(y))
    
# s1 =10
# s2=20
# s3=30
# s4=40
# s1,s2,s3,s4=s4,s1,s2,s3

# print(s1)

#! def functiona verdiğimiz key word function  oluştururken kullanıcaz

# def func():
#     print("hello word")
    

# # func()
# def func(username,name):
#     print(f"hello {username} hello {name}")
    
# func("hüseyin","seda")

# def func1():
#     return 5 + 10


# def func2():
#     print(5 + 10)
    
# x=func1()
# y=func2()
    
# print(f"func1 {x}")
# print(f"func2 {y}")

# x=[1,2,3,4,5,6,7]
# z=tuple(x)
# print(type(z))

# def func(x):
#     return x**2

# print(func(5))    
    
# y=lambda a,b=10: a + b

# k=y(10,10)
# print(k)


# def func1(x):
#     return x**2

# l=int(input("sayi : "))
# z=func1(l)
# print(f"{l} sayısının karesi {z}")

# v=input("işlem secin: ")
# x=int(input("sayı Girin: "))
# z=int(input("sayı Girin: "))
# if v=="c":
#     c=lambda:x*z
#     print(c())
# if v=="t":
#     b=lambda:x+z
#     print(b())
# v=[3,5,6,10]
# def func():
#     x=1
#     for z in v:
#         x*=z
#     return x
        
# n=func()
# print(n)
 
# a=int(input("sayı girin : "))

# def func(a):
#     if a==0:
#         return 1
#     else:
#         return a *func(a-1)
        
# print(func(a))


# x="hüseyin"
# def func1():
#     x="yusuf"
#     return x

# def func2():
#     x="mert"
#     return x
 
        

# print(f"func1 {func1()} ")

# print(f"func3 {func2()} ")



#! __init__ her yeni nesne oluşturduğumuzda çalışan bir metottur
# class car:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def newcar(self):
# #         return f"araba markası {self.x} ve modeli {self.z}"
    
# # car1=car("bmw","i5",2012)
# # car2=car("spring","r9",1994)          



# # print(car1.newcar())

# # class dizi:
# #     def __init__(self,dizi,diziS):
# #         self.diziAdi=dizi
# #         self.diziSuresi=diziS
# #     def func(self):
# #         return f"Dizi Adı {self.diziAdi} Dizi Süresi {self.diziSuresi}"

# # dizi_1=dizi("kurtlat vadisi pusu","Sonsuz")
# # dizi_2=dizi("Ezel","Sonsuz")
# # print(dizi_1.func())
# # print(dizi_2.func())

# # #!^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# c=input("öğrençi adı: ")
# b=input("ders adı giriniz: ")

# class kitap:
#     cv=0
#     def __init__(self,j,x,y,z):
#         self.name=j
#         self.matematik=x
#         self.fizik=y
#         self.veribilimi=z
#         kitap.cv+=1
   
#     def func(self):
#         if c==self.name:
#             if b=="veribilimi": 
#                 return sum(self.veribilimi.values())/len(self.veribilimi)
#             if b=="fizik":
#                 return sum(self.fizik.values())/len(self.fizik)
#             if b=="matematik":
#                 return sum(self.matematik.values())/len(self.matematik)
            
# not1=kitap("Hüseyin",{"sinav1":20,"sinav2":20,"sinav3":70},{"sinav1":80,"sinav2":80,"sinav3":70},{"sinav1":40,"sinav2":80,"sinav3":70})

# print(not1.func())

# # #!  __dict__ metodu bütün özellikleri verir
# # print(not1.__dict__)


#! # #!^^^^^^^^^^^^^^^^^^^^^^^^^^^

# # # class kisi:
# # #     zamoranı = 1.1
# # #     kisisayisi=0
# # #     def __init__(self,isim,yas):
# # #         self.isim = isim
# # #         self.yas = yas
# # #         kisi.kisisayisi+=1
        
# # #     def func(self):
# # #         return self.yas*self.zamoranı
        

# # # kisi1=kisi("Ali",20)
# # # kisi2=kisi("Veli",20)
# # # kisi1.zamoranı=1.2
# # # print(kisi1.func())
# # # print(kisi.kisisayisi)
  
         
# # # def func(ne):
# # #     print(f"{ne} adamdır")

# # # func("hüseyin")

# # # c=int(input("sayı: "))
# # # def func1():
# # #     print(c+10)

# # # func1()



# # #? ders 27 tekrar et sonra başla
# # #! başarıyan gideyen yolda sıkılmakta vardır



# # class ben:
# #     School_name="job hig scholl"
# #     okul="bumu"
# #     kisi=0
    
# #     def __init__(self,name,age,grades):
# #         self.name=name
# #         self.age=age
# #         self.grades=grades
# #         ben.kisi+=1
# #     def func1(self):
# #         return sum(self.grades)/len(self.grades)
# #     @classmethod
# #     def x(cls,ad,sd):
# #         cls.School_name=ad
# #         cls.okul=sd
# #     @staticmethod
# #     def ne():
# #         return f"mesaj geldi"
# # ben.x("y lisesi",12)

# # ben1=ben("mahmut",34,[23,45,67,78])
# # ben2=ben("alihan",23,[23,65,67,98])
# # # print(ben2.ne())
# # # print(round(ben1.func1()))
# # # print(ben1.__dict__) özelliklerini verir
# # class sen():
# #     def __init__(self, name, age, grades,uni):
# #         super().__init__(name, age, grades)
# #         self.uni=uni
    
# # olur=sen("arin",30,[90,94,97,89,90],"özel çamlıca lisesi")
# # print(olur.uni)
# # print(olur.func1())
# # print(ben1.name)


# class job:
    
#     school_name="meslek lisesi"
#     number=0
#     def __init__(self,name,age,grades):
#         self.name=name
#         self.age=age
#         self.grades=grades
#         job.number+=1
        
       
        
#     def func(self):
#         return sum(self.grades)/len(self.grades)
#     def func1(self):
#         return f"okul isimi {self.school_name}"
# x=job("hüseyin",19,[45,78,89,98])
# y=job("hüseyin",19,[45,78,89,98])
# z=job("hüseyin",19,[45,78,89,98])
# v=job("hüseyin",19,[45,78,89,98])
# print(job.number)
# # x.name="yusuf"
# # print(x.name)



# class Circle:
#     pi =3.14
    
#     def __init__(self,radius):
#         self.radius=radius
        
#     def area(self):
#         return self.radius*self.radius*self.pi
#     def __repr__(self):
#         return f"{__class__.__name__} nesnesi ve yarı capı {self.radius} radius"
        
# x=Circle(1)

# print(x.__repr__())




# x=[1,3,4,5,9]
# print(type(x))




# x="55"
# y=35
# z=20
# print(x+x)
# # 5555 3575 110

# x=55
# y="35"
# z=20
# b=x+z
# l=str(b)
# print(y+l)

# x=55
# y=35
# z=20
# print(x+y+z)



# a=25
# x=10
# print(a+x)

# a="25"
# x="10"
# g=int(a)
# k=int(x)
# l=g+k
# o=str(l)
# print(o+x)


# a=25
# x=10
# c=a-x
# j=str(c)
# l=str(a)
# print(l+j)
#6852


# s1=12
# s2=56
# s3="34"
# s4="18"

# l=int(s4)+s1
# g=str(l)
# b=s2+int(s3)
# xx=str(b)
# print(g+xx)

# y=s1+s2
# r=int(s3)+int(s4)
# print(str(y)+str(r))


# u=s2+int(s3)+s1
# print(str(u)+s4)

#!basriberkay@gmail.com
#?5376925242





# x=int(input("sayı1: "))
# z=int(input("sayı2: "))
# y=int(input("sayı3: "))

# print(str(x+y)+str(z))

# print(str(x)+str(y+z))

# print(str(x+z+y)+str(x))


#!Ödev1

# s1=24
# s2=44
# s3="14"
# s4="55"

# print(str(s1+s2+int(s3))+s4)

# print(str(int(s3)+int(s4))+str(s1+s2))

# print(str(int(s4)+int(s3)+s2)+str(24))
# #!Ödev1

#!Ödev 2
# c=input("öğrenci adı: ")
# b=input("ders adı giriniz: ")

# class Not:
    
#     def __init__(self,j,x,y,z):
#         self.name=j
#         self.matematik=x
#         self.fizik=y
#         self.veri_bilimi=z
      
   
#     def func(self):
#         if c==self.name:
#             if b=="veri_bilimi": 
#                 return sum(self.veri_bilimi.values())/len(self.veri_bilimi)
#             if b=="fizik":
#                 return sum(self.fizik.values())/len(self.fizik)
#             if b=="matematik":
#                 return sum(self.matematik.values())/len(self.matematik)
            
# note=Not("Hüseyin",{"sinav1":20,"sinav2":20,"sinav3":70},{"sinav1":80,"sinav2":80,"sinav3":70},{"sinav1":40,"sinav2":80,"sinav3":70})
# if note.func()>40:
#     print("Geçti")
#     print(note.func())
# else:
#     print("Kaldı")
#     print(note.func())
 
#!Ödev 2    

# #!Ödev 3

# deger1=int(input("sayı1: "))

# deger2=int(input("sayı2: "))

# deger3=int(input("sayı3: "))

# print(f"Girilen sayıların ortalaması %{round(deger1 +deger2 + deger3)/3}")

#!Ödev 3



# x ="yaşım "
# y=19
# def sumation(numbers):
#     total=0
#     for x in numbers:
#         total +=x
#     return total



# my_file=open("movies.txt", "r")
# file_content = my_file.read()
# print(my_file.name)
# print(my_file.mode)
# print(file_content)


# my_file.close()

# with open('movies.txt','r') as my_file:
#     for line in my_file:
#         print(line)
  
    

# with open('movies.txt','w') as my_file:
#     my_file.write("satie 1\n")
#     my_file.write("satie 2\n")
#     my_file.write("satie 3\n")

# with open('movies.txt','a') as my_file:
#     my_file.write("satie 1\n")
    

    

# with open('movies.txt','r') as my_file:
#         for line in my_file:
#             print(line)
    


# x="benim adım hüseyin soyadım yalçın"
# print(x[11:18],x[-7:])


# y="4 sayısı 4,2 eşittir ve 8 2nin kübüdür"
# print(y[:20])
# print(y[23:])

# l="bugün neos akademi etkinliği varmış"
# print(l[19:])

# z="arabanın markası kia modeli rio ve 2016 modelidir"
# print("marka: "+z[17:20]+" model "+z[-21:-18]+" yıl "+z[-15:-9])

# k="hava güzel gibiydi ama değilmiş"
# print(f"{k[:4]} kötü {k[10:]}")

# o="markete gittim bir elma 2 armut aldım"
# print(o[8:15]+o[:8]+o[15:18]+o[-12:-6]+o[14:18]+o[18:23]+o[-6:])

# s="sonunu düşünen kahraman olamaz"
# print(s[7:15]+s[-16:-6]+s[:5]+"cu"+s[-7:])

# i="bir gün batacak şehirdeki tüm güneşler"# tüm gün sehirde çıkacak güneşim
# print(i[-12:-9]+i[3:8]+i[15:23]+" çıkacak "+i[-8:-3]+"im")

# x="burada yararsa var"
# print(x[:7]+x[7:14].upper()+x[14:])



# from dosya import Book
# from uye import mumber

# book_1=Book("alexander dumas","siyah lale",False)
# book_2=Book("hz muhahmedin hayatı","diyanet",True)
# book_3=Book("dostyeveski","suc ve ceza",True)


# number_1=mumber("arin")

# number_1.books.append(book_1)
# number_1.books.append(book_2)
# number_1.books.append(book_3)

# print(number_1.read.books)


# text = "Benim adım Hüseyin Yalçın"# ad ve soyadı dışarıda tanımlayın
#Printe ad ve soyadı yazdırın len(),find kullanarak parçala, sayılar kullanılmayacak.
# x="Hüseyin"
# y="Yalçın"
# z=f"Benim Adım {x} Soyadım {y}"

# xx=z[z.find("Hüseyin"):len(x)+z.find("Hüseyin")]
# yy=z[z.find("Yalçın"):len(y)+z.find("Yalçın")]
# print(xx+" "+yy)



# "Bir gün batacak şehirdeki tüm güneşler"

# i="bir gün batacak şehirdeki tüm güneşler"
# print(i[-12:-9]+i[3:8]+i[15:23]+" çıkacak "+i[-8:-3]+"im")

# v="4 sayısı 8'e eşittir ve 4 2'nin küpüdür." 
# v=v.replace("4","8")
# print(v)

# username=".,.,.,.,.!huseyylcn.,.,.,.."
# username=username.strip(",.!*")
# print(username)


# x="benim para sayan pahalı bilgisayarım "
# x=x.split(" ")
# print(x[3])

# y="benim para sayan pahalı bilgisayarım "

# y=y.title()
# y=y.replace("Pahalı","")
# print(y)

# kist1=["bir","iki",[30,[11,22,33]]]
# print(kist1[2][1][1])


# list4=[1,2,3,4,5]
# list1=["bir","iki"]

# list1+=list4
# print(list1)

# sort küçük büyük sıralama
# x=[1,2,3,4,5]
# y=[6,7,8,9]
# x.insert(1,1.5)
# x.extend(y)
# print(x)


# print(x)


# list2=[22,11,44,111,333]
# x= list2[-2]*2
# list2[-2]=x
# print(list2)
 
# list1=["armut","elma","kiraz","şeftali"]
# list1[3]=("patetes")
# print(list1)

# dil=["html","css","javascript"]
# dil.append("python")
# del dil[2]
# print(dil)

# list1=["armut","elma","kiraz","şeftali"]
# list1[2],list1[3]=list1[3],list1[2]
# list1.insert(0,"muz")
# print(list1)

# list1=["armut","elma","kiraz","şeftali"]
# list1.reverse()
# list1.pop(0)
# list1.sort()
# list1.reverse()
# print(list1)

# list1=[1,55,7,12,200]
# list1.sort()
# c=list1.index(12)
# print(list1[c])


#=["elma","armut","kiraz","patates"]
# list2[0]=list2[0].upper()
# list2[2]=list2[2].upper()
# list2[1],list2[3]=list2[3],list2[1]
# print(list2)

# x=input("1: ")
# y=input("2: ")
# z=input("3: ")
# v=input("4: ")
# f=[x,y,z,v]
# f[2]=f[2].upper()
# print(f)









# x=int(input("not: "))
# if x>=80:
#     print(f"{x} not ile geçti ve çok iyi")
# elif x>=60:
#     print(f"{x} not ile geçti ve iyi")
# elif x>=50:
#     print(f"{x} not ile geçti")

# else:
#     print(f"{x} not ile kaldı")



# if x<0:
#     print(f"{x} nagatif")
# else:
#     print(f"{x} pozitif")
    

# x=input("isim soyisim: ")
# y=(x.find(" ")+1)
# if x[0]==x[0].upper() and x[y]==x[y].upper():
#     print("tamamla")


# x=input("sayı 1: ")
# y=input("sayı 2: ")
# while x.isdigit() != True:
#      x=input("sayı 1: ")
#      y=input("sayı 2: ")
#      if x.isdigit()== True and y.isdigit()== True:
#         print(int(x)+int(y))
#      else:
#          print("harf giriniz")


# s1=input("lütfen sayı girin: ")

# if int(s1) % 5==0:
#     if int(s1) % 2 ==0:
#         print(f" {s1} özel sayıdır")


# else:
#     print(f"{s1} özel sayı değildir")


# age =int(input("lütfen yaş girin"))



# if age >=18:
#     note=int(input("sınav notunuz "))
#     if note>=70:
#         print("ehliyet alabilirsiniz")
# kullanici_adi="hsyn"
# parola="1234"
# v=0
# ana=1000
# while v<3:
#     v+=1
#     x=input("kullanıcı adı girin: ")
#     y=input("parola:")
#     if kullanici_adi==x:
#         if y==parola:
#             print("doğru giriniz")
#             c=input("para cekme (1) para yatırma (2): ")
#             print(f"hesapta olan para {ana}")
            
#             if c=="2":
#                 k=int(input("yatırmak istediğiniz miktar"))
#                 print(f"güncel bakiye {ana+k}")
#                 break
#             if c=="1":
#                 k=int(input("cekmek istediğiniz miktar"))
#                 print(f"güncel bakiye {ana-k}")
#                 break
                
        
#     if parola != y:
#         if v<3:
#             print("tekrar deneyin")
#     if v==3:
#         print("hakkınız kalmadı")
#         break
# # import random
    
# # hava=["güneşli","yağışlı","karlı","bulutlu","dolu"]
# # print(random.choice(hava))
    

    
# x=["bomba","hüseyin","yusuf","hamza"]
# for v in x:
#     print(v)
# list1=[]
# for x in range(1,50,3):
#     list1.append(x)
# print(list1)

# for x in range(0,10):
#     if x ==5:
#         continue
#     print(x)

# for x in range(0,10):
#     if x ==5:
#         x="bes"
#     if x ==8:
#         x="sekiz" 
#     print(x)
# list1=[]
# x=["elma","armut","kiraz","portakal","şeftali","muz"]
# z=["17tl","18tl","56tl","34tl","78tl","65tl"]
# secenek=input("ne almak istiyorsunuz ")
# soru=int(input("kilo sayısı: "))
# for y in range(0,6):
#     list1.append(f"{x[y]} {z[y]}")
#     if secenek==list1[y][:list1[y].find(" ")]:
#         print(soru,"kilo", list1[y][:list1[y].find(" ")])
#         j=int(list1[y][list1[y].find(" "):(list1[y].find(" "))+3])*soru
            
# print(f"{j} tl tuttu" )
# list1=[]
# list2=[]
# for x in range(0,100):
#     if x%2==0:
#         list1.append(x)
#     if x%2!=0:
#         print(list2.append(x))
# print(list1)
# print(list2)


# list1=[]
# for x in range(0,100):
#     if x%3==0 and x%7==0:
#         list1.append(x)
# print(list1)

       
# x=input("şifre")
# y="hsyn"
# sifre="123"
# v=3
# while v != 1:
#     v-=1
#     if x==sifre:
#         print("şifre doğru")
#         break
#     if x!=sifre:
#         print(f"{v} hakkınız kaldı")
#         z=input("parolayımı unuttunuz 1 0:")
#     if z=="0":
#         x=input("şifre")
#     if z=="1":
#         g=input("e mail")
#         if y==g:
#             sifre=input("yeni şifre")
#             print("Giriş yapıldı")
#         break
#     if z==1:
#         break
    
    
    
    
# t=0
# b=0
# x=int(input("sayı: "))
# for z in range(0,x):
#     if z%2==0:
#         t+=z
#     if z%2!=0:
#         b+=z
# print(t)
# print(b)


# y=0
# z=[]
# b=0
# k=0
# for x in range(0,70):
#     if x%5==1:
#         y+=x
#     elif x%5==3:
#         z.append(x)
#     elif x%3==0:
#         b+=x
    
#     else:
#         k+=x
# print(y)
# print(z)
# print(b) 
# print(k)       
    
    

#! Proje*******************************
# import random
# x=random.randint(1,50)

# for y in range(1,7):
#     k=int(input("sayı: "))
#     if x==k:
#         print("bildiniz")
#         break
#     if x!=k:
#         if k<x:
#             print("daha yukarı")
#         else:
#             print("daha aşağı")
#         print("bilemediniz")
        
        
 
 
# x=["elma","armut","çilek","kavun","şeftali","kiraz"]
# y=[]
# for i in x:
   
#     if i==x[4]:
#         break

#     y.append(i)
        
# y[0]=y[0][0:-2]
# y[1]=y[1][0:-2]
# print(y)

# for x in range(1,100):
#     if x>50 and x%7==0:
#         print(x)
#         break

# x=[1,5,8,12,67]
# y=[]
# z=[]
# for i in x:
#     i+=5
#     c=i%3
#     z.append(c)
#     y.append(i-5)
# print(y)
# print(z)
# list2=[1,3,5,8,9,12,15]
# list2.sort()
# d=list2[-1]
# list1=[]

# for y in range(0,d+1):
#    if y%2!=0:
#        list1.append(y)
# i=0
# while i<10:
#     i+=1      
#     if i==6:
#         print("merhaba")
#         continue 
#     if i%2==0:
#         print(i)
# meyveler=[12,"meyve",13,"armut","kiraz"]
# list1=[]
# i=-1
# while i<len(meyveler)-1:
#     i+=1
#     if type(meyveler[i]) !=int:
#         list1.append(meyveler[i])
# print(list1)



# for i in range(10):
#     if i==5 or i==8:
#         continue
#     for c in range(6):
#         print(i)


# for i in range(10):
#     if i==4:
#         break
#     for c in range(1,4):
#         print(c)
 

x=int(input("sayi: "))

def bul():
    z=1
    for c in range(0,x):
        if c%2!=0:
            z*=c
    return z
    
print(bul()) 
