def greet():
    print("Hello, World!")
    pass #when you dont want to return anything you can use pass to avoid an error

greet()

def check_weather(temp):
    if temp > 30:
        print("It's hot outside")
    elif temp < 10:
        print("It's cold outside")
    else:
        print("The weather is nice")

check_weather(35)  # It's hot outside
check_weather(5)   # It's cold outside
check_weather(20)  # The weather is nice