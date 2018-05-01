wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

"""
in_string = input("Please enter a word: ")
len_in_string = len(in_string)
i = len_in_string
while len_in_string - i < i-1 and in_string[len_in_string - i] == in_string[i-1]:
    i -= 1

if len_in_string - i == i or i*2-1 == len_in_string:
    print("It's a palindrome")
else:
    print("Not a palindrome")
"""
