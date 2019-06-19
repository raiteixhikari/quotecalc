##### Renewal Calculation Function ##### START #####
def rcalc(discount,reinstatement,renewal,late,latediscount):
    conv=round(((reinstatement + renewal) * exchange),2)
    rnd=round(((discount) / 100),2)
    disc=round((rnd) * (conv) ,2)
    final=round((conv) - (disc),2)
    print("Original Price is %.2f" % (conv))
    print("Final Price is %.2f" % (final))
    lateconv=round(((late) * exchange),2)
    laternd=round(((latediscount) /100),2)
    latedisc=round((laternd) * (lateconv),2)
    latefinal=round((lateconv) - (latedisc),2)
    print("Late Fee is %.2f" % (latefinal))

##### Renewal Calculation Function ##### END #####


##### New Purchase Calculation Function ##### START #####

##### COMING SOON #####

##### New Purchase Calculation Function ##### END #####



##### Select Quotation Type which will then invoke Renewal or New Purchase Function ########################## START ####

def option():
    print("1: Renewal")
    print("2: New Purchase")
    select = str(input("Select Your Choice - press q to quit"))
    if select is '1':
        rcalc(discount,reinstatement,renewal,late,latediscount)
        print("All Prices stated here are in RM")
    if select is '2':
        noption()
    if select is 'q':
        exit()
    else:
        input("Invalid Input,press any key to return to menu")
        option()

##### Select Quotation Type which will then invoke Renewal or New Purchase Function ########################## END ####



##### Initial Data Input which will lead to Quotation Selection Function ############################ START ####


reinstatement = float(input("Please enter Reinstatement amount : "))
print("Reinstatement is %.2f USD" % (reinstatement))
late = float(input("Please enter Late Fee : "))
print("Late Fee is %.2f USD" % (late))
renewal = float(input("Please enter Renewal Amount : "))
print("Renewal Amount is %.2f USD" % (renewal))
exchange = float(input("Please enter Exchange Rate :"))
print("Exchange Rate is %.2f" % (exchange))
discount = float(input("Please enter Discount percentage : "))
print("Discount percentage is %.2f" % (discount))
latediscount = float(input("Please enter Late Fee discount :"))
print("Late Fee discount is %.2f" % (latediscount))


#####  Function ################################################################## START ####

option()

##### Quotation Selection Function ################################################################## END ####

##### Initial Data Input which will lead to Quotation Selection Function ############################ END ####
