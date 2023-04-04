import tkinter as tk
form=tk.Tk()
# tk.TK() fonksiyonu ile pencereyi çağırıyoruz aslında burada bencere geliyor ama biz götemiyoruz çünkü hemen gelip gidiyor 
form.title("Tkinter")

tk.Label(form,text="1.Ders",fg="red",font="Times 40 bold",bg="green").pack()
tk.Label(form,text="hüseyin",bg="yellow",font="Times 40 italic bold").pack()




form.mainloop()# mainloop ile durdurabiliyoruz ve pencere gelmiş oluyor