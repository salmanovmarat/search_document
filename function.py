import string
def search_document(word):
    indexes =[]
    with open("ap_docs.txt", "r") as f:
        read = f.read().split("<NEW DOCUMENT>")
        word = word.split(" ")
        for index,value in enumerate(read):
            allexist = True
            for i in string.punctuation:
                line = value.replace(i," ")
            for i in word:
                if i.lower() not in line.lower():
                    allexist = False
                    break
            if(allexist):
                indexes.append(index)
    print(set(indexes))

def read_document(number):
    with open("ap_docs.txt", "r") as f:
        read = f.read().split("<NEW DOCUMENT>")
        for index,value in enumerate(read):
            if index == number:
                print(value)


