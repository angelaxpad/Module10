def calculate_price(make, model, electric, msrp):
    if electric == "Y":
        discount_percent = 0.30
    elif make == "Honda" and model == "Accord":
        discount_percent = 0.10
    elif make == "Toyota" and model == "Rav4":
        discount_percent = 0.15
    else:
        discount_percent = 0.05

    discount = msrp * discount_percent
    new_msrp = msrp - discount
    tax = new_msrp * 0.07
    total = new_msrp + tax

    return total, discount


total_msrp = 0
total_sales = 0
answer = "Yes"

while answer == "Yes":
    make = input("Enter automobile make: ").title()
    model = input("Enter automobile model: ").title()
    electric = input("Is it an electric vehicle? (Y or N): ").upper()
    msrp = float(input("Enter MSRP: "))

    total, discount = calculate_price(make, model, electric, msrp)

    print("Discount:", discount)
    print("Final sales price:", total)

    total_msrp += msrp
    total_sales += total

    answer = input("Do you want to continue? (Yes or No): ").title()

print("Total MSRP:", total_msrp)
print("Total sales prices:", total_sales)
