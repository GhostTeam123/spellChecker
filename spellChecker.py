
import string
#TO LOAD THE DICTIONARY FILE
def load_word():
    with open('words_alpha.txt') as txt_file:
        all_words = list(txt_file.read().split())
    return all_words
#TO LOAD THE FILE FROM THE USER
def loadFile():
    fileToCheck = input("Enter the file name to check : ")
    with open(fileToCheck) as txt_file:
        wordsAll = list(txt_file.read().split())
    return wordsAll
# THIS FUNCTION IS TO BINARY SEARCH THE FOLDER
def binarySearch(dictionary,word):
    mid = 0
    low = 0
    high = len(dictionary)-1
    while low<= high:
      mid = (low+high)//2
      item = dictionary[mid]
      if word == item:
        return mid
        break
      elif word< item:
        high = mid-1
      else:
        low = mid+1
    return -1

dictionary = load_word()
dictionary.sort()
listWordsFile = loadFile()
listWordsFile.sort()

count = 0 
start = 0
end = len(listWordsFile)
#LOOP THEOUGH THE WORDS AND CHECK THE SPELLING 
while start <= end-1:
   result = binarySearch(dictionary, listWordsFile[start].lower()) 
   if(result==-1):
       print(listWordsFile[start],"  is Incorrect word")
       count+=1
   start += 1
print("count of incorrect words : ", count)


