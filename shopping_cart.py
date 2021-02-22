# shopping_cart.py
import datetime

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


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

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

def add_to_cart(p):
    name = p["name"]
    price = p["price"]
    my_cart.append((name, price))

def output_bill():
    now = datetime.datetime.now()
    tax = 8.75
    total = 0
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
    
    print("---------------------------------------")
    print("SUBTOTAL", to_usd(total))
    print("TAX", to_usd(total * 8.75 / 100 ))
    print("TOTAL", to_usd((total) + (total * 8.75 / 100)))
    print("---------------------------------------")
    print("THANKS, SEE YOU AGAIN!")
    print("---------------------------------------")
    return

def main():
    print("CHECKOUT")
    print("Enter product ID's for whichever product you would like to purchase.")
    print("When you have scanned all your products, type 'DONE'. ")
    while True: 
        p_id = input("Please Enter A Product ID: ")
        if p_id == "DONE":
            output_bill()
            return
        try:
            p_id = int(p_id)
            if not find_product(p_id):
                print("I am sorry, I do not recognize this ID, please try again or type DONE?")
        except: 
            print("I am sorry, I do not recognize this ID, please try again or type DONE?")

main()