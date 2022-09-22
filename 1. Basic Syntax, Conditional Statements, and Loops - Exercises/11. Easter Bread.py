budget = float(input())
flour_price = float(input())

eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price
bread_price = flour_price + eggs_price + milk_price / 4

breads = 0
colored_eggs = 0
while budget > bread_price:
    budget -= bread_price
    breads += 1
    colored_eggs += 3
    if breads % 3 == 0:
        colored_eggs -= breads - 2

print(f"You made {breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")