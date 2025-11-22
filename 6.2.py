###
# Counts vowels in the text
#
text = "aaaabbbasdwcaaaa."
i = 0 
vowels = "aeiouAEIOU"
vowel_count = 0

# Count vowels in the text
while len(text) > i :
    if  text[i] in vowels :
        vowel_count +=1
    i +=1

    


##for char in text:
 #   if char in vowels:
   #     vowel_count += 1

print(f"The number of vowels in the text is: {vowel_count}")