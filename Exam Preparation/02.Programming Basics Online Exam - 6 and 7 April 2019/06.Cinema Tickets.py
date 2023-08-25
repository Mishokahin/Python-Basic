ticket_types = {"standard": 0, "student": 0, "kid": 0}
movie = input()

while movie != "Finish":
    seats = int(input())
    tickets_sold = 0
    for seat in range(seats):
        ticket = input()
        if ticket in ticket_types:
            ticket_types[ticket] += 1
        else:
            break
        tickets_sold += 1

    percentage_occupied = (tickets_sold/seats)*100
    print(f"{movie} - {percentage_occupied:.2f}% full.")

    movie = input()

total_tickets = sum(ticket_types.values())
student_tickets = (ticket_types["student"]/total_tickets)*100
standard_tickets = (ticket_types["standard"]/total_tickets)*100
kids_tickets = (ticket_types["kid"]/total_tickets)*100

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets:.2f}% student tickets.")
print(f"{standard_tickets:.2f}% standard tickets.")
print(f"{kids_tickets:.2f}% kids tickets.")