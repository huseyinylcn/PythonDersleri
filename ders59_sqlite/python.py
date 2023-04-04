# import sqlite3 #? pythonun standart kütüphanesi veritutmak için kullanılır
# # x=sqlite3.connect('friend.db')#? bağlantımızı oluşturdu
# # y=x.cursor()
# # # y.execute("CREATE TABLE friends(name, year, score)")#? burada tabloyu oluşturduk
# # c=input("gir")
# # # y.execute(f'INSERT INTO friends VALUES("{c}","21","geldi")')
# # # y.execute("SELECT * FROM friends WHERE name=?",(c,))
# # y.execute("DELETE  FROM friends WHERE name=?",(c,))
# # # print(y.fetchone())
# # # with open("movies.txt","r")as f:
# # #     for h in f:
        
# # #         y.execute('INSERT INTO friends VALUES(?,?,?)',(h.upper(),c,"tyt"))
# # x.commit()
# # x.close()
# #! cursor olayı biraz anlamadım ama imleç oluşturuyoruz artık onun üzerinden ulaşıçaz
# # x=sqlite3.connect("friend.db")
# # y=x.cursor()
# # # y.execute("CREATE TABLE friends(ad,soyad)")
# # with open("movies.txt","r",encoding="utf-8")as f:
   
    
    
# #     for t in f.readlines():
# #          p=t.strip("\n").split(",")
# #          y.execute("INSERT INTO friend VALUES(?,?)",(p[0].title(),p[1],))
# #          print(p)
# # x.commit()
# # x.close()
# x=sqlite3.connect("user.db")
# y=x.cursor()
# # y.execute("CREATE TABLE user(kullanıcı_adı,parola)")

# kull=input("kullanıcı adı: ")
# pas=input("parola: ")
# # y.execute(f"INSERT INTO user(kullanıcı_adı,parola) VALUES('{kull}','{pas}')")

# y.execute(f"SELECT * FROM user WHERE kullanıcı_adı='{kull}' AND parola='{pas}'")

# if y.fetchone():
#     print("GİRİŞ BAŞARILI")
# else:
#      print("GİRİŞ BAŞARISIZ")
    
    
    
    
# # y.execute("DELETE FROM user")
# # y.fetchmany()
# x.commit()
# x.close()