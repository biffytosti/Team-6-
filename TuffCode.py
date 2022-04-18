'''
Program: TCU Lacrosse Store Cost Calculator
Program Developers: Trager Conard, Hayden Lunde, Biffy Tosti, and Camden Handwerger
Date: April 21, 2022
Purpose: Calculate the total order cost of an order for a TCU Lacrosse Store customer
Installation Instructions: Save this file and the accompanying TCU Lacrosse logo in the same folder
'''

from distutils.command.config import config
from tkinter import * #import tkinter
from tkinter.ttk import *

window = Tk() # Create a window instance
window.title("Order Cost Calculator") # Set title of the window

class OrderCostCalculator():
    def __init__(self):
        # Our GUI application has three inputs and two outputs plus a Compute Payment Button, so we will need six rows and two columns
        photo = PhotoImage(file=r'TCULacrosse.gif') # specify the path to your file; the r prefix stands for "raw" string
        Label(window, image=photo).grid(row = 1, column = 1, sticky = W)  #put the image in a label to display it in the window

        # From Loan Calculator, THANKS! :)
        # First, create labels in the window for each input and output value.
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
        #The above and below code allows for a dropdown menu of the color options for each product
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
        #the above and below code allows for a dropdown menu of the sizes available for each product
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
        #the above and below code allows for a dropdown menu of the quantity available for each product
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
        Button(window, text = "Compute Total Cost", command = self.computeTotalCost).grid(row = 9, column = 6, sticky = E)
        
        #Create a 'Proceed to Payment and Delivery' button to move to the next window
        # Button(window, text = 'Proceed to Payment and Delivery', command = PayDelivWindow).grid(row = 9, column = 7, sticky = E)

        self.ShirtPrice = 22
        self.LongSleevePrice = 30
        self.HoodiePrice = 45
        self.PantsPrice = 40

        # window.mainloop() # Create an event loop


    def getTaxAndShipping(self, Subtotal):
        #this function calculates the tax and shipping by multiplying the subtotal cost by the sales tax rate in Texas, then adding the $5 shipping fee
        TaxAndShipping = (Subtotal * 0.0825) + 5
        return TaxAndShipping

    def computeTotalCost(self):
        #this function computes the total cost of the order by adding the different products and their respective prices together and then adding the tax and shipping fees associated with the purchase
        self.Subtotal.set((self.ShirtPrice*self.shirtNum.get())+(self.LongSleeveNum.get()*self.LongSleevePrice)+(self.HoodieNum.get()*self.HoodiePrice)+(self.pantsNum.get()*self.PantsPrice))
        TaxAndShipping = self.getTaxAndShipping(
            int(self.Subtotal.get())
        )
        self.TaxAndShippingVar.set(format(TaxAndShipping, '10.2f'))
        FinalPrice = float(self.TaxAndShippingVar.get()) + int(self.Subtotal.get())
        self.FinalPrice.set(format(FinalPrice,'10.2f'))

OrderCostCalculator()  # Create GUI

def PayDelivWindow():
        PayDeliv = Tk()
        PayDeliv.title = 'Payment and Delivery Method'
        Label(PayDeliv, text = "Select Delivery Method:").grid(row = 2, column = 1, sticky = W)
        Radiobutton(PayDeliv, text = "Pickup").grid(row = 2, column = 2, sticky = W)
        Radiobutton(PayDeliv, text = "Ship to Address").grid(row = 2, column = 3, sticky = W)
        Label(PayDeliv, text = "Enter Payment Information Below:").grid(row = 3, column = 1, sticky = W)
        Entry(PayDeliv, text = "Credit Card Number").grid(row = 4, column = 1, sticky = W)
        Entry(PayDeliv, text = "Name on Card").grid(row = 4, column = 2, sticky = W)
        Entry(PayDeliv, text = "Expiration Date").grid(row = 5, column = 1, sticky = W)
        Entry(PayDeliv, text = "Security Code/CVC").grid(row = 5, column = 2, sticky = W)
        PayDeliv.mainloop()
        
Button(window, text = 'Proceed to Payment and Delivery', command = PayDelivWindow).grid(row = 9, column = 7, sticky = E)       

mainloop()