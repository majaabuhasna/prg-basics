###
# A program that prints your height both in cm and in feet and inches.
#
cm = float(input('Enter your height in cm: '))
feet = (cm / 2.54) // 12
inches = (cm / 2.54) % 12
# calculate the number of feet

# 1 foot = 12 inches

print(f'I am{cm: .0f} cm tall, i.e.{feet: .0f} feet and{inches: .0f} inches')