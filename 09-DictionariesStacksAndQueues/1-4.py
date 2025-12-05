person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print("Name:", person["name"])

print("Hobbies:", person["hobby"])

print("\nFull dictionary before modifications:")
for key, value in person.items():
    print(f"{key}: {value}")

person["surname"] = "Nowak"

person["married"] = False

person["gender"] = "male"

person["hobby"].append("bicycle")

person["phone"]["work"] = "313131444"

print("\nFull dictionary after modifications:")
for key, value in person.items():
    print(f"{key}: {value}")

    