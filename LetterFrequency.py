#LetterFrequency.py
#Name:Liam Gillispie
#Date:2/22/2026
#Assignment:Lab 5
#Purpose:Analyze how often a letter appears in a message

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

def countLetters(msg):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = msg.upper()

    freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for char in msg:
        if 'a'<=char.lower()<='z':
            position=ord(char.lower())-ord('a')
            freq[position]+=1

    output = ""
    for index, count in enumerate(freq):
        if count>=0:
            letter=chr(ord('A')+index)
            output+=f"{letter},{count}\n"
    return output        
    writeToFile(output)


def writeToFile(fileText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    freqFile = open("frq.csv", 'w')
    freqFile.write(fileText)

    freqFile.close()


def main():
    msg = input("Enter a message: ")
    result=countLetters(msg)
    print(result)
#loop through each letter
    #Find the position in the alphabet
    #Increase the frequency at that position. If position was 5, then frequencies[5] = frequencies[5] + 1
        

    #Create the output text in the format A,5\n if there were 5 letter A in the message.
    #Remember that the \n is the symbol for a new line.


if __name__ == '__main__':
  main()
