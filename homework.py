print("1 - prof")
print("2 - docent")
print("3 - doktor")
title_code = input("unvaninizi yaziniz: ")
name = input("adinizi giriniz: ")
surname = input ("soyadinizi yazin: ")


if title_code == "1" :
    title = "prof"
elif title_code == "2" : 
    title = "docent"
elif title_code == "3" : 
    title = "doktor"
else : 
    print("unvaniniz yok")


class Calisanlar: 
    def __init__ (worker, title, name, surname):
        worker.title = title
        worker.name = name 
        worker.surname = surname
    
    def welcome_display (worker):
        message = f"hosgeldin {worker.title} {worker.name} {worker.surname}"
        print(message)

calisan1 = Calisanlar(title , name, surname)
calisan1.welcome_display()
