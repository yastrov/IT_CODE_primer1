if True:
    print('True')

def my_func():
    print("hello")
my_func()

def my_func2(name):
    print("hello",name)
my_func2("Andrey")

def my_func3(name, *args, **kwargs): #с помощью * может передать все позиционные значения(массив), с помощью ** именнованые аргументы(словарь)
    print("hello",name)
    print('args',args)
    print('kwatgs', kwargs)
my_func3('Pasha', 4,5,5, phone = 123)

l = lambda n1,n2: n1 + n2
print(l(1,2))

class Car:
    def __init__(self, color: str, number:int):
        self.color = color
        self.number = number
        self.speed = 0
    def move(self):
        print("Погнали")
        self.speed = 100
    def stop(self):
        print("Приехали")
        self.speed = 0
car = Car(color = 'red', number =  321)
print(car.number)
print(car.color)
print(car.speed)
print(car.move)
print(car.stop)


