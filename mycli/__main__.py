import sys
from .classmodule import myClass
from .funcmodule import my_function

def main():
    print('In main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))

    my_function('Test mycli')
    my_object = MyClass('Sample')
    my_object.say_name()

if __name__ == '__main__':
    main()