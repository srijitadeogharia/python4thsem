items = [] # list of items(fruits)
n=int(input("enter no. of items"))

for i in range(n):
    fruitName= input("enter name of fruits")
    PricePerUnit = int(input("enter price per unit"))
    quatity = int(input("enter quantity"))

    fruitsDetails = {"name":fruitName , "price":PricePerUnit , "quantity":quatity}
    items.append(fruitsDetails)

print(items)


def mostExpensive():
    highest = 0 #storing the price of expensive item
    highItem = " " #store the name of exp. item

    for i in items:  #for i in range(len(items))
        p = i.get("price")
        q = i.get("quantity")
        sp = p*q
        if( sp > highest ):
            highest = sp
            highItem = i.get("name")
    print("expesive fruit is",highItem)

# Function to calculate total selling price of all items
def totalSellingPrice():
    total = 0
    for i in items:
        p = i.get("price")
        q = i.get("quantity")
        sp = p * q
        total += sp
    print("Total selling price of all items is:", total)

# Function to calculate average selling price per item
def averageSellingPrice():
    total = 0
    for i in items:
        p = i.get("price")
        q = i.get("quantity")
        sp = p * q
        total += sp
    
    avg = total / len(items) if len(items) > 0 else 0
    print("Average selling price per item is:", avg)

# Calling the functions
mostExpensive()
totalSellingPrice()
averageSellingPrice()



