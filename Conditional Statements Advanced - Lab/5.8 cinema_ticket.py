day_of_week = input()
ticket_price = 12

if day_of_week == 'Wednesday' or day_of_week == 'Thursday':
    ticket_price += 2
elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    ticket_price += 4

print(ticket_price)
