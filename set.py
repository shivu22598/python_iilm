#1
s={"C","C++","Java","Python"}
print(s)
#2
s1={"Shivani",20,"Female"}
print(s1)
#3
print(type(s1))
#4
thisset={"Java","Python","Django"}
if "Python" in thisset:
    print("Present")
else:
    print("Not Present")
#5
thisset={"Java","Python","SQL"}
secondset={"C","Cpp","NoSQL"}
print(thisset.union(secondset))
#6
thisset={"Python","Django","JavaScript"}
mylist=["Java","C"]
print(thisset.union(mylist))
#7
thisset={"Python","Django","JavaScript","SQL"}
thisset.remove("SQL")
print(thisset)
#8
thisset.clear()
print(thisset)
#9
thisset={"Python","Django","JavaScript","SQL"}
for x in thisset:
    print(x)
#10
s={10,23,77,81,2}
print(max(s))
print(min(s))