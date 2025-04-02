catalogue = {"Stoneling":
            {"Strength": 7,
            "Speed": 1,
            "Stealth": 25,
            "Cunning": 15,},

        "Vexscream":
        {"Strength": 1,
        "Speed": 6,
        "Stealth": 21,
        "Cunning": 19,},

        "Dawnmirage":
        {"Strength": 5,
        "Speed": 15,
        "Stealth": 18,
        "Cunning": 22,},   

        "Blazegolem":
        {"Strength": 15,
        "Speed": 20,
        "Stealth": 23,
        "Cunning": 6,},
        
        "Websnake":
        {"Strength": 7,
        "Speed": 15,
        "Stealth": 10,
        "Cunning": 5,},
              
        "Moldvine":
        {"Strength": 21,
        "Speed": 18,
        "Stealth": 14,
        "Cunning": 5,},
              
        "Vortexwing":
        {"Strength": 19,
        "Speed": 13,
        "Stealth": 19,
        "Cunning": 2,},
        
        "Rotthing":
        {"Strength": 16,
        "Speed": 7,
        "Stealth": 4,
        "Cunning": 12,},
              
        "Froststep":
        {"Strength": 14,
        "Speed": 14,
        "Stealth": 17,
        "Cunning": 4,},
              
        "Wispghoul":
        {"Strength": 17,
        "Speed": 19,
        "Stealth": 3,
        "Cunning": 2,},
        }

def show_card(): #Shows the card and their values (stats/power)
    print("\n---CARDS---")
    for key, value in catalogue.items():
        print(f"\n--{key}--")
        for stat, power in value.items():
            print(f"{stat}: {power}")


while True: 
    print("\n---MONSTER CARDS---")
    print("-Please type in a number between 1-5 to navigate-")
    number = int(input("Enter a number: "))

    if number == 1: #When user inputs 1 it runs the function 'show_card'
        show_card()

    elif number == 5: #Quit/ends the code
        print("Thank you for using MONSTER CARDS")
        break