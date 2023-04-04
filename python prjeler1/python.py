 #! uzayda kaç kişi var bak emmoğlu 
# import requests
# cevap=requests.get("https://jsonplaceholder.typicode.com/posts")
# uzaydaki=cevap.json()
# gh=uzaydaki[1]["id"]
# print(f"uzayda toplam {gh} kişşi var")
# print("----------------------------------------")

# for x in cevap.json():
#     name=x["title"]
#     surname=x["body"]
#     print("----------------------------------------")
    # print(f" title {name} body {surname}")
 #! uzayda kaç kişi var bak emmoğlu 
 
 
 
 
# ?film cekme  projesi 
# from bs4 import BeautifulSoup
# import requests
# import lxml
# request = requests.get("https://www.imdb.com/chart/top")
# soup=BeautifulSoup(request.content,"lxml")

# top_250=soup.find("tbody",attrs={"class":"lister-list"}).find_all("tr")
# film_sira=1
# for film in top_250:
#     adi= film.find("td",attrs={"class":"titleColumn"}).a.text
#     yili= film.find("td",attrs={"class":"titleColumn"}).span.text
#     puan=film.find("td",attrs={"class":"ratingColumn imdbRating"}).strong.get("title")
#     print("film sırası",film_sira)
#     print("film adi", adi)
#     print("film yili", yili)
#     print("film puan", puan)
#     print("-----------------------------")
#     film_sira +=1
# ?film cekme  projesi 
      
      
      
# print("                                              ")
# print("                    |||||||||                 ")
# print("                  |||||||||||||               ")
# print("                 |||||||||||||||              ")
# print("                |||||||||||||||||             ")
# print("           ||||||||||||||||||||||||||||       ")
# print("               ||| ___     ___  |||           ")
# print("               ||--|__|---|__|---||           ")
# print("                |      ||       ||            ")
# print("                ||     oo      ||             ")
# print("                |||   _____   |||             ")
# print("                 ||    ||    ||               ")
# print("                  ||||    ||||                ")
# print("                     ||||||                   ")
# print("                      |||                     ")
# print("                                              ")

# ! harika ötesi
# from gtts import gTTS
# import os
# with open("oldu.txt","r",encoding="utf-8")as f:
#     konuşma = gTTS(text=f.read(),lang="tr",slow=False)
#     konuşma.save("deneme.mp3")
#     os.system("deneme.mp3")

# ! harika ötesi



