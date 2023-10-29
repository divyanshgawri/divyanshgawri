'''
class students:
    #constructors
    def __init__(self,roll_num,markslist,stream,percentage,grade,name):
        self.name = name

        self.roll_num= roll_num
        self.markslist = markslist
        self.stream = stream
        self.percentage = percentage
        self.grade = grade
        #roll number and name
    def nameandgrade(self,name,roll_num):
        self.name  = name
        self.roll_num = roll_num
        self.name = str(input("enter your name :"))
        self.roll_num=int(input("enter your roll number "))
        print("welcome mr/ms..",self,name)
        print("your roll number is ",self.roll_num)


        #marklist
    def get_numbers(self,markslist):
        self.markslist = markslist
        self.markslist = []
        for i in range(5):
            n= int(input("enter your number of subject respectively"))
            self.markslist.append(n)
    #streams
    def get_streams(self,stream,streams):
        self.stream = stream
        self.stream = streams
        self.streams = str(input("enter your stream (A--ARTS,C--COMMERCE,S--SCINECE):")).lower()
        if(self.streams == "a"):
            print("your stream is Arts")
        elif(self.streams=="c"):
            print("your stream is commerce")
        elif(self.streams == "s"):
            print("your stream is science")
        else:
            print("enter your valid stream")
    #percentage
    def percentage(self,percentage):
        self.percentage = percentage
        self.percentage = (sum(self.markslist)/5)*100
        print("your percentage is",self.percentage)
    #grade
    def gradebolte(self,grade):
        self.grade  = grade
        if(self.percentage>= 90):
            print("your grade is 'A'")
        elif(self.percentage<90 and self.percentage>=80):
            print("your grade is 'B'")
        elif(self.percentage<80 and self.percentage>=65):
            print("your grade is 'C' ")
        elif(self.percentage<65 and self.percentage>=40):
            print("your grade is 'D' ")
        else:
            print("beta tum shisha dekho grade nhi ")
class fere(students):
    print("your result is here \U0001F600")
c1 = fere()
c1.get_numbers(10)'''#doubt students class
'''
class student:
    def entery(self,name,roll_number,total_marks):
        self.name = name
        self.roll_num = roll_number
        self.total_marks = total_marks

    def enter(self):
        self.name = input("enter your name :")

        print("WELCOME MR/MS.",self.name)
    def pero(self):
        self.total_marks = int(input("enter your total marks :"))
        self.percentage = (self.total_marks/500)*100
        self.roll_num = int(input("enter your roll_num :"))
        print("YOUR ROLL NUMBER IS",self.roll_num)
        print("SO,YOUR TOTAL MARKS ARE ",self.total_marks)
        print("YOU GAINED THE PERCENTAGE OF",self.percentage)
class studenta(student) :
    print("hii student.")
s1  = studenta()
#s1.entery("divyansh gawri",2023010030913,450)
s1.enter()




s1.pero()'''#done small sudent class
'''
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        print("your coressponding value of x is", self.x)
        print("your coressponding value of y is",self.y)
        print("your coressponding value of x is", other.x)
        print("your coressponding value of y is", other.y)

        return point(x,y)
    def __str__(self):
        return str((self.x,self.y))
p1 = point(10,20)
p2 = point(50,60)
print("your respective values sum is ",p1 +p2)'''#done (x1+x) vala code
'''class Students:
    def __init__(self, name, rollnum):
        self.name = name
        self.rollnum = rollnum
        self.marklist = []

    def intro(self):
        print(f"Hello {self.name}, how are you? Your roll number is {self.rollnum}")

    def markslist(self):
        for i in range(5):
            c = int(input(f"Enter marks for subject {i + 1}: "))
            self.marklist.append(c)

    def calculate_percentage(self):
        total_marks = sum(self.marklist)
        percentage = total_marks / 5
        return percentage

    def calculate_grade(self, percentage):
        if percentage >= 90:
            return "A grade"
        elif 80 <= percentage < 90:
            return "B grade"
        else:
            return "C grade"

c1 = Students("divyansh", 2023010030913)
c1.intro()
c1.markslist()
percentage = c1.calculate_percentage()
grade = c1.calculate_grade(percentage)
print(f"You got a percentage of {percentage} and your grade is {grade}.")'''#gpt ala
'''class students:
    def __init__(self,name,rollnum):
        self.name = name
        self.rollnum = rollnum
        self.marklist = []
    def intro(self):
        print(f"helllo {self.name} welcome to resultt of yours...YOUR ROLL NUMBER IS  {self.rollnum}")
    def marklist(self):
        for i in range(5):
            c = int(input(f"enter your number of subject {i +1}"))
            self.marklist.append(c)
    def calculate_percentage(self):
        total_marks = sum(self.marklist)
        percentage = total_marks/5
        return percentage

    def calculate_grade(self, percentage):
        if percentage >= 90:
            return "A grade"
        elif 80 <= percentage < 90:
            return "B grade"
        else:
            return "C grade"
d1 = students("divyansh gawri",2030204)
d1.intro()
d1.marklist()
percentage = d1.calculate_percentage()
grade = d1.calculate_grade(percentage)
print(f"you got a percentage of{percentage} and grade of {grade}")'''#mere alaa
'''class bank:
    def __init__(self,name,accountnum,type,amount):
        self.name = name
        self.accountnum = accountnum
        self.type = type
        self.amount = amount
        x = self.amount
    def intro(self):
        print(f" welcome master/madam- {self.name}\n"
              f"your account number is- {self.accountnum}\n"
              ,
              f"your account is of type:{self.type}\n current balance is {self.amount}")

    def deposit(self):
        c = float(input("enter your amount to add"))
        x = self.amount
        print("this is new amount after addition",c+x)
    def withdrwal(self):
        x = self.amount
        v = float(input("enter your amount"))
        print("this is new amount after withdrwl",x-v)
b1 = bank("divyansh",23034934,"saving",4000000)
b1.intro()
b1.deposit()
b1.withdrwal()'''#bank wala dekhna payega
#alag h ye sab
'''a = input("enter your string :")
b = (a[::-1])
if (a == b ):
    print("yes!!!you coded well par salya yaad  rakhya kar")
else :
    print("kya baat krte ho bhai")'''#prblm -1(pailndrome checker)
'''def func(n):

    fact = 1
    for i in range(1,n+1):
        fact *=i
    print("your factorial is",fact)
n = int(input("enter number :"))
func(n)'''#func factorial
'''l= []
n = int(input("enter a number"))
for i in range(n):
    c = int(input("enter your elements"))
    l.append(c)
for nc in l:
    fact = 1
    for vc in range(1,nc+1):
        fact *=vc
    print(f"your factorial of {i +1} element",fact)'''#list aale factorial
''' class car :
    def model(self,model,price,company):
        self.model = model
        self.price = price
        self.company = company
        print("your model is",self.model)
        print("price of your car is",self.price)
        print("company of the car is",self.company)
c1 = car()
c1.model("sadiyyo puraaani",20000000,"alto")'''#car aala quesrtion


def calculate_tax(salary, donation):
    if salary <= 250000:
        return 0
    elif salary <= 500000:
        return (salary - 250000) * 0.05
    elif salary <= 750000:
        return 12500 + (salary - 500000) * 0.1
    elif salary <= 1000000:
        return 37500 + (salary - 750000) * 0.15
    elif salary <= 1250000:
        return 75000 + (salary - 1000000) * 0.2
    elif salary <= 1500000:
        return 125000 + (salary - 1250000) * 0.25
    else:
        return 187500 + (salary - 1500000) * 0.3


if __name__ == "__main__":
    salary = float(input("Enter your salary: "))
    donation = float(input("Enter the amount you donated or any other deductions: "))
    final_tax = calculate_tax(salary, donation)
    print(f"Your total taxable income after deductions: {salary - donation}")
    print(f"Your tax to be paid: {final_tax}")

