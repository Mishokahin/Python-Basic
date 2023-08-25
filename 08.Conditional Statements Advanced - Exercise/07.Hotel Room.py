month = input()
nights = int(input())
studioPrice = 0
apartmentPrice = 0

if month == "May" or month == "October":
    studioPrice = 50 * nights
    apartmentPrice = 65 * nights
    if nights > 14:
        studioPrice -= studioPrice * 0.3
    elif nights > 7:
        studioPrice -= studioPrice * 0.05

elif month == "June" or month == "September":
    studioPrice = 75.20 * nights
    apartmentPrice = 68.70 * nights
    if nights > 14:
        studioPrice -= studioPrice * 0.2

elif month == "July" or month == "August":
    studioPrice = 76 * nights
    apartmentPrice = 77 * nights

if nights > 14:
    apartmentPrice -= apartmentPrice * 0.1

print(f"Apartment: {apartmentPrice:.2f} lv.")
print(f"Studio: {studioPrice:.2f} lv.")