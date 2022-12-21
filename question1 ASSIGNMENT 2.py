a="Python is a case sensitive language"

#FINDING LENGTH OF THE STRING

print("length of the string is", len(a))

#REVERSING THE ORDER OF THE STRING

print(a[::-1])

#STORING A NEW STRING USING SLICE FUNCTION

b=slice(a[11:27:1])
print(b)

#REPLACING 'A CASE SENSITIVE' with 'OBJECT ORIENTED'

x=a.replace('a case sensitive','object oriented')
print(x)

#FINDING INDEX OF SUBSTRING "a" IN THE GIVEN INPUT STRING

print(a.index("a"))

#removing white spaces from the string

print(a.replace(" ",""))
