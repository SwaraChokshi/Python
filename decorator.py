def deco(func):
    def wrapper():
        print("Adding the neww additional information ")
        func()
        print("Completed adding the additional information ")

    return wrapper


@deco
def greetings():
    print('Inside greeting function ')


greetings()