def duplicacy(list):
    n=len(list)
    for i in range(n):
        for j in range(i+1,n):
            if list[i]==list[j]:
                return True
    return False
list=[2,7,9,4,5,6,2,3,7]
print(duplicacy(list))    
    