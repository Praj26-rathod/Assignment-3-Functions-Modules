list1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for j in range(0,len(list1)-1):
    for i in range(0,len(list1)-1):
    
        firstVal=list1[i]
        secondVal=list1[i+1]
        if firstVal[1]>secondVal[1]:
            temp=list1[i]
            list1[i]=list1[i+1]
            list1[i+1]=temp
print(list1)