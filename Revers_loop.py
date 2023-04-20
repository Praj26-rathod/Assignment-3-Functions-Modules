string_in=input("enter your string")
out=""
for i in range(len(string_in)-1,-1,-1):
    out+=string_in[i]
print(out)