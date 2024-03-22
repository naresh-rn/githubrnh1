# Object oriented program
# string pallindrome or not

def stringPallindrome(string):
    return string == string[::-1]

string = input("Enter a String to find Given string is Pallindrome or Not : ")
if stringPallindrome(string) == True:
    print(string ,"is a Pallindrome String")
else:
    print(string , "is Not a pallindrome string")

