no=[1,2,3,4,5,6,7,8,9]
counte=0
counto=0
for i in range(1,len(no)-1):
    if no[i]%2==0:
         counte+=1
         
    else:
        counto+=1
        
print("event count",counte)
print("odd count",counto)