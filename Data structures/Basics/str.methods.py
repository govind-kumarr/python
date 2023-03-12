# how to get stubstr

txt = "Hello World!"
# * Task to get world out of txt
print(txt[6:12])

txt = "   hello world!  "
# * Task To return str whithout whitspaces
print(txt.strip() + "p")


txt = "hello world"
# * To convert txt to uppercase
print(txt.upper())


txt = "hello world"
# * To convert txt to lowercase
print(txt.lower())


txt = "Hello world"
# * To Replace the char H in txt to J
print(txt.replace("H", "J"))


#! Format function in Python
txt = "For only {price:.2f} dollars!"
# print(txt)
print(txt.format(price=49))


txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {} {} {}".format("John", 36, "male", "trying")

print(txt1)
print(txt2)
print(txt3)
