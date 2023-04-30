# string1 = "Hello"
#         # 0 1 2 3 4
# string1[0] = "h"
# print(string1)
# #string ---> immutable ---> can't modify
# #'str' object does not support item assignment

amazon_cart = ['notebooks','sunglasses','toys','grapes']

# print(amazon_cart[::-1])
#list ---> mutable ---> can modify
amazon_cart[0] = 'earphone'#overwrite
print(amazon_cart)

#list methods
#adding
#1.append method
amazon_cart.append("Book")#doesn't return
print(amazon_cart)

#extend method
#ရှိပြီးသား list ထဲမှာ list တစ်ခုကိုထပ်ပေါင်းထည့်ခြင်း
new_amazon_cart = ["chicken","beef","pork"]
amazon_cart.extend(new_amazon_cart)
print(amazon_cart)

#insert method
amazon_cart.insert(0,"smart tv")
print(amazon_cart)


