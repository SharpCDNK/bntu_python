str1 = list(input("Enter str1: "))
str2 = list(input("Enter str2: "))

def isAnagram(s1,s2):
    s1.sort()
    s2.sort()

    if s1 == s2:
        print("Is Anagram")
    else:
        print("Not Anagram")


isAnagram(str1,str2)
