'''
Program: TCU Lacrosse Store Cost Calculator
Program Developers: Trager Conard, Hayden Lunde, Biffy Tosti, and Camden Handwerger
Date: April 21, 2022
Purpose: Calculate the total order cost of an order for a TCU Lacrosse Store customer
Installation Instructions: Save this file and the accompanying TCU Lacrosse logo in the same folder
'''

from tkinter import * # Import tkinter

class OrderCostCalculator:
    def __init__(self):
        window = Tk() # Create a window instance
        window.title("Order Cost Calculator") # Set title of the window

        # Our GUI application has three inputs and two outputs plus a Compute Payment Button, so we will need six rows and two columns
        photo = PhotoImage(file=r'TCULacrosse.gif') # specify the path to your file; the r prefix stands for "raw" string
        Label(window, image=photo).grid(row = 1, column = 1, sticky = W)  #put the image in a label to display it in the window
        
        # From Loan Calculator, THANKS! :)
        # First, create labels in the window for each input and output value. Note they are put into a grid with rows and columns
        Label(window, text = "Select Product").grid(row = 2, column = 1, sticky = W)
        Label(window, text = "Select Color").grid(row = 3, column = 1, sticky = W)
        Label(window, text = "Select Size").grid(row = 4, column = 1, sticky = W)
        Label(window, text = "Select Quantity").grid(row = 5, column = 1, sticky = W)
        Label(window, text = "Loan Amount").grid(row = 6, column = 1, sticky = W)
        Label(window, text = "Monthly Payment").grid(row = 7, column = 1, sticky = W)
        Label(window, text = "Total Payment").grid(row = 8, column = 1, sticky = W)
        
        #For each of the three inputs, create string variable and get their values through Entry control
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 2, column = 2)
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable = self.numberOfYearsVar, justify = RIGHT).grid(row = 3, column = 2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar, justify = RIGHT).grid(row = 4, column = 2)
        
        #For each of the two outputs, crete a String variable and output each to a Label in the Window
        self.monthlyPaymentVar = StringVar()
        Label(window, textvariable = self.monthlyPaymentVar).grid(row = 5, column = 2, sticky = E)
        self.totalPaymentVar = StringVar()
        Label(window, textvariable = self.totalPaymentVar).grid(row = 6, column = 2, sticky = E)
        
        #Create a Compute Payment button to call the computePayment function
        Button(window, text = "Compute Payment", command = self.computePayment).grid(row = 7, column = 2, sticky = E)
        
        window.mainloop() # Create an event loop
        
    def getMonthlyPayment(self,loanAmount, monthlyInterestRate, numberOfYears):
        #this function calculates a monthly payment based on the user data entered and returns the value of the monthly payment
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment

    def computePayment(self):
        #this function calls getMonthlyPayment function with the input values entered into the textboxed (Entry controls) and assigned to corresponding variables, 
        # after converting them to numerical values; after the monthly payment is returned, it is assigned to a variable for output in the window and 
        #total payment is calculated and assigned to a variable to output in the window
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()), 
            float(self.annualInterestRateVar.get()) / 1200, 
            int(self.numberOfYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
            * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))


OrderCostCalculator()  # Create GUI 