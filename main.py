from my_package.my_module import MyClass 
from my_package.another_module import AnotherClass 
 
if __name__ == "__main__": 
    my_instance = MyClass("Alice") 
    my_instance.say_hello() 
 
    another_instance = AnotherClass("Bob") 
    another_instance.do_something() 
