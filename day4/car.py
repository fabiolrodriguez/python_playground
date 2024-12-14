user_command = ""
is_started = False

while True:
    user_command = input(">").lower()
    if user_command == "help":
        print(''' Usage:
        start - start the car
        stop - stop the car
        quit - exit program
        ''')
    elif user_command == "start":
        if is_started:
            print("The car is already started")
        else:
            print("Started the car!")
            is_started = True
    elif user_command == "stop":
        if is_started:
            print("The car is now stopped")
            is_started = False
        else:
            print("The car is already stopped")
    elif user_command == "quit":
        exit()
    else:
        print("unsupported command")
        exit()
