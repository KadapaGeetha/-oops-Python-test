# 1. student details
class student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(self.name)
        print(self.age)
        print(self.course)
obj = student("Geetha",21,"cse")
obj.display()

# employee salary
class emp:
    def __init__(self,name,basic_salary):
        self.name = name
        self.basic_salary = basic_salary
    def display_salary(self):
        print("name:",self.name)
        print("salary:",self.basic_salary)
obj = emp("geetha",50000)
obj.display_salary()

# bank account
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("deposit money:",amount)
    def withdraw(self,amount):
        if amount <= self.balance:
            print("withdraw amount:",amount)
        else:
            print("insufficient balance")
    def display_balance(self):
        print("account_holder:",self.account_holder)
        print("balance:",self.balance)
    
obj =BankAccount("Geetha",5000)
obj.deposit(100)
obj.withdraw(6000)
obj.display_balance()

# mobile phone

class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print("brand:",self.brand)
        print("model:",self.model)
        print("price:",self.price)
obj = Mobile("Realme","narzo30A",1000)
obj.display()
obj1 = Mobile("Iphone","18pro",2000000)
obj1.display()

# Rectangle calculation
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print(self.length * self.breadth)
    def parameter(self):
        print(2*self.length + 2*self.breadth)
obj = Rectangle(2,3)
obj.area()
obj.parameter()

# student marks
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_marks(self):
        print(self.name)
        print(self.marks)
    def check_result(self):
        if self.marks >= 40:
             print("pass")
        else:
             print("fail")
            
obj=student("geetha",50)
obj.display_marks()
obj.check_result()
obj1=student("yegna",60)
obj1.display_marks()
obj1.check_result()

#Employee Bonus
class Employee:
    def __init__(self,name,salary):
        self.name=name 
        self.salary=salary
    def calculate_bonus(self):
        if self.salary >= 50000:
            bonus = self.salary * 0.10

        else:
            
            bonus = self.salary * 0.05 
        total_salary = self.salary + bonus

        print("Employee name:",self.name)
        print("salary:",self.salary )
        print("bonus:",bonus)
        print("Total_salary:",total_salary)

obj=Employee("Geetha",45000)
obj.calculate_bonus()

#product discount
class Product:
    def __init__(self,product_name,price):
        self.product_name=product_name
        self.price=price
    def calculate_discount(self):
        if self.price >= 5000:
            discount=self.price * 0.20
        elif self.price >= 2000:
            discount = self.price * 0.10
        else:
            discount = self.price * 0.05
        final_price = self.price - discount
        print("name:",self.product_name)
        print("price:",self.price)
        print("discount:",discount)
        print("final price:",final_price)

obj=Product("mobile",9000)
obj.calculate_discount()

# ATM Transaction
class ATM:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("deposit amount:",amount)
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("withdraw amount:",amount)
        else:
            print("insuffiecient balance")
    def check_balance(self):
        print("account_number:",self.account_number)
        print("balance:",self.balance)
obj = ATM(796543221,10000)
obj.deposit(2000)
obj.withdraw(500)
obj.check_balance()

#car information
class Car:
    def __init__(self,brand,model,price,fuel_type):
        self.brand=brand 
        self.model = model 
        self.price = price
        self.fuel_type = fuel_type 
    def display(self):
        print("brand:",self.brand)
        print("model:",self.model)
        print("fuel_type:",self.fuel_type)
    def check_price(self):
        if self.price > 1000000:
            print("premium car")
        else:
            print("Normal car")
obj = Car("suzuki","pro",5000000,"petrol")
obj.display()
obj.check_price()

# Electricity bill
class ElectricityBill:
    def __init__(self,customer_name,units):
        self.customer_name = customer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            self.bill = self.units * 2
        elif self.units <= 200:
            self.bill = self.units * 3
        elif self.units <= 300:
            self.bill = self.units * 5
        else:
            self.bill = self.units * 7
    def display_bill(self):
        print("customer_name:",self.customer_name)
        print("units:",self.units)
        print("bills:",self.bill)
obj = ElectricityBill("geetha",543)
obj.calculate_bill()
obj.display_bill()

#Library book
class Book:
    def __init__(self,title,author,price,available):
        self.title=title
        self.author=author
        self.price=price
        self.available=available

    def display_book(self):
        print("title:",self.title)
        print("author:",self.author)
        print("price:",self.price)
        print("available:",self.available)
    def borrow_book(self):
        if self.available:
            self.available = False
            print("book borrowed successfully")
        else:
            print("book is not available")
    def return_book(self):
            self.available = True
            print("bokk retuned successfully")

obj = Book("python Basics","jhon",500,True)
obj.display_book()
obj.borrow_book()
obj.display_book()
obj.return_book()
obj.display_book()

#shipping cart
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def calculate_total(self):
        self.total = self.price * self.quantity
        print("total:",self.total)
    def display_products(self):
        print("name:",self.name)
        print("price:",self.price)
        print("quantity:",self.quantity)
        print("total:",self.total)
obj = Product("laptop",50000,1)
obj.calculate_total()
obj.display_products()
obj1 = Product("mouse",500,2)
obj1.calculate_total()
obj1.display_products()
obj2 = Product("keyboard",600,1)
obj2.calculate_total()
obj2.display_products()

# employee performance
class Employee:
    def __init__(self, name, salary, rating):
        self.name = name
        self.salary = salary
        self.rating = rating

    def display(self):
        # print name, salary, rating
        print("name:",self.name)
        print("salary:",self.salary)
        print("reting:",self.rating)
        pass

    def calculate_increment(self):
        # write if-elif-else here
        if self.rating >= 4.5:
            self.salary = self.salary * 0.20
        elif self.rating >= 3.5:
            self.salary = self.salary * 0.10
        else:
            if self.rating < 3.5:
                self.salary = self.salary * 0.05


        pass


obj = Employee("Geetha", 50000, 4.6)

obj.display()
obj.calculate_increment()

# Bank Account Validation
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # add amount to balance
        self.balance=self.balance+amount
        print("deposit money:",amount)

        pass

    def withdraw(self, amount):
        # check minimum balance rule
        if self.balance - amount >= 1000:
            self.balance -= amount
            print("widthdraw money:",amount)
        else:
            print("withdraw should not be allowed")
        pass

    def check_balance(self):
        # display account holder and balance
        print("name:",self.account_holder)
        print("balanace:",self.balance)
        pass


obj = BankAccount("Geetha", 5000)
obj.deposit(100)
obj.withdraw(6000)
obj.check_balance()

# online food order
class FoodOrder:
    def __init__(self, customer_name, food_name, price, quantity):
        self.customer_name = customer_name
        self.food_name = food_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        # price * quantity
        self.total = self.price * self.quantity
        print("total:",self.total)
        pass

    def apply_discount(self):
        # use if-elif-else
        if self.total >= 2000:
            self.discount =self.total * 0.20
           
        elif self.total >= 1000:
            self.discount = self.total * 0.10
            
        else:
            self.discount=0
        self.final_total = self.total - self.discount
        print("discount:",self.discount)
        print("final_total:",self.final_total)

        pass

    def display_order(self):
        # display order details
        print("customer_name:",self.customer_name)
        print("food_name:",self.food_name)
        print("price:",self.price)
        print("quantity:",self.quantity)
        print("total:",self.total)
        print("discount:",self.discount)
        print("final_total:",self.final_total)
        
        pass


obj = FoodOrder("Geetha", "Biryani", 500, 3)

obj.calculate_total()
obj.apply_discount()
obj.display_order()

# Hospital patient
class Patient:
    def __init__(self, name, age, disease, bill):
        self.name = name
        self.age = age
        self.disease = disease
        self.bill = bill

    def display_patient(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Bill:", self.bill)

    def add_bill(self, amount):
        self.bill = self.bill + amount
        print("Added Bill:", amount)

    def check_bill(self):
        print("Current Bill:", self.bill)


obj1 = Patient("Geetha", 21, "Fever", 5000)
obj2 = Patient("yegna", 30, "Cold", 3000)

obj1.display_patient()
obj1.add_bill(2000)
obj1.check_bill()

print()

obj2.display_patient()
obj2.add_bill(1000)
obj2.check_bill()

# Employee Attendance
class Employee:
    def __init__(self, name, total_days, present_days):
        self.name = name
        self.total_days = total_days
        self.present_days = present_days

    def attendance_percentage(self):
        # calculate attendance percentage
        self.attendance = self.present_days / self.total_days * 100
        print("attendance:",self.attendance)

        pass

    def check_attendance(self):
        # check whether employee is eligible
        if self.attendance >= 75:
            print("eligible")
        else:
            print("not eligible")   
        pass


obj = Employee("Geetha", 100, 80)

obj.attendance_percentage()
obj.check_attendance()

#Movie ticket booking
class MovieTicket:
    def __init__(self, movie_name, ticket_price, number_of_tickets):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.number_of_tickets = number_of_tickets

    def calculate_total(self):
        self.total = self.ticket_price * self.number_of_tickets
        print("Total:", self.total)

    def apply_discount(self):
        if self.number_of_tickets >= 5:
            self.discount = self.total * 0.10
        else:
            self.discount = 0

        self.final_total = self.total - self.discount
        print("Discount:", self.discount)
        print("Final Total:", self.final_total)

    def display_ticket(self):
        print("Movie Name:", self.movie_name)
        print("Ticket Price:", self.ticket_price)
        print("Number of Tickets:", self.number_of_tickets)
        print("Total:", self.total)
        print("Discount:", self.discount)
        print("Final Total:", self.final_total)


obj = MovieTicket("Avengers", 300, 5)

obj.calculate_total()
obj.apply_discount()
obj.display_ticket()

#student report card
class Student:
    def __init__(self, name, roll_no, python, sql, powerbi):
        self.name = name
        self.roll_no = roll_no
        self.python = python
        self.sql = sql
        self.powerbi = powerbi

    def calculate_total(self):
        self.total = self.python + self.sql + self.powerbi
        print("Total:", self.total)

    def calculate_average(self):
        self.average = self.total / 3
        print("Average:", self.average)

    def calculate_grade(self):
        if self.average >= 90:
            self.grade = "A"
        elif self.average >= 75:
            self.grade = "B"
        elif self.average >= 60:
            self.grade = "C"
        elif self.average >= 40:
            self.grade = "D"
        else:
            self.grade = "Fail"

        print("Grade:", self.grade)

    def display_report(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Python:", self.python)
        print("SQL:", self.sql)
        print("Power BI:", self.powerbi)
        print("Total:", self.total)
        print("Average:", self.average)
        print("Grade:", self.grade)


obj = Student("Geetha", 101, 85, 90, 80)

obj.calculate_total()
obj.calculate_average()
obj.calculate_grade()
obj.display_report()
