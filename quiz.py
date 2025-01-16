import re

print(chr(ord('A')))  

print('----------------------------------------------------------------')
print(type(type(int)))

print('----------------------------------------------------------------')
y = 8
z = lambda x : x * y
print(z(6))


print("----------------------------------------------------------------")
s = 'horses are fast'

regex = re.compile(r'(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
matched = re.search(regex, s)

if matched:
    print(matched.groupdict())

print('--------------------------------')

li=[3, 4, 5, 20, 5, 25, 1, 3]
print(li.pop(1))
print(li)

# time.time()

def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        return x
    return inner

closure = outer()
print(closure())
print(closure())
