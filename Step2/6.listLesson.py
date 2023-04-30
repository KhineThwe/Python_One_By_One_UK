#sort
amazon_cart = ['smart tv', 'earphone', 'sunglasses', 'toys', 'grapes', 'Book', 'chicken', 'beef', 'pork']
# amazon_cart.sort()
# print(amazon_cart)#ascending order ငယ်စဉ်ကြီးလိုက်
#
# amazon_cart.sort(reverse=True)#descending order ကြီးစဉ်ငယ်လိုက်
# print(amazon_cart)

#length
def myFun(e):
    return len(e)

amazon_cart.sort(key=myFun)
print("Sorting according to length of the item: ")
print(amazon_cart)

#smart tv ----> 7
#amazon_cart  = ['smart tv','earphone','sunglasses']