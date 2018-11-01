print("Rules that govern the state of water")

current_temp = False

while current_temp is False:
    # user input - this changes temp on every interation
    current_temp = input("Enter a temperature: \n")
    print(current_temp)

    if(int(current_temp) < 0) or (int(current_temp) == 0):
        print("water is a solid. icy!")
        current_temp = False

    elif (int(current_temp) < 100):
        print("water is a liquid. profit!")
        current_temp = False

    elif (int(current_temp) > 100) or (int(current_temp) == 100):
        print("water is a vapour. Hot!")
        current_temp = False
