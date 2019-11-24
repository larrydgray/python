
for num in range(1,33):
    count=1
    if(num%2==0):
        count+=1
    if(num%4==0):
        count+=1
    if(num%8==0):
        count+=1
    if(num%16==0):
        count+=1
    print(str(num)+' '+str(count))
