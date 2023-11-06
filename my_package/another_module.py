from my_package.my_module import MyClass 
 
class AnotherClass: 
    def __init__(self, name): 
        self.my_instance = MyClass(name) 
 
    def do_something(self): 
        self.my_instance.say_hello() 
