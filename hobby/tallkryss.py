numbers = [1,2,3,4,5,6,7,8,9]

def fir():
	return 21-a-b==10
def sec():
	return 21+c-d==23 
def thi():
	return a*e+f==39
def fou():
	return b-g*h==4
def fiv():
	return c*e-g==67
def six():
	return d+f-h==7

def test():
	return fir() and sec() and thi() and fou() and fiv() and six()

for num in numbers:
	a = num
	for num in numbers:
		b = num
		for num in numbers:
			c = num
			for num in numbers:
				d = num
				for num in numbers:
					e = num
					for num in numbers:
						f = num
						for num in numbers:
							g = num
							for num in numbers:
								h = num
								if test(): print '-------------------'
								print 'a = %i, b = %i, c = %i, d = %i, e = %i, f = %i, g = %i, h = %i' %(a,b,c,d,e,f,g,h)
