import os, string

#TASK 1

# path = input()
# print("Directories: ")
# for x in os.listdir(path):
#     if os.path.isdir(os.path.join(path, x)):
#         print(x)
# print("\nFiles: ")
# for y in os.listdir(path):
#     if os.path.isfile(os.path.join(path, y)):
#         print(y)
# print("\nAll Directories and Files: ")
# for index, folder,file in os.walk(path):
#     for i in folder:
#         print(os.path.join(index, i))
#     for j in file:
#         print(os.path.join(index, j))

#TASK 2

# path = input()
# print(path)
# print(f"Reading: {os.access(path, os.R_OK)}")
# print(f"Writing: {os.access(path, os.W_OK)}")
# print(f"Executability: {os.access(path, os.X_OK)}")
# print(f"Existance: {os.path.exists(path)}")

#TASK 3

# path = input()
# def check(path):
#     if os.access(path, mode=os.EX_OK):
#         return os.listdir(path)
#     else:
#         return False
# print(check(path))

#TASK 4

# with open('sometext.txt', 'r') as file:
#     x = sum(1 for line in file)
# print(f"Total lines: {x}")

#TASK 5

# listik = list(input().split())
# with open('example.txt', 'w') as x:
#     for i in listik:
#         x.write(str(i) + ' ')

#TASK 6
# for ch in string.ascii_uppercase:
#    with open(f"task6/{ch}.txt", 'w'):
#         pass

#TASK 7
# with open('sometext.txt', 'r') as r:
#     with open('copyof.txt', 'w') as w:
#         for line in r:
#             w.write(line)

#TASK 8
# path = input()
# if os.path.exists(path):
#     os.remove(path)