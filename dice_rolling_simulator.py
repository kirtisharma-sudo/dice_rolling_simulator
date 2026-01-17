import random

print("🎲 DICE ROLLING SIMULATOR 🎲")

while True:
    roll = input("Roll the dice? (y/n): ").lower()

    if roll == "y":
        dice_number = random.randint(1, 6)
        print(f"🎯 You rolled: {dice_number}")
    elif roll == "n":
        print("👋 Thanks for playing!")
        break
    else:
        print("❌ Invalid choice. Please enter y or n.")