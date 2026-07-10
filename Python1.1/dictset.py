#Dictionary: They are unordered, mutable(changeable) &don't allow duplicate keys.

# info={
#     "name": "kk",
#     "subjects": ["c", "C++", "Python"],
#     "topics": ("dict", "set"),
#     "name":"kathmandu",
#     "age":21,
#     "gender":"Female",
#     12.11: 56.4,
#     ('HI'): ("hello")
# }

# print(len(list(info.keys())))
# print(info.values())
# print(info.items())

# print(info["subjects2"])#error
# print(info.get("subjects"))

#nestedDictionary: dictionary inside dictionary.

# new_dict= {"City": "Lalitpur"}
# info.update(new_dict)
# print(info)

#Set in Python
#set is the collection of the unordered items.
#Each element in the set must be unique and immutable.

#repeated elements stored only once , so it resolved to {1,2}
# we can add boolean, int, float, str, tuple but not list and dictionary

# collection={1,2,3,4,"hello", "world", "world", "hello",4.78}
# print(collection)
# print(type(collection))
# print(len(collection))

# collection=set() #empty set syntax
# print(type(collection))

# collection.add("hello")
# collection.add("world")
# collection.add(2)
# collection.add(5)
# collection.remove("hello")
# collection.clear()
# collection.add(9)
# print(collection.pop())
# set1={1,2,3}
# set2={3,4,5}
# print(set1.union(set2))
# print(set1)
# print(set2)
# print(set2.intersection(set1))"
# subjects={"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
# print(len(subjects))
# mark1=int(input("Enter mark of Physics: "))
# mark2=int(input("Enter marks of chemistry: "))
# mark3=int(input("Enter marks of Mathematics: "))
# dict={}
# new_dict={"Physics": mark1, "Chemistry": mark2, "Mathematics": mark3}
# dict.update(new_dict)
# print(dict)
# a=str(9)
# b=str(9.0)
# set1={a,b}
# print(set1)
# values={
#     ("float", 9.0),
#     ("int", 9),
# }
# print(values)

