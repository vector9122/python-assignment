import re
import os.path


var = input("Please enter the file path : ")
file_name = os.path.split(var)[1].rsplit('.',1)[0]   # extracting file name from the input file
nonLettersPattern = re.compile("[^a-zA-Z]")  # Regex code to remove anthing other than alphabets from the strings

# Defining a Function which will be used to return a list of names from the input file
def read_words(var):
    f = open(var, "r")
    original_words = f.readlines()
    new_words = []
    for i in original_words:
        line = i.strip().replace('\n', '')
        new_words.append(line)

    return new_words

l = read_words(var)



# Function to be used for removing apostrophes from the string

def removeApostrophes(string):
    return string.replace("'","")     

# Function to remove spaces and make a list of individual words from names

def cleanString(string,cleanPattern):
    
    string = removeApostrophes(string)
    
    string = cleanPattern.sub(" ",string)
    string = string.upper()
    words = [word.strip() for word in string.split(" ")]
    
    return words


wordScore = {"Q":1,
            "Z":1,
            "J":3,
            "X":3,
            "K":6,
            "F":7,
            "H":7,
            "V":7,
            "W":7,
            "Y":7,
            "B":8,
            "C":8,
            "M":8,
            "P":8,
            "D":9,
            "G":9,
            "L":15,
            "N":15,
            "R":15,
            "S":15,
            "T":15,
            "O":20,
            "U":20,
            "A":25,
            "I":25,
            "E":35}

# Function to get list of score of each letter in a name
def nameScores(words, wordScore):
    scoreIndex=[]
    for word in words:
        
        for i,letter in enumerate(word,0):
            
            if i==0:
                scoreIndex.append(0)
            elif i==len(word)-1:
                
                if letter == "E":
                    scoreIndex.append(20)
                else:
                    scoreIndex.append(5)
                    
            else:
                i_scr = min(i,3)
                
                scoreIndex.append(wordScore.get(letter)+i_scr)
                
    return scoreIndex

# Function to get combination of valid abbreviation for a name and their scores in the form of a dictionary
def createCombs(compactString,scores):
    
    createdCombs = {}
    
    start = compactString[0]
    
    for i,secondLetter in enumerate(compactString[1:],1):
        
        for j,thirdLetter in enumerate(compactString[i+1:],i+1):

            comb = start+secondLetter+thirdLetter
            combScore = 0+scores[i]+scores[j]
            if createdCombs.get(comb):
                
                if createdCombs.get(comb) > combScore:
                    createdCombs[comb] = combScore
                    
            else:
                createdCombs[comb] = combScore
                
    return createdCombs

# Function to take a name as list of words and the scores corresponding to 
# each letter and return all combinations where abbreviations are sorted in ascending order of score
def combGenerator(words,wordScore):
    scores = nameScores(words, wordScore)
    compactString = "".join(words)
    allCombs = dict(sorted(createCombs(compactString,scores).items(),key=lambda x:x[1]))
    return allCombs

# Function to take list of names, word score corresponding to each letter and a regex compiled patttern
# It returns final abbreviation correponding to each name as per specification.
def main(listNames,wordScore, cleanPattern):
    
    abbreviations = []
    finalOutput=[]
    
    for name in listNames:

        words = cleanString(name, cleanPattern)
        temporaryAbbr = combGenerator(words,wordScore)
        combKeys = list(temporaryAbbr.keys())

        for i,element in enumerate(abbreviations):
            elementAbbrs = list(element[-1].keys())
            for abbr in combKeys :
                if abbr in elementAbbrs:
                    temporaryAbbr.pop(abbr,None)
                    element[-1].pop(abbr,None)

                    abbreviations[i] = [element[0],element[-1]]

        abbreviations.append([name,temporaryAbbr])

        
    for element in abbreviations:
        if len(element[-1])==0:
            finalOutput.append(element[0])
            finalOutput.append(" ")
            
        else:
            finalOutput.append(element[0])
            finalOutput.append(list(element[-1].keys())[0])
    return finalOutput



if __name__ == '__main__':
    output = main(l,wordScore,cleanPattern = nonLettersPattern)

    with open(r'pant'+'_'+ file_name +'_'+'abbrevs.txt', 'w') as writer:
        for item in output:
        # write each item on a new line
            writer.write("%s\n" % item)

