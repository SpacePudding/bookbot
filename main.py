def main():
    filePath = 'books/frankenstein.txt' 
    with open(filePath) as file:

        print(f"Begin report of {filePath}")

        fileContents = file.read()

        print(f"Number of words in the book: {getNumberOfWords(fileContents)}")

        charDict = countOccurenceOfLetters(fileContents)

        sortedCharDict = {k: v for k, v in sorted(charDict.items(), reverse=True, key=lambda item: item[1])}

        for char in sortedCharDict:
            print(f"The \'{char}\' character was found {sortedCharDict[char]} times")



        

def sort_on(dict):
    return dict["num"]

def countOccurenceOfLetters(fileContents):
    letterDictionary = {}

    for character in fileContents.lower():

        isAlpha = character.isalpha()

        if character not in letterDictionary and isAlpha:
            letterDictionary[character] = 1
        elif isAlpha:
            letterDictionary[character] += 1

    return letterDictionary


def getNumberOfWords(fileContents):
    return len(fileContents.split()) 

if __name__ == "__main__":
    main()