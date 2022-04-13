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
        Label(window, text = "Subtotal Cost").grid(row = 6, column = 1, sticky = W)
        Label(window, text = "Shipping and Tax").grid(row = 7, column = 1, sticky = W)
        Label(window, text = "Total Cost").grid(row = 8, column = 1, sticky = W)
        
        #For each of the three inputs, we created radio buttons and check buttons to select which product(s), color(s), and size(s)
        self.ProductVar = IntVar()
        Radiobutton(window, text = 'Short Sleeve: $22', variable = self.ProductVar, value = 'ShortSleeve', justify = CENTER).grid(row = 2, column = 2)
        Radiobutton(window, text = 'Long Sleeve: $30', variable = self.ProductVar, value = 'LongSleeve', justify = CENTER).grid(row = 2, column = 3)
        Radiobutton(window, text = 'Hoodie: $45', variable = self.ProductVar, value = 'Hoodie', justify = CENTER).grid(row = 2, column = 4)
        Radiobutton(window, text = 'Sweat Pants: $40', variable = self.ProductVar, value = 'SweatPants', justify = CENTER).grid(row = 2, column = 5)
        self.ColorVar = IntVar()
        Radiobutton(window, text = 'Black', variable = self.ColorVar, value = 'Black',  justify = CENTER).grid(row = 3, column = 2)
        Radiobutton(window, text = 'White', variable = self.ColorVar, value = 'White', justify = CENTER).grid(row = 3, column = 3)
        Radiobutton(window, text = 'Purple', variable = self.ColorVar, value = 'Purple', justify = CENTER).grid(row = 3, column = 4)
        Radiobutton(window, text = 'Gray', variable = self.ColorVar, value = 'Gray', justify = CENTER).grid(row = 3, column = 5)
        self.Size = IntVar()
        Radiobutton(window, text = 'XS', variable = self.Size, value = 'XS', justify = CENTER).grid(row = 4, column = 2)
        Radiobutton(window, text = 'S', variable = self.Size, value = 'S', justify = CENTER).grid(row = 4, column = 3)
        Radiobutton(window, text = 'M', variable = self.Size, value = 'M', justify = CENTER).grid(row = 4, column = 4)
        Radiobutton(window, text = 'L', variable = self.Size, value = 'L', justify = CENTER).grid(row = 4, column = 5)
        Radiobutton(window, text = 'XL', variable = self.Size, value = 'XL', justify = CENTER).grid(row = 4, column = 6)
        self.Quantity = IntVar()
        Entry(window, textvariable = self.Quantity, justify = CENTER).grid(row = 5, column = 7)
        self.Subtotal = IntVar()
        Entry(window, textvariable = self.Subtotal, justify = CENTER).grid(row = 6, column = 7)
        
        #For each of the two outputs, create a String variable and output each to a Label in the Window
        self.TaxAndShippingVar = StringVar()
        Label(window, textvariable = self.TaxAndShippingVar).grid(row = 7, column = 7, sticky = E)
        self.FinalPrice = StringVar()
        Label(window, textvariable = self.FinalPrice).grid(row = 8, column = 7, sticky = E)
        
        #Create a Compute Total Cost button to call the computeTotalCost function
        Button(window, text = "Compute Total Cost", command = self.computeTotalCost).grid(row = 9, column = 7, sticky = E)
        
        window.mainloop() # Create an event loop
        
    def getTaxAndShipping(self, Subtotal):
        #this function calculates a monthly payment based on the user data entered and returns the value of the monthly payment
        TaxAndShipping = (Subtotal * 0.0825) + 5
        return TaxAndShipping

    def computeTotalCost(self):
        #this function calls getMonthlyPayment function with the input values entered into the textboxed (Entry controls) and assigned to corresponding variables, 
        # after converting them to numerical values; after the monthly payment is returned, it is assigned to a variable for output in the window and 
        #total payment is calculated and assigned to a variable to output in the window
        TaxAndShipping = self.getTaxAndShipping(
            int(self.Subtotal.get())
        )
        self.TaxAndShippingVar.set(format(TaxAndShipping, '10.2f'))
        FinalPrice = float(self.TaxAndShippingVar.get()) + int(self.Subtotal.get())
        self.FinalPrice.set(format(FinalPrice,'10.2f'))
      

OrderCostCalculator()  # Create GUI 