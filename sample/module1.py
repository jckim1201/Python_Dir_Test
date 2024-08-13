# module1.py

def add(a,b):
	return a+b

def function1():
	print("This is function1 from module1.")

def helper_function():
	print("This is a helper function in module1.")

class MyClass:
	def __init__(self, name):
		self.name = name

	def greet(self):
		return f"Hello, {self.name}!"

	def my_method(self):
		print("This is a method of MyClass.")
