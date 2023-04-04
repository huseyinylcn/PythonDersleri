# import csv

# with open("movies.csv","r",encoding="utf-8")as f, open("movies2.csv","w",encoding="utf-8",newline="")as f2:
#     x=csv.reader(f, delimiter=",")
#     y=csv.writer(f2,delimiter="@")
#     for c in x:
#         y.writerow(c)
    
 
 
 
 
 
    # okubakalim = csv.reader(f)
    # for x in list(okubakalim)[1:]:
    #     print(f"Kullanıcı adı {x[0]} Yaşı {x[1]} Çinsiyeti {x[2]}")
    
import json

with open("data.json","r",encoding="utf-8")as f:
    x=json.load(f)
    print(x["dizi"][-1]["name"])
    for c in x["dizi"]:
        print(c["name"],c["surname"])
        