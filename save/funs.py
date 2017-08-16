def isPrime(num):
	flag = 0;
	for i in range(2,num/2):
		if num % i == 0 :
			flag  = 1
			return False
	if flag == 0:
		return True


def rng(num):
	lst1 = []
	lst1.append(num)
	if num == 0:
		return lst1
	rng(num-1)


