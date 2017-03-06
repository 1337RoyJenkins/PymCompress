###################################################################################################################
# What is this program anyways?
###################################################################################################################

'''
Pym is an RLE CODEC designed with the purpose of compressing text files. In case the person grading this
doesn't happen to be as big of a comic geek as this CODEC's developer (aka me), The name is a nod to
Hank Pym, alter-ego of Marvel Comics character Ant Man, famed for his ability to compress himself to
extremely small sizes through the use of his trademark "Pym Particles".

Written by Lukas Horak
Student number 5693163

This program has been posted on my GitHub! The link is included below:

'''
###################################################################################################################
# Function Declarations and initial declarations
###################################################################################################################
import os

again = True
options = ["encode a file", "decode a file", "exit"]

###################################################################################################################
'''Function: listCWD(which)'''
###################################################################################################################
'''
Description:
    Lists files in the current working directory, so the user may easier choose one
Parameters:
    which - takes 'encode' or 'decode' as an argument, depending on WHICH of these is being asked for
            from the user
Output:
    ask - Returns the name of the file that the user wishes to encode or decode
'''
###################################################################################################################
def listCWD(which):
    print ("These are the files in the current working directory:" + "\n")
    files = [f for f in os.listdir('.'  ) if os.path.isfile(f)]
    for f in files:
        print (f)
    ask = str(input("Please select one of the listed .txt files to {}:".format(which)))
    return ask

###################################################################################################################
'''Function: main()'''
###################################################################################################################
'''
Description:
    The main function of the program. Written as a function instead of simply in the body so that it can return a
    boolean value and be easily loop-able based on the value it returns.
Parameters:
    None
Output:
    Returns True or False, based on whether or not the user elects to continue, or terminate the program. True if
    they would like to continue, false if they would like to break the loop and terminate.
'''
###################################################################################################################
def main():
    repeat = True   # For listing the options
    check = False   # For repeating the whole thing later
    while repeat == True:
        print ("Please select one of the following options:\n")
        for i in range (0, 3):
            print ("Enter {} to {}".format(i+1, options[i]))
        print ('\n')
        selection = input("Enter your choice:")
        if int(selection) == 1:
            #encode the selected file
            validChoice = False
            while validChoice == False:
                # Set the value of selectFile to the user's choice from listCWD
                selectFile = listCWD('encode')
                if isSupported(selectFile):
                    # Tags the output file with a (compressed) tag for validation should it be decompressed later
                    out = "(compressed)" + selectFile
                    encode(selectFile, out)
                    validChoice = True
                else:
                    print ("Invalid choice. Try again\n")
            repeat = False
        elif int(selection) == 2:
            #decode the selected file
            validChoice = False
            while validChoice == False:
                # Set the value of selectFile to the user's choice from listCWD
                selectFile = listCWD('decode')
                if isSupported(selectFile):
                    # Verifies if the file is valid for compression by checking for the approprate tag
                    if selectFile[0:12] == "(compressed)":
                        # Removes the old (compressed) tag, and tags the output file with (new) to avoid overwriting an existing file
                        out = "(new)" + selectFile[12:]
                        decode(selectFile, out)
                        validChoice = True
                    else:
                        print ("Invalid file for decompression.\n(Hint: Pym-compressed files begin with '(compressed)')")
                else:
                    print ("Invalid choice. Try again\n")
            repeat = False
        elif int(selection) == 3:
            print ("You have selected 'Exit'. " + "\n" "Thanks for using Pym, good-bye!")
            return False
            break
        else:
            print ("Whoops! I couldn't understand your input, please try again")
    print ("\nWould you like to select another file?\n")
    # Use of 'while' loop to remain in the program until the user decides to quit
    while check == False:
        goAgain = input("Enter y to go again, or n to terminate:").lower()
        if goAgain == 'y':
            check = True
            return check
        elif goAgain == 'n':
            check = True
            return False
        else:
            print ("Invalid input, try again.")


###################################################################################################################
'''Function: isSupported(inFile)'''
###################################################################################################################
'''
Description:
    Verifies if a desired input file not only exists, but is in the proper file format. This is done with a combo of
    an if statement to verify file format, and a try/except attempting to open the file if it is the correct format.
    Pym currently supports the use of .txt files only.
Parameters:
    inFile - Desired input file for verification.
Output:
    Returns True if the file exists and is supoorted, or False otherwise.
'''
###################################################################################################################
def isSupported(inFile):
    if inFile.endswith('.txt'):
        try:
            open(inFile, 'r')
        except IOError:
            print ("Input File Not Found")
            return False
        return True
    else:
        print ("Unsupported file format. Pym supports .txt files only")
        return False

###################################################################################################################
'''Function: encode(inputFile, outputFile)'''
###################################################################################################################
'''
Description:
    Opens the desired file, encodes its contents into a list, with each line being one item. Linebreaks are marked
    with a '$' character. The function then iterates over this list, writing each element to the desired output file.
    encode() also keeps counts the length of both the output and input files (oldLength and newLength, respectively),
    then uses these to calculate the compression ratio, printing this out with the confirmation of completion.
Parameters:
    inputFile  - Filename of the desired file for encoding
    outputFile - Filename of the desired file for output
Output:
    None
'''
###################################################################################################################

def encode(inputFile, outputFile):
    with open(inputFile, "r") as inFile:
        print("Encoding in progress...")
        # Initialize Variables
        compressed = []
        count = 0
        oldLength = 0
        newLength = 0
        current = ''
        for line in inFile:
            # Visually represent progress with '...' for each iteration over a line
            print("...")
            for c in range (0, len(line)-1):
                current = line[c]
                oldLength += 1
                if c == 0:
                    current = line[c]
                    # Initialize count at 1
                    count = 1
                if line[c] == line[c+1]:
                    count += 1
                else:
                    # Record the count and the current character being counted
                    compressed.append(str(count) + current)
                    # Reset count to 1 for next character
                    count = 1
            # Records'$' character as a marker so linebreaks can be preserved for decompression
            compressed.append('$')
    for ix in compressed:
        newLength += len(ix)
        # Calculate Compression Ratio
    ratio = oldLength / newLength
    print("Encoding Complete!" + "\n" + "Compression ratio: {0:.2f}".format(ratio))
    outFile = open(outputFile, 'w')
    for ic in compressed:
        outFile.write(ic)
    return None

###################################################################################################################
'''Function: decode(inputFile, outputFile)'''
###################################################################################################################
'''
Description:
    Opens the desired file, decodes its contents into a list, with each count-character pairing (eg 4A) as an item.
    The function then iterates over this list, writing each element to the desired output file, and linebreaks for
    each '$' character listed.
Parameters:
    inputFile  - Filename of the desired file for decoding
    outputFile - Filename of the desired file for output
Output:
    None
'''
###################################################################################################################

def decode(inputFile, outputFile):
    with open(inputFile, "r") as inFile:
        print ("Decoding in progress...")
        # Initialize Variables
        decompressed = []
        num = ''
        for line in inFile:
            print("...")
            for c in range (0, len(line)):
                # First, check if character calls for a linebreak, inserting if necessary
                if line[c] == '$':
                    print ("...")
                    decompressed.append('\n')
                elif line[c].isnumeric():
                    # Create string called 'num' noting number of characters to write
                    num = num + line[c]
                elif (line[c].isalpha() or line[c] == ' ') and not num == '':
                        # Converts 'num' to an integer so it can be used to write the desired character 'num' times
                        ch = line[c]

                        string = ch * int(num)
                        decompressed.append(string)
                        # Reset 'num' to blank so that this process can be repeated for the next character
                        num = ''
                else:
                    print ("Wrong Encoded Format. Terminating Program")
                    return None
    print("Decoding Complete!")
    outFile = open(outputFile, 'w')
    for ic in decompressed:
        outFile.write(ic)
    return None



########################################################################################################
# Where the magic happens
########################################################################################################


# Choose Wisely
print ("Welcome to Pym!\n\n:")
while again:
    again = main()
print ("\nThank you for using the Pym Compression CODEC. Good-bye!")
