movie_name = input()
days_count = int(input())
ticket_count = int(input())
ticket_price = float(input())
theater_percent = int(input())
sales_per_day = ticket_count * ticket_price
gross_profit = sales_per_day * days_count
net_profit = gross_profit * (1 - (theater_percent/100))

print(f"The profit from the movie {movie_name} is {net_profit:.2f} lv.")