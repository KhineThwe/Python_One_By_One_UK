ls = [1,2,3,4]
ls.append(5)#နောက်ဆုံးမှာ data ထည့်ခြင်း
print(ls)

#ls = [1,2,3,4,5]
#      0 1 2 3 4
#index no နဲ့ထည့်လို့ရတယ်။
ls.insert(2,77)#index no , data
print(ls)

#ls = [1,2,77,3,4,5]
#      0 1  2 3 4 5
ls.insert(4,88)
print(ls)

#ls = [1,2,77,3,88,4,5]
ls.append(888)
print(ls)
#ls = [1,2,77,3,88,4,5,888]

ls.insert(5,1000)
print(ls)
#ls = [1,2,77,3,88,100,4,5,888]

ls.insert(4,444)
print(ls)

#ls = [1,2,77,3,444,88,1000,4,5,888]


