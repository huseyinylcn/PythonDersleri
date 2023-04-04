list1=[10,20,30,40,50,60,70,80,90,100]
# x=len(list1)
# while len(list1)!=0:
#     x=x-3
#     list1=list1[:x]
#     print(list1)  

# x=input("yazı yaz: ")
# y=x.split(" ")
# d=0
# for c in y:
#     g=len(c)
#     d+=g
# print(y)
# print(d)
 
 
# x = int(input(" sayı gir"))
# y=x*5
# y=str(y)
# print(len(y)) 
# x =input("gir: ")
# b=x.split(" ")
# z=0
# for y in b:
#     for d in y:
#         if d=="a":
#             z=z+1
# print(z)    
# x={}
# x.update({"model":"drim paket"})
# x.update({"marka":"toyota"})
# x.update({"yıl":"2012"})
# x["yıl"]="2015"
# del x["model"]

# print(x)
x={"ad":"hüseyin","soyad":"yalçın","kullanıcı_adı":"hsyn","sifre":1234}
kul=input("kullanıcı adı: ")
sif=int(input("sifre"))
if kul==x["kullanıcı_adı"] and sif==x["sifre"]:
    print(f"hosgeldin {x['ad']} {x['soyad']}")
else:
    print(f"yanlış girdin {x['ad']} {x['soyad']}")  
