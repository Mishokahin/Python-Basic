import math
coins = 0
change = float(input())
lv_to_st = change * 100

while lv_to_st > 0:
    if lv_to_st >= 200:
        lv_to_st -= 200
        coins += 1
    elif 200 > lv_to_st >= 100:
        lv_to_st -= 100
        coins += 1
    elif 100 > lv_to_st >= 50:
        lv_to_st -= 50
        coins += 1
    elif 50 > lv_to_st >= 20:
        lv_to_st -= 20
        coins += 1
    elif 20 > lv_to_st >= 10:
        lv_to_st -= 10
        coins += 1
    elif 10 > lv_to_st >= 5:
        lv_to_st -= 5
        coins += 1
    elif 5 > lv_to_st >= 2:
        lv_to_st -= 2
        coins += 1
    elif 2 > lv_to_st >= 1:
        lv_to_st -= 1
        coins += 1

    lv_to_st = math.floor(lv_to_st)

print(coins)