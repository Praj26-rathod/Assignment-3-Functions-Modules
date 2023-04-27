dic = {
    
}
key = "a"
value = ord(key)

for i in range(0,26):
    dic[chr((value)+i)] = value + i

print(dic)