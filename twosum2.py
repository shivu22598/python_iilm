def twosum(num,t):
    x=0
    while(x<len(num)):
        z=x+1
        while(z<len(num)):
            if (t == num[x]+num[z]):
                return[x,z]
            z+=1
        x+=1           
nums=[12,7,8,13,9]
t=20
result=twosum(nums,t)   
print(result)         