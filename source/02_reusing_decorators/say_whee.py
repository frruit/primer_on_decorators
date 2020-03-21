from decorators import do_twice


@do_twice
def say_whee():
    print("Whee!")


if __name__ == '__main__':
    say_whee()
