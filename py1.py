str = "123456abc"

list1 = list(str)
print(list1)

num = range(6)
sum = 0
for i in num:
    sum += i

print(sum)

obj1 = [1,2,3,4,5,6]
obj2 = {"1":1, "2":2, "3":3, "4":4, "5":5}
obj3 = (1,2,3)
def lens(object):
    if(len(object) >= 5):
        print("True")
    else:
        print("False")
lens(obj1)
lens(obj2)
lens(obj3)