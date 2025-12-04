# Simple Person class with name and age attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person('John', 30)
print(f'Name: {person.name}, Age: {person.age}')

# Simple BankAccount class with deposit, withdraw, and check_balance methods
class BankAccount:
    def __init__(self, account_number, customer_name,  balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited: {amount}, New Balance: {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            print(f'Withdrew: {amount}, New Balance: {self.balance}')

    def check_balance(self):
        print(f'Current Balance: {self.balance}')

account = BankAccount('123456', 'Alice', 1000)
account.check_balance()
account.deposit(500)
account.withdraw(200)
account.check_balance()

# Book class with title and author attributes and a from_string method
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def from_string(title, author):
        return Book(title, author)

book = Book.from_string('Python Programming', 'John Doe')
print(f"Title: {book.title}, Author: {book.author}")

# Inheritance example with Animal base class and Dog and Cat subclasses
class Animal:
        def sound(self):
            return "some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

dog = Dog()
print(dog.sound())
cat = Cat()
print(cat.sound())

# Multiple inheritance example with classes A and B
class A:
    def greet_a(self):
        return "Hello from A"

class B:
    def greet_b(self):
        return "Hello from B"
class C(A, B):
    pass

c = C()
print(c.greet_a())
print(c.greet_b())# Should print "Hello from A" due to method resolution order