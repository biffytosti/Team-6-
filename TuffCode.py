'''
Program: TCU Lacrosse Store Cost Calculator
Program Developers: Trager Conard, Hayden Lunde, Biffy Tosti, and Camden Handwerger
Date: April 21, 2022
Purpose: Calculate the total order cost of an order for a TCU Lacrosse Store customer
Installation Instructions: Save this file and the accompanying TCU Lacrosse logo in the same folder
'''

from tkinter import *
from turtle import right # Import tkinter

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
        
        #Images for each clothing item
        photoShirt = PhotoImage(file=r'Shirt.gif')
        Label(window, image=photoShirt).grid(row = 1, column = 2, sticky = W)  
        photoLong = PhotoImage(file=r'LongSleeve.gif')
        Label(window, image=photoLong).grid(row = 1, column = 3, sticky = W) 
        photoHoodie = PhotoImage(file=r'Hoodie.gif')
        Label(window, image=photoHoodie).grid(row = 1, column = 4, sticky = W) 
        photoSweats = PhotoImage(file=r'Sweats.gif')
        Label(window, image=photoSweats).grid(row = 1, column = 5, sticky = W) 
        #For each of the three inputs, we created radio buttons and check buttons to select which product(s), color(s), and size(s)
        Label(window, text = 'Short Sleeve: $22').grid(row = 2, column = 2)
        Label(window, text = 'Long Sleeve: $30').grid(row = 2, column = 3)
        Label(window, text = 'Hoodie: $45').grid(row = 2, column = 4)
        Label(window, text = 'Sweat Pants: $40').grid(row = 2, column = 5)
        
        colorOptions = [
            "Black",
            "White",
            "Purple",
            "Grey"
        ]    
        
        HoodieColor = StringVar(window)
        ShirtColor = StringVar(window)
        PantsColor = StringVar(window)
        LongSleeveColor = StringVar(window)
        HoodieColor.set(colorOptions[0])
        ShirtColor.set(colorOptions[0])
        PantsColor.set(colorOptions[0])
        LongSleeveColor.set(colorOptions[0])
        OptionMenu(window, ShirtColor, *colorOptions).grid(row = 3, column = 2)
        OptionMenu(window, LongSleeveColor, *colorOptions).grid(row = 3, column = 3)
        OptionMenu(window, HoodieColor, *colorOptions).grid(row = 3, column = 4)
        OptionMenu(window, PantsColor, *colorOptions).grid(row = 3, column = 5)

        SizeOptions = [
            "XSmall",
            "Small",
            "Medium",
            "Large",
            "XLarge"
        ]    
        
        shirtSize = StringVar(window)
        LongSleeveSize = StringVar(window)
        HoodieSize = StringVar(window)
        pantsSize = StringVar(window)
        shirtSize.set(SizeOptions[0])
        LongSleeveColor.set(SizeOptions[0])
        HoodieSize.set(SizeOptions[0])
        pantsSize.set(SizeOptions[0])
        
        OptionMenu(window, shirtSize, *SizeOptions).grid(row = 4, column = 2)
        OptionMenu(window, LongSleeveSize, *SizeOptions).grid(row = 4, column = 3)
        OptionMenu(window, HoodieSize, *SizeOptions).grid(row = 4, column = 4)
        OptionMenu(window, pantsSize, *SizeOptions).grid(row = 4, column = 5)

        numProduct = [
            "0",
            "1",
            "2",
            "3",
            "4"
        ]    
        
        self.shirtNum = IntVar(window)
        self.LongSleeveNum = IntVar(window)
        self.HoodieNum = IntVar(window)
        self.pantsNum = IntVar(window)
        self.shirtNum.set(numProduct[0])
        self.LongSleeveNum.set(numProduct[0])
        self.HoodieNum.set(numProduct[0])
        self.pantsNum.set(numProduct[0])
        
        OptionMenu(window, self.shirtNum, *numProduct).grid(row = 5, column = 2)
        OptionMenu(window, self.LongSleeveNum, *numProduct).grid(row = 5, column = 3)
        OptionMenu(window, self.HoodieNum, *numProduct).grid(row = 5, column = 4)
        OptionMenu(window, self.pantsNum, *numProduct).grid(row = 5, column = 5)
        
        self.Subtotal = IntVar()
        self.Subtotal.set(0)
        Label(window, textvariable = self.Subtotal).grid(row = 6, column = 7, sticky = E)
        
        #For each of the two outputs, create a String variable and output each to a Label in the Window
        self.TaxAndShippingVar = StringVar()
        Label(window, textvariable = self.TaxAndShippingVar).grid(row = 7, column = 7, sticky = E)
        self.FinalPrice = StringVar()
        Label(window, textvariable = self.FinalPrice).grid(row = 8, column = 7, sticky = E)
        
        #Create a Compute Total Cost button to call the computeTotalCost function
        Button(window, text = "Compute Total Cost", command = self.computeTotalCost).grid(row = 9, column = 7, sticky = E)
        
        self.ShirtPrice = 22
        self.LongSleevePrice = 30
        self.HoodiePrice = 45
        self.PantsPrice = 40

        window.mainloop() # Create an event loop
        

    def getTaxAndShipping(self, Subtotal):
        #this function calculates a monthly payment based on the user data entered and returns the value of the monthly payment
        TaxAndShipping = (Subtotal * 0.0825) + 5
        return TaxAndShipping

    def computeTotalCost(self):
        #this function calls getMonthlyPayment function with the input values entered into the textboxed (Entry controls) and assigned to corresponding variables, 
        # after converting them to numerical values; after the monthly payment is returned, it is assigned to a variable for output in the window and 
        #total payment is calculated and assigned to a variable to output in the window
        self.Subtotal.set((self.ShirtPrice*self.shirtNum.get())+(self.LongSleeveNum.get()*self.LongSleevePrice)+(self.HoodieNum.get()*self.HoodiePrice)+(self.pantsNum.get()*self.PantsPrice))
        TaxAndShipping = self.getTaxAndShipping(
            int(self.Subtotal.get())
        )
        self.TaxAndShippingVar.set(format(TaxAndShipping, '10.2f'))
        FinalPrice = float(self.TaxAndShippingVar.get()) + int(self.Subtotal.get())
        self.FinalPrice.set(format(FinalPrice,'10.2f'))
      
OrderCostCalculator()  # Create GUI 
