# noinspection PyUnusedLocal
def fizz_buzz(number):
	a=str(number)
	if number%3==0 and number%5==0:
		return "fizz buzz"	
	elif number%3==0 or "3" in a:
		return "fizz"
	elif number%5==0 or "5" in a:
		return "buzz"
	else:
		return str(number)
    #raise NotImplementedError()
