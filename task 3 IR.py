from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import PorterStemmer,SnowballStemmer
snowball1=SnowballStemmer(language='english')
porter1 = PorterStemmer()
input1=input("Enter your text :")
print("1: tokenize words \n2: tokenize sentence \n3: original text \n[for stemming] : \n4: porter Stemmer \n5: snowball Stemmer")

choice=input("choose your number : ")
if choice=="1":
    print(word_tokenize(input1))
elif choice == "2":
    print(sent_tokenize(input1))
elif choice =="3":
    print(input1)
elif choice =="4":
    print(porter1.stem(input1))
elif choice =="5":
    print(snowball1.stem(input1))
else:
    print("wrong choice ")




