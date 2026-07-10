#w: open for truncationg the file first.i.e it overwrite if something is already there in file.
# +: open for updatating (reading and writing)


# f=open("demo.txt", "rt")
# data=f.read(5) #reads entire file
# line1=f.readline() # reads line by line
# print(data)
# print(type(data))
# f.close()

# f=open("demo.txt", "r+")
# f.write("what")
# print(f.read())

# with open("demo.txt", "r") as f:
#     data=f.read()
#     print(data)

# with open("demo.txt", "w") as f:
#     new_data= f.write("new data ")
#     print(new_data)

#Deleting a File


# with open("hello.txt", "r") as f:
#     data=f.read()

# new_data=data.replace("Java", "Python")
# print(new_data)

# with open("hello.txt", "w") as f:
#     f.write("new_data")

# with open("hello.txt", "r") as f:
#     data=f.read()
#     if (data.find("learning")!=-1):
#         print("Found")
#     else:
#         print("notfound 404!")

# def check_for_line():
#     word="learning"
#     data=True
#     line_no=1
#     with open("hello.txt", "r") as f:
#         while data:
#             data=f.readline()
#             if (word in data):
#                 print(line_no)
#             line_no+=1

# check_for_line()
count=0
with open("number.txt", "r") as f:
    data=f.read()

    num=data.split(",")
    for val in num:
        if (int(val)%2==0):
            count+=1

print(count)

