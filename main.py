class Hello:
    def __init__(self, str):
        self.str = str

class MyHello(Hello):
    def tptint(self):
        print("TPTINT!")

from class1 import MyHello

my_hello = MyHello()
my_hello.tptint()
