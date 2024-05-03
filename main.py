#task_1
def list1(lst1):
    lstp1 = []
    for x in lst1:
        pass

        return lstp1


print(list1(["1", "3", "3.6"]))
print(list1(["9.4", "4.2"]))
print(list1(["91", "44"]))
print(list1(["9.5", "8.8"]))
print("\n")



#task_2
print("oxirgi index boshiga chiqarish:")
def list2(lst2):
    lstp2 = []
    x = lst2.pop(4)
    lstp2.append(x)
    lstp2.extend(lst2)
    return lstp2

print(list2([1,2,3,4,5]))
print(list2([6,5,8,9,7]))
print(list2([20,15,26,8,4]))
print("\n")



#task_3
print("3 ta listning birinchi indexni yig'indisi: ")
def list3(lst3a,lst3b,lst3c):
    lstp3 = []
    a = lst3a.pop(0)
    b = lst3b.pop(0)
    c = lst3c.pop(0)
    lstp3.append(a)
    lstp3.append(b)
    lstp3.append(c)

    return sum(lstp3)

print(list3([1,2,3,4,5],[5,6,7,8,9],[20,21,34,56,100]))
print("\n")
