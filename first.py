print("hello world")
text = "welcome to python world"
print(text)
print("your name:", end='')
namee = input()
print("\nhello ", namee, "\n wellcome to pycharm")

num1, num2 = input('enter  two number:').split()
num1 = int(num1)
num2 = int(num2)
addi = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2
print("{} + {} = {}".format(num1, num2, addi))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
