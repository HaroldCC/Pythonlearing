'''
2-3
name = "Eric"
print("Hello "+ name + ", would you like to learn some python today?")
'''
'''
2-4
name = "Cheng Rong"
print(name.title())
print(name.lower())
print(name.upper())
'''
'''
2-5
name = "albert einstein"
#记住单双引号巧妙换着用
word = '"A person who never made a mistake never tried anything new."'
print(name.title() + " once said," + word)
'''
'''
2-6
famous_person = "albert einstein"
word = '"A person who never made a mistake never tried anything new "'
message = famous_person.title() + " once said," + word
print(message)
'''
'''
2-7
name = "\talbert einstein\n"
print(name)
print(name.lstrip())       #删除前空白（左l）
print(name.rstrip())       #删除后空白（右r）
print(name.strip())        #删除前后空白
'''
'''
2-8
print(5 + 3)
print(10 - 2)
print(2 * 4)
print(8 / 1)                  #??????????/
'''
'''
2-9
digtal = 40
message = "My favorite number is "
print(message + str(digtal) + "!")
'''