def calculate_ticket_price(miles):
    if miles >= 30:
        price = 12
    elif miles >= 20:
        price = 10
    elif miles >= 10:
        price = 8
    else:
        price = 5

    return price


total_tickets = 0
answer = "Yes"

while answer == "Yes":
    last_name = input("Enter last name: ")
    miles = float(input("Enter miles from downtown Chicago: "))

    ticket_price = calculate_ticket_price(miles)

    print(last_name, "Ticket price:", ticket_price)

    total_tickets += ticket_price

    answer = input("Do you want to continue? (Yes or No): ").title()

print("Total price of all tickets:", total_tickets)
