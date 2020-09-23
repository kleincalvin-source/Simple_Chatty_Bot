aa = int(input())
bb = int(input())
hh = int(input())
if hh < aa:
    print("Deficiency")
else:
    if hh > bb:
        print("Excess")
    else:
        print("Normal")
