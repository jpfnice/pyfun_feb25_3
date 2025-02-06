"""
Write a pythons scripts that, given a list of words (a list of str), creates a dictionary where the keys do correspond to the word lengths and the values a list of the words with the corresponding length.

For instance, if the list is:
    
words=["He", "does", "confess", "he", "feels", "himself", "distracted", "but", "from", "what", "cause", "he", "will", "by", "no", "means", "speak"]

The dict should be:
    
{ 2:['He', 'he', 'by', 'no'],
 3:['but'],
 4:['does', 'from', 'what', 'will'],
 5:['feels', 'cause', 'means', 'speak'],
 7:['confess', 'himself'],
10:['distracted']}

"""

words=["He", "does", "confess", "he", "feels", "himself", "distracted", "but", "from", "what", "cause", "he", "will", "by", "no", "means", "speak"]

#words=open("words.txt")

mydict=dict() # an empty dict
# or
mydict={} # an empty dict

# Loop through the list words

for e in words:
#   Determine the length of the word currently retreived
    e=e.strip() # to suppress the \n (needed in case we read a file)
    wordsize=len(e)
#   Check if the corresponding key (the length of the word) exist in the dict mydict
#   (you can use the operator "in" to do this test)
    if wordsize in mydict:
#       if it exist append the word to its current values
        mydict[wordsize].append(e)
#       if it does not exist add a new key/value pair to the dict mydict
    else: # elif wordsize not in mydict:
        mydict[wordsize]= [e]
        
# After having processed the whole list, print the dict element by element
print(mydict)
# or
for element in sorted(mydict.keys()):
    print(element, "->", mydict[element])



