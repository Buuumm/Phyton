#Zad1
def fun1(a_lis , b_lis):
    lis = []
    for i in range(0, len(a_list )):
        if i % 2:
            lis.append(a_list [i])
    for i in range(0, len(b_list)):
        if not i % 2:
            lis.append(b_list[i])
    return lis


a_lis  = [i for i in range(1, 16)]
b_lis = [i for i in range(23, 39)]
print(fun1(a_list , b_list))

#Zad2
def fun2(data_text):
    return {'length': len(data_text),
            'letters': list(set(list(data_text))),
            'big_letters': data_text.upper(),
            'small_letters': data_text.lower(),
            }


data_text = "Ziomki"
print(fun2(data_text))

#Zad3
def fun3(text, letter):
    return text.lower().replace(letter.lower(), "")


text = ""
letter = "D"
print(my_fun3(text, letter))

#Zad4
def fun4(temp, temp_type):
    temp = 0
    # if params valid
    if temp < -273:
        return Exception("Temperatura nie istnieje")
    elif temp_type not in ["K", "F", "R"]:
        return Exception("Wybierz rodzaj temp (kelvin - K, fahrenheit - F, rankine - R)")
    # calc
    if temp_type.lower() == "F":
        t = (temp * 1.8) + 32
    elif temp_type.lower() == "K":
        t = temp + 273.15
    elif temp_type.lower() == "R":
        t = (temp + 273.15) * 1.8
    return t


#Zad5
class Calculator:
    def add(self, x, y):
        return x + y
    def difference(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        return x / y
    
#Zad6
from z5 import Calculator

class ScienceCalculator(Calculator):
    def power(self, x, y):
        return pow(x, y)

c = ScienceCalculator()
print(c.power(5, 10))

#Zad7
def fun7(text):
    return text[::-1]

text = "truskawka"
print(my_fun7(text))
