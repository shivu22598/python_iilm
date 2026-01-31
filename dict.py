d={"name":"Shivani","age":20,"gender":"Female"}
print(d)
#2
print(d.get("name"))
print(d.get("age"))
print(d.get("gender"))
#3
lst=list[d.values()]
print(lst)
#4
d.update({"age":21})
print(d)
#5
print(d.keys())
#6
student = {
    "student1": {
        "name": "Shivani",
        "age": 21
    },
    "student2": {
        "name": "Amit",
        "age": 22
    },
    "student3": {
        "name": "Neha",
        "age": 20
    }
}

print(student)
#7
d1={"name":"Amit","age":22}
d2={"name":"Neha","age":20}
student={"student1":d,"student2":d1,"student3":d2}
print(student)
#8
lst=["name","age","gender","city"]
lst1=["Shivani",21,"Female","Greater Noida"]
d={lst[i]:lst1[i]for i in range (len (lst))}
print(d)
#9
merge_dct={**d1,**d2}
print(merge_dct)
#10
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
print(min(sample_dict, key=sample_dict.get))