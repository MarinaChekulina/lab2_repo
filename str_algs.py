def change (str):
    k=len(str)
    #print("Длина вводимой строки: ",k)
    m=k-1
    i = 0
    while i<k:
        a=str[i]
        b=str[m]
        a,b=b,a
        print(a,end='')
        i=i+1
        m=m-1
    print(" ")
    print(" ")
    return None

str1="hello, world"
str2="Chekulina_Marina_Yurevna"

print("Строка hello, world наоборот:")
change(str1)
print("Строка Chekulina_Marina_Yurevna наоборот:")
change (str2)