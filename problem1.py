def calculateforecast(month, sales):
    if month in ["Jan", "Feb", "Mar"]:
        percent = 0.10
    elif month in ["Apr", "May", "Jun"]:
        percent = 0.15
    elif month in ["Jul", "Aug", "Sep"]:
        percent = 0.20
    else:
        percent = 0.25

    nextmonthsales = sales * (1 + percent)
    return nextmonthsales


answer = "Yes"

while answer == "Yes":
    lastname = input("Enter last name: ")
    month = input("Enter month (Jan-Dec): ").title()
    sales = float(input("Enter sales: "))

    forecast = calculateforecast(month, sales)

    print(lastname, "Next month's forecast:", forecast)

    answer = input("Do you want to continue? (Yes or No): ").title()
