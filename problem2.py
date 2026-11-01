def calculate_wall_area(length, width, height):
return 2 * length * height + 2 * width * height


def calculate_gallons(square_feet):
return square_feet / 50


answer = "Yes"

while answer == "Yes":
length = float(input("Enter room length: "))
width = float(input("Enter room width: "))
height = float(input("Enter room height: "))

wall_area = calculate_wall_area(length, width, height)
gallons = calculate_gallons(wall_area)

print("Wall square footage:", wall_area)
print("Gallons of paint needed:", gallons)

# Bonus: ceiling or floor
ceiling_area = length * width
ceiling_gallons = calculate_gallons(ceiling_area)

print("Ceiling or floor square footage:", ceiling_area)
print("Ceiling or floor gallons needed:", ceiling_gallons)

answer = input("Do you want to continue? (Yes or No): ").title()
