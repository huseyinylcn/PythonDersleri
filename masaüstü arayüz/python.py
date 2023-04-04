# gelenveri=[
#            "*1hytn*1hytn*1hytn*1hytn*1hytn*1hytn*1hytn*2hytnn"
#            ,"*1hytn*1hytn*1hytn*1hytn*1hytn*1hytn*1hytn*1hytn"
#            ,"*2hytn*3hytn*2hytn*1hytn*1hytn*1hytn*1hytn*1hytn"
#            ,"*2hytn*3hytn*2hytn*1hytn*1hytn*1hytn*1hytn*1hytn"
#            ,"*2hytn*3hytn*2hytn*1hytn*1hytn*1hytn*1hytn*1hytn"
#            ,"*2hytn*3hytn*2hytn*1hytn*1hytn*1hytn*1hytn*1hytn"
#            ,"*2hytn*3hytn*2hytn*1hytn*1hytn*1hytn*1hytn*1hytn"
#            ,"*2hytn*3hytn*2hytn*1hytn*1hytn*1hytn*1hytn*1hytn"
#            ,"*2hytn*3hytn*2hytn*1hytn*1hytn*1hytn*1hytn*1hytn"
#            ,"*2hytn*3hytn*2hytn*1hytn*1hytn*1hytn*1hytn*1hytn"
#            ,"*2hytn*3hytn*2hytn*1hytn*1hytn*1hytn*1hytn*1hytn"
#            ]
 
# yeniliste=[]
# ikinci_liste=[]
# for forgelenveri in gelenveri:
#     temizveri=forgelenveri.split("*")
#     for f in temizveri:
#         if f!="" and f[0]=="1":
#             yeniliste.append(f)
# for ayirma in yeniliste:
#     if ayirma[0] =="1":
#         ikinci_liste.append(ayirma)
# print(ikinci_liste)
# try:
#     text ="bugün hava cok kasvetli"
#     print(text.index("aaa"))
# except ValueError:
#     print("böyle bir nesne yok")
 
x =input("nereye: ")
y=int(input("koltuk numarası: "))
mevcut =list(range(20,50))
olmayan =list(range(20,50))
class yrni:
    
    
    def __init__(self,ad,soyad,koltuk,ucret,nere):
        self.ad=ad
        self.soyad=soyad
        self.koltuk=koltuk
        self.ucret=ucret
        self.nere=nere
      
  
    def func1(self):
        self.nere=x
        if x=="izmir":
            self.ucret+=300
            return f"adım {self.ad} soyadıim {self.soyad} koltuk {self.koltuk} ücreti {self.ucret} giriş yili {self.nere}"
        if x=="edirne":
            self.ucret+=400
            return f"adım {self.ad} soyadıim {self.soyad} koltuk {self.koltuk} ücreti {self.ucret} giriş yili {self.nere}"
        if x=="istanbul":
            self.ucret+=500
            return f"adım {self.ad} soyadıim {self.soyad} koltuk {self.koltuk} ücreti {self.ucret} giriş yili {self.nere}"
    def func2(self):
            mevcut.pop(y)
            for f in mevcut:
                if f==y:
                    return  "koltuk mevcut"
                else:
                    return "koltuk kalmadı"


kisi1=yrni("hüseyin","yalçın",y,0,"")

print(kisi1.func1())
print(kisi1.func2())

