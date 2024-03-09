# Python Program to Update
# character of a String

String1 = "Hello, I'm a uzair"
print("Initial String: ")
print(String1)

#1
list1 = list(String1)
list1[2] = 'n'
String2 = ''.join(list1)
print("\nUpdating character at 2nd Index: ")
print(String2)

#2
String3 = String1[0:2] + 'm' + String1[3:]
print(String3)
