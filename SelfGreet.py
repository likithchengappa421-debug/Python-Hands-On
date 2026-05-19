Run_intended = False
message="Running indented"
if Run_intended:
    print(message)

def hello ():
    print("So I am confused")

def my_function():
    greet='Likith'
    return greet


Run_intended = False

while True:
    hello()
    print(my_function())

    # Now we check the condition INSIDE the spinning loop
    if not Run_intended:
        print("stop this shit")
        break




