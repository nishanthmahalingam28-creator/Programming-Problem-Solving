try:
    x=int(input("Enter your name:"))
    print(x)
except NameError:
    print("give correct error")
except ValueError:
    print("give correct value")
