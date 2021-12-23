def square(x):
    y = x ** 2
    return y

result = square(3)
print(result)
############################


def loop_five():
    for x in range(0, 25):
        print(x)
        if x == 5:
            # Stop function at x == 5
            return
    print("This line will not execute.")

loop_five()

################################

def main():
    print("This is the main function.")
    hello()

def hello():
    print("Hello, World!")

main()
