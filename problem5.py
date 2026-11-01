def calculate_assessed_value(county, market_value):
    if county == "Cook":
        percent = 0.90
    elif county == "DuPage":
        percent = 0.80
    elif county == "McHenry":
        percent = 0.75
    elif county == "Kane":
        percent = 0.60
    else:
        percent = 0.70

    assessed_value = market_value * percent
    return assessed_value


total_market = 0
total_assessed = 0
answer = "Yes"

while answer == "Yes":
    county = input("Enter county: ").title()
    market_value = float(input("Enter market value of home: "))

    assessed_value = calculate_assessed_value(county, market_value)

    print("Assessed value:", assessed_value)

    total_market += market_value
    total_assessed += assessed_value

    answer = input("Do you want to continue? (Yes or No): ").title()

print("Total market values:", total_market)
print("Total assessed values:", total_assessed)
