
box1 = ["plates", "bowls", "cups", "cutlery"]
box2 = ["shirt", "shoes", "hat", "jacket", "tie"]
box3 = ["coke", "fanta", "bigga", "marinda", "water"]
box4 = ["gold chain", "silver rings", "earrings"]

boxes = [box1, box2, box3, box4]

i = 0
n = 0
for box in boxes:
    if i == 2:
        for item in box:
            if n == 2:
                print(item)
                break
            n += 1
    i += 1

