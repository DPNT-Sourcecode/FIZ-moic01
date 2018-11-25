# noinspection PyUnusedLocal
def fizz_buzz(number):
	dlx1=number>10
	ns=str(number)
	fr=ns[0]
	for i in ns[1:]:
		if i!=fr:
			dlx2=False
			break
	div3=number%3==0
	div5=number%5==0
	dlx= dlx1 and dlx2
	in3=str(3) in str(number)
	in5=str(5) in str(number)	
	if (div3 or in3) and (div5 or in5):
		if dlx:
			return "fizz buzz deluxe"
		else:
			return "fizz buzz"
	elif dlx:
		return "deluxe"
	elif div3 or in3:
		return "fizz"
	elif div5 or in5:
		return "buzz"
	else:
		return str(number)
    #raise NotImplementedError()
