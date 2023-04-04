
# try:
    
#     print(12/1)
    
    
# except ZeroDivisionError:
#     print("sayıyı sıfıra bölemezsin")
# except TypeError:
#     print("int sayı ile string sayıyı toplayamazsın")
# except NameError:
#     print("syntax hatası")
# else:
#     print("başaralı")
# finally:
#     print(2+5)
   


# try:
#     num=int(input("sayı : "))
# except:
#     print("lütfen sayı girin")
# else:
#     print("Başarılı")
# finally:
#     print("Ben Buradayım")

# try:
#     with open("movies.txt","r")as f:
#         print(f.read())
# except FileNotFoundError:
#     print("Böyle bir dosya yok")
import movies
user_options="""
FİLM YÖNETİM SİSTEMİ
eklemek için 1
listelemek için 2
düzenlemek için 3
silmek için 4
çıkış yapmak için 0
"""

def main():
    user_input=input(user_options)
    while user_input != "0":
        if user_input == "1":
            add_movie()
            user_input=input(user_options)
        elif user_input == "2":
            list_movie()
            user_input=input(user_options)
        else:
            print(f"{user_input}daha tanımlamadım bacım")
    
    
            
            
def add_movie():
    name=input("film adı")
    director=input("yönetmen adı")
    movies.func(name,director)
    
    
def list_movie():
    g=movies.func1()
    for j in g:
        p=j["name"]
        t=j["director"]
        print(f"Film {p}, Yönetmen {t}")
main()