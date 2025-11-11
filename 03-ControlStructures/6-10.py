dog_age = int(input("Enter the dog's age in human years: "))
human_age = 0

if dog_age < 0:
    print('Inaccurate age.')

elif dog_age <= 2:
    human_age = dog_age * 10.5

else:
    human_age = 2*10.5 + (dog_age - 2)*4

print(f"The dog's age in dog's years is {human_age} years.")