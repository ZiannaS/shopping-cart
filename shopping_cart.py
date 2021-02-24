# shopping_cart.py
import datetime
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import dotenv_values

# getting environmental variable values
config = dotenv_values(".env")
SENDGRID_API = config["SENDGRID_API_KEY"]
SENDER_ADDRESS = config["SENDER_ADDRESS"]
TAX_RATE = float(config["TAX_RATE"])



# list of available products in the Grocery store
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# function which takes in a file name and contents, creates the file and writes to it
def write_to_file(file_name, content):
    with open(file_name, "w") as file:
        file.write(content)


# convert numeric dollar value to string dollar value with $ and rounded to 2 d.p.
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71




my_cart = []
# Function which returns the product attributes based on a product id 
# Input: product_id
# Output: {id, name, department, aisle, price}
def find_product(product_id):
    for p in products: 
        if p["id"] == product_id:
            add_to_cart(p)
            return True     
    return False 

# adds a particular item to cart along with the price
def add_to_cart(p):
    name = p["name"]
    price = p["price"]
    my_cart.append((name, price))

# Creates a receipt from all items in the cart in a human readable format
# Checks whether the user has requested for an email receipt and emails the receipt to the user.
# Creates a txt file in the Receipts folder and adds a printabe receipt to that folder.
def output_bill(email_addr):
    now = datetime.datetime.now()  
    total = 0
    item_string = ""
    item_string_recpt = ""
    print("---------------------------------------")
    print("ZEE GROCERY")
    print("WWW.ZEEGROCERY.COM")
    print("---------------------------------------")
    print("CHECKOUT AT: ", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("---------------------------------------")
    print("SELECTED PRODUCTS")
    for item in my_cart:
        total += item[1]
        print('...', item[0], '(' + to_usd(item[1]) + ')')
        item_string += '<li> ' + item[0] + ' (' + to_usd(item[1]) + ')' + '</li>'
        item_string_recpt += item[0] + ' (' + to_usd(item[1]) + ')' + '\n'
    
    print("---------------------------------------")
    print("SUBTOTAL", to_usd(total))
    print("TAX", to_usd(total * TAX_RATE / 100 ))
    print("TOTAL", to_usd((total) + (total * TAX_RATE / 100)))
    print("---------------------------------------")
    print("THANKS, SEE YOU AGAIN!")
    print("---------------------------------------")

    email_receipt = "<h2> You Have Ordered </h2> <br /> Date " + now.strftime("%Y-%m-%d %H:%M:%S") + '<br />' + '<ol>' +item_string + '</ol>' + '<br />' "Sub Total: " + to_usd(total) + '<br />' + "Sales Tax: " + to_usd(total * TAX_RATE / 100 ) +'<br />' + "Total: " + to_usd((total) + (total * TAX_RATE / 100))
    if email_addr != None:
        send_email(email_receipt, email_addr)
    
    txt_recpt = 'You Have Ordered:' + '\n' + 'Date ' +  now.strftime("%Y-%m-%d %H:%M:%S") + '\n' + item_string_recpt + "Sub Total: " + to_usd(total) + '\n' + "Sales Tax: " + to_usd(total * TAX_RATE / 100 ) + '\n' + "Total: " + to_usd((total) + (total * TAX_RATE / 100))
    write_to_file("./Receipts/" + now.strftime("%Y-%m-%d-%H-%M-%S-%f"), txt_recpt)
    return

# Given the email address and email contents, sends an email to the user.
def send_email(html_content, email_addr):
    client = SendGridAPIClient(SENDGRID_API)
    subject = "Your Receipt from ZEE's Groceries"
    message = Mail(from_email=SENDER_ADDRESS, to_emails=email_addr, subject=subject, html_content=html_content)

    try:
        response = client.send(message)
        
        if int(response.status_code) == 202:
            print("Your receipt has been emailed to you!")
        else:
            print("There seems to be an error in emailing your receipt, we apologize for the inconvenience.")    
    except Exception as err:
        print("There seems to be an error in emailing your receipt, we apologize for the inconvenience.")

# Executing the automated checkout process
def main():
    print("CHECKOUT")
    print("Enter product ID's for whichever product you would like to purchase (1-20).")
    print("When you have scanned all your products, type 'DONE'. ")
    while True: 
        p_id = input("Please Enter A Product ID: ")
        if p_id == "DONE":
            while True:
                email_recpt = input("Would you like to receive an email_recipt (yes/no)? ")
                if email_recpt == "yes": 
                    email_addr = input("please input your email address: ")
                    output_bill(email_addr)
                    break
                elif email_recpt == "no":
                    output_bill(None)
                    break
                else:
                    print("Oops I did not understand that, please type (yes/no) ")
            return
        try:
            p_id = int(p_id)
            if not find_product(p_id):
                print("I am sorry, I do not recognize this ID, please try again or type DONE?")
        except: 
            print("I am sorry, I do not recognize this ID, please try again or type DONE?")

main()
