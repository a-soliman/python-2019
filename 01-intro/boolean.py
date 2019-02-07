import random
truthy = True
falsy = False


age = 20
is_over_age = age >= 18

my_number = 5
random_num = random.randint(0, 20)
tryes = 0
success = False

while tryes < 3:
    user_num = int(input("Enter a number: "))
    if user_num == random_num:
        print("Good Job")
        success = True
        break

    elif user_num > random_num:
        print("Go Down")

    else:
        print("Go Up")

    tryes += 1

if success == False:
    print(f"The number was {random_num}")

# print(user_number == my_number)
