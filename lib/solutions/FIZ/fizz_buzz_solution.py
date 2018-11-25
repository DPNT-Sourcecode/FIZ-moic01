# noinspection PyUnusedLocal
def fizz_buzz(number):
    isOdd=number%2!=0
    dlx1=number>10
    dlx2=True
    ns=str(number)
    fr=ns[0]
    for i in ns[1:]:
        if i != fr:
            dlx2=False
            break
    div3=number%3==0
    div5=number%5==0
    dlx3= dlx1 and dlx2
    dlx= dlx3 and isOdd
    in3=str(3) in str(number)
    in5=str(5) in str(number)
    if (div3 or in3) and (div5 or in5):
        if dlx:
            return "fizz buzz fake deluxe"
        elif dlx3:
            return "fizz buzz deluxe"
        else:
            return "fizz buzz"
    elif div3 or in3:
        if dlx:
            return "fizz fake deluxe"
        elif dlx3:
            return "fizz deluxe"
        else:
            return "fizz"
    elif div5 or in5:
        if dlx:
            return "buzz fake deluxe"
        elif dlx3:
            return "buzz deluxe"
        else:
            return "buzz"
    elif dlx3:
        if isOdd:
            return "fake deluxe"
        else:
            return "deluxe"
    else:
        return str(number)
    #raise NotImplementedError()
