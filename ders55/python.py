# import json

# with open("data.json","r",encoding="utf-8")as f,open("data2.json","w")as f2:
#     content=json.load(f)
#     for l in content["dizi"]:
#        del l["name"]
#     json.dump(content,f2, indent=4)
    
   
   
        

        


# class Deneme:
#     def __init__(self):
#         self.arin=[]
#     def func1(self,friend):
#         self.friend=friend
#         self.arin.append(self.friend)
# book_1=Deneme()
# book_1.func1("ahmet")
# book_1.func1("mehmet")
# print(book_1.arin)
#? is not 2 nesnenin aynı olup olmadığına bakar

# free=["ahmet","mehmet","fatma",34]
# def func1(fr):
#     if type(fr)is not str: #! burada is not yani değise gireceğim parametre string değilse
#         raise TypeError("İsim string olmak zorunda")
#     if fr not in free: #! burada not in yani free içinde fr varmı diye baktı varsa false çevirir yani içine girmez yoksa true çevirir içine girer
#         raise ValueError("Girilen isim arkadaş listesinde bulunmalı")
#     print(f"en iyi arkadaşım {fr}")

# func1(free[0])
import requests
import json
