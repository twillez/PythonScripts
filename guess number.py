import random
import sys

def main():
	print("\n  Try to divine a number from X to Y\n\tYou have 10 attempts")
	try:
		x = int(input("X: "))
		y = int(input("Y: "))
		if (x > y):
			print("\n X have not be less than Y")
			sys.exit()
		if (y < 0):
			print("Y or X can not be less than 0")
			sys.exit()
		if (x < 0):
			print("X or Y can not be less than 0")
			sys.exit()
	except ValueError:
		print("\n[!] ValueError")
		sys.exit()

	number = random.randint(x,y)
	attempts = 10

	while (True):
		try:
			n = int(input("\nAnswer: "))
		except ValueError:
			print("\n[!] ValueError")
			break

		if (n != number):
			attempts -= 1

			if (attempts == 0):
				print(f"All attempts ended try again (number: [{number}])")
				break

			print(f"\n{attempts} attempts left")

			if (n < number):
				print(f"??? more than {n}")

			if (n > number):
				print(f"??? less than {n}")

		if (n == number):
			print(f"\nYou divinide the number! Attempts left: {10 - attempts}")
			break

if __name__ == '__main__':
	main()