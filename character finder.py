text= input("Enter a paragraph: ")

characters= len(text)

spaces = text.count(" ")  

words = len(text.split())

vowels = "aeiouAEIOU"
vowel_count =0

for char in text:
    if char in vowels:
        vowel_count += 1


print("\n***********character finder*********")
print("Total Characters:",characters)
print("Total Spaces:", spaces)
print(" Total Words:", words)
print("Total Vowels:", vowel_count)

if len(text) == 0:
    print("\n first character(Indexing) :",text[0])
    print("Last character(Indexing) :",text[-1])


print("\nfirst 10 characters(slicing):", text[0:10])
print("Last 10 characters(slicing):", text[-10:])