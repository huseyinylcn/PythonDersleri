import tkinter as tk
import serial

def func1():
    
    
   

    
    ser = serial.Serial("COM3", 115200, timeout=1)
    ser.write(f"AT+CWJAP_CUR={wifiad},{wifi_sifre}".encode())
    ser.close()
    wifiad = wifiadi.get()
    wifi_sifre = sifre.get()

    wifiadi.delete(0,tk.END)
    sifre.delete(0,tk.END)

    tk.messagebox.showinfo("Bilgi", "WiFi şifresi başarıyla değiştirildi!")

# Pencere oluştur ve widgetleri ekle
pencere = tk.Tk()
pencere.geometry("300x330")
pencere.resizable(width="FALSE",height="FALSE")
pencere.title("AGL SİSTEM DEPREM ERKEN UYARI")
baslik = tk.Label(pencere,text="Giriş Yap",font="Times 30")
buton = tk.Button(pencere,text="Giriş Yap",command=func1)
yazi1 = tk.Label(pencere,text="WiFi Adı",font="Times")
wifiadi=tk.Entry(width=24)
yazi2 = tk.Label(pencere,text="WiFi Şifresi",font="Times")
sifre=tk.Entry(width=24, show="*") 
baslik.pack()
yazi1.pack()
wifiadi.pack()
yazi2.pack()
sifre.pack()
buton.pack()
pencere.mainloop()