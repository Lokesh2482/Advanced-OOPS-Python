# lst = [1,2,3]
# my_str = "MLOps playlist"
# my_int = 155

# #print(type(my_int))
# my_str.capitalize()
# print(my_str)

# a = 'x'
# b = 'y'
# print(a+b)

from oops_proj import chatbook

# user1 = chatbook()
# lst = [1,2,3]

# #function
# a1 = len(lst)
# print(a1)

#calling a method
# create a class and then using dot operator call the method
user1 = chatbook()
print(user1.id)

#Using static method directly from class rather than object
chatbook.set_id(10)

user2 = chatbook()
print(user2.id)
user3 = chatbook()
print(user3.id)
#getter and setter
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())
#print(user1.__name)(you cant access like this)

#To access encapsulated attributes:
#print(user1._chatbook__name)