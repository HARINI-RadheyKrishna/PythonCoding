#Time Complexity = O(n) where n = number of words in the sentence
#Space Complexity = O(n) where n = number of words in the sentence

def wordLen (word):
    for i in range(len(word)):
        New = list(word.split(" "))
        
    #print("Hi",New)
    n = len(New)
    return n
        

print("Hello world")
sentence = str(input())
num = wordLen(sentence)
print(num)