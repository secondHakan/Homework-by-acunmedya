import math_1 as matematikislemleri
from selenium import webdriver



def Calculator (price, discount):
    a = (price*discount) /100 
    lastprice = price - a 
    return lastprice


NewPrice = Calculator(100, 20)

print(NewPrice)



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
    def __init__ (personnel, title, name, surname):
        personnel.title = title
        personnel.name = name 
        personnel.surname = surname
    
    def welcome_display (personnel):
        message = f"hosgeldin {personnel.title} {personnel.name} {personnel.surname}"
        print(message)

calisan1 = Calisanlar(title , name, surname)
calisan1.welcome_display()


class Human:
    name = "ahmet"
    def __init__(self):
        print("bir instance uretildi yani ornek")
    def talk (self,sentence):
        print(f"{self.name}: {sentence}")
    
    def walk (self, sentence): 
        print(f"{self.name} {sentence}")

human1 = Human()
human1.name = "Osman"
human1.talk("naber beyler")

human2 = Human()
human2.walk("hanimlar ben kosuyorum")


class Car: 
    speed = 12
    def set_speed(self, speed):
        self.speed = speed 

    def drive (self):
        print(f"driving at {self.speed} km/h")

mycar = Car()
mycar.drive()

from selenium import webdriver


chormeDriver = webdriver.Chrome()

print(matematikislemleri.collection(12,3)) 
