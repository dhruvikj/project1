#####################
L1 = []
for i in range(5):
    x = int(input('number for list:-'))
    L1.append(x)
print('L1',L1)

D =0
L2 =[]
for i in range(5):
    x = int(input('number for list:-'))
    L2.insert(D,x)
    D +=1
print('L2',L2)
##############
T1 = tuple(L1)
T2 = tuple(L2)
print(T1)
print(T2)
""" AFTER ADDING 90 AND 100 IN T1"""
T1 += (90,100)
print('AFTER ADDING 90 AND 100 IN T1:-',T1)
""" DETERMINING THE LENGTH OF THE TUPLE"""
print('DETERMINING THE LENGTH OF THE TUPLE:-',len(T2))
###############
Dict2 = {11: 'PDPU', 22: 'Gandhinagar', 33: 'Gujarat',44: 'India'}
print('\nDictionary with the use of integer keys:')
print(Dict2)
key = int(input('input the key number from above dictionary'))
del(Dict2[key])
print('after deleting the key',Dict2)
