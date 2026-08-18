list=["Ahishek",1232]
print(list)

list.append(1)
print(list)

list.insert(2,5)
print(list)

list[2]=10    #//update method
print(list)

list.extend(["A,M,P,K"])
print(list)

list[4]        #//index method Accesing element
print(list[4])

list.remove(1232)   #// remove element method ,list
print(list)

list.pop()
print(list)      #// last delete

del list[1]    #//start form the sequnce(01234)=abhi=0,10=1
print(list)

print(len(list))    #//list len find

if 1 in list:
    print("Element is present")


for i in list:
    print(i)

list.count("Abhishek")
print(list.count("Abhishek"))  

list.index(1)
print(list.index(1))


list2=[5,3,7,1,9,2]
list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)

list2.reverse()
print(list2)

list.clear()
print(list)

list3=list2.copy()
print(list3)