def findExp(g, p, remainder) :
    exp = 0
    num = 0
    test = 0
    while (num < 1000000) :
        num+=1
        test = (g ** num) % p
        if (test == remainder) :
            exp = num
            break
    print(exp)