from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

input1=input("Enter your text :")
print("1: tokenize words \n2: tokenize sentence \n3: original text")

choice=input("choose your number : ")
if choice=="1":
    print(word_tokenize(input1))
elif choice == "2":
    print(sent_tokenize(input1))
elif choice =="3":
    print(input1)
else:
    print("wrong choice ")
#“ NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project.”    