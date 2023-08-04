import random
    
pc_number = random.randint(0, 20)
guesses = []

for attempt in range(1, 10):
        try:
            user_number = int(input(f"Attempt {attempt}:  your number: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_number < 0 or user_number > 20:
            print("Your number is out of the assigned range.")
            continue

        guesses.append(user_number)


        if user_number == pc_number:
            print(" Congrats! You won! ")
            break
        if user_number < pc_number:
                print(" Go higher ")

        if user_number > pc_number:
                [print(" Go lower ")]
else:
            print("Game Over! The secret number was: ", pc_number)

print(" The number of your attempts: ", len(guesses))