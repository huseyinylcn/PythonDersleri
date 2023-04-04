
kral="movies.csv"
def func(name,director):
    with open(kral,"a",encoding="utf-8")as f:
         f.write(f"{name},{director}\n")
         
def func1():
    with open(kral,"r", encoding="utf-8")as f:
        lines=[]
        for line in f.readlines():
            lines.append(line.strip().split(","))
            
    return [{f"name":line[0], "director":line[1]} for line in lines]