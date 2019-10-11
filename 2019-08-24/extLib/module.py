
CONSTANTS = {
        "best_animal": "Affe",
        "best_food": "Pizza"
}

def whatsBestAnimal():
    print(f'Best animal is: { CONSTANTS["best_animal"] }!')

def availableConstants():
    print(f'Available constants are: { ", ".join(CONSTANTS.keys())  }')

###---

if (__name__ == '__main__'):
    print('Executing as standalone script')
