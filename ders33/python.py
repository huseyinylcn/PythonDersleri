 # bu yapıda dosyayı kapatman gerekir çünkü dosyanın içind eözel şeyler olabilir
 #! open dosyayı acar adı üstünde r ise modu
 #! read actığın dosyayı okur
 #  print(x.name)# dosyanın adını verir
# x=open("movies.txt", "r")

# print(x.read())
# x.close()#? dosyayı kapatır
# print(x.read())
# bu yapıda ise dosyayı kendisi kapatır 
#bir şeyler yazmak istiyorsan dizinin içine girmen gerekir
# read dosyanın tamamını okur
# readline tek tek satırları gösteriyor kaçtane yazarsak o kadar satır gösteriyor # readlines ise hepsini tek satırda gösteriyor 
# with open("movies.txt", "r") as x:
#     for c in x:
#         print(c,end="")
 
    
# print(x.closed)
#? w modu ile istediğin dosyayı oluşturabilirsin
#? r okuma modu ekleyemezsin silemezsin yani w modu ile dosyayı açarsan dosyada yoksa yeni dosya oluşturur seek ise başlangıç noktasını belirler
# with open("data.txt", "w") as x:
#     x.write("test\n")
#     x.write("test\n")
#     print("eklendi", file=x)
    
# #? a modu var olanın yanına ekler
# with open("movies.txt","a")as g:
#     g.write("\nyanina gecti")


#? x modu yeni dosya yaratır var olan dosya üzerinde işlem yapamazsın

    
with open("movies.txt","r") as f,open("data2.txt","w") as fr:
    fr.write(f.read())
    




