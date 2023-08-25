penPacks = int(input())
markerPacks = int(input())
litersBoardCleaner = int(input())
discountPercentage = int(input())
totalPrice = penPacks * 5.80 + markerPacks * 7.20 + litersBoardCleaner * 1.20

print(totalPrice - (totalPrice * (discountPercentage/100)))