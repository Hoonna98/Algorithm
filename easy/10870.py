n = int(input())
rest = 0
def fibonachi(n):
	if n == 1 or n == 0:
		return n
	return fibonachi(n-1) + fibonachi(n-2)

print(fibonachi(n))

