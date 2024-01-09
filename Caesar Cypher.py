#Marcin Zarkowski
#24225410
#This program shifts right letters using cypher disk.

mess=input("Enter a message to encode")
codedWord=""
for i in mess:
    offset = ord(i) - ord('a') + 13
    wrap= offset % 26
    newChar=chr(ord('a')+wrap)
    print(wrap,chr(ord('a') + wrap))
    codedWord= codedWord + newChar

print("The coded word (with wrap) is",codedWord)
