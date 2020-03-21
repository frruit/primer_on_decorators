def decorator_example_1():
    def my_decorator(func):
        def wrapper():
            print("PreProcessing")
            func()
            print("PostProcessing")

        return wrapper

    def say_whee():
        print("Whee!")

    print('-----------------------------------')
    print('Example 1')
    print('-----------------------------------')
    say_whee = my_decorator(say_whee)
    say_whee()
    print(say_whee)


def decorator_example_2():
    from datetime import datetime

    def not_during_the_night(func):
        def wrapper():
            if 7 <= datetime.now().hour < 22:
                func()
            else:
                pass  # Hush, the neighbors are asleep

        return wrapper

    def say_whee():
        print("Whee!")

    print('-----------------------------------')
    print('Example 2')
    print('-----------------------------------')
    say_whee = not_during_the_night(say_whee)
    say_whee()


def decorator_example_3():

    def my_decorator(func):
        def wrapper():
            print("PreProcessing")
            func()
            print("PostProcessing")

        return wrapper

    @my_decorator
    def say_whee():
        print("Whee!")

    print('-----------------------------------')
    print('Example 3')
    print('-----------------------------------')
    say_whee()


if __name__ == '__main__':
    # Remark: this is my test of the decorator article https://realpython.com/primer-on-python-decorators/#functions
    decorator_example_1()
    decorator_example_2()
    decorator_example_3()
