""" Project-1
Purpose:- To build a system to help speed up the process of creating receipts for customers in Lovely Loveseat furniture company"""

#Create a variables
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""
lovely_loveseat_price = 254.00
stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
stylish_settee_price = 180.50
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""
luxurious_lamp_price = 52.15
sales_tax = 0.088

#The 1st customer haven’t purchased anything yet, let’s set that variable equal to 0 for now.
customer_one_total = 0

#The list of discription of things they're purchasing
customer_one_itemization = ""
#The customer decide to purchase Lovely Loveseat!,Luxurious Lamp!, we update customer_one_ total & description
customer_one_total += 254.00 + 52.15
customer_one_itemization += lovely_loveseat_description + luxurious_lamp_description
#Calculate salse tax
customer_one_tax = customer_one_total * sales_tax
#updaten customer_one_total
customer_one_total += customer_one_tax
#Printing recipt
print ("Customer One Items:")
print (customer_one_itemization)
print ("Customer One Total:")
print (customer_one_total)
