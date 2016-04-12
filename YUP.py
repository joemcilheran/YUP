def near_ten():
    num = input("input a postive number \n")
    num = float(num)
    num = int(num)
    num = str(num)
    if (int(num[-1]) > 7) or (int(num[-1]) < 3):
        print("YUP")
    else:
        print("NOPE")
near_ten()
    