priceTable = {"Quarter final": {"Standard": 55.50, "Premium": 105.20, "VIP": 118.90},
              "Semi final": {"Standard": 75.88, "Premium": 125.22, "VIP": 300.40},
              "Final": {"Standard": 110.10, "Premium": 160.66, "VIP": 400}}

stage = input()
ticketType = input()
ticketQuantity = int(input())
photo = input()

photoPrice = 40 * ticketQuantity
ticketTotal = priceTable[stage][ticketType] * ticketQuantity

if ticketTotal > 4000:
    ticketTotal = ticketTotal * (1 - 0.25)
    photoPrice = 0

elif 4000 >= ticketTotal > 2500:
    ticketTotal = ticketTotal * (1 - 0.10)

if photo == "Y":
    ticketTotal += photoPrice

elif photo == "N":
    photoPrice = 0

print(f"{ticketTotal:.2f}")