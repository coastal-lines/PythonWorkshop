x = "My name is Agent Smith"
print(x[3:16:3]) #nesgt

s = "hello"
ascii = s.encode("ascii")
utf8 = s.encode("utf8")
utf16 = s.encode("utf16")

str_in_bytes = b"hello"


str = "hello"
#str[0] = "r"

strBa = bytearray(b"hello")
strBa[0] = 97
print(strBa)

result = strBa.decode("utf-8") 
print(result)

jpeg = [99, 97, 96, 0]
with open(r"jpeg.jpeg", "w+b") as file:
    file.write(bytes(jpeg))

with open(r"jpeg.jpeg", "rb") as file:
    data = file.read()
    for b in data:
        print(int(b))