# test for sample/module1.py
# pytest

from sample.module1 import add, MyClass

def test_add():
	assert add(1,2) == 3
	assert add(-1,1) == 0

def test_myclass_greet():
	obj = MyClass("Alice")
	assert obj.greet() == "Hello, Alice!"
