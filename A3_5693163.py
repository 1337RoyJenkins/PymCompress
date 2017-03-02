########################################################################################################
# What is this program anyways?
########################################################################################################

'''
Pym CODEC is an RLE CODEC designed with the purpose of compressing text files. In case the person grading
this doesn't happen to be as big of a comic geek as this CODEC's developer (aka me), The name is a nod to
Hank Pym, alter-ego of Marvel Comics character Ant Man, famed for his ability to compress himself to
extremely small sizes through the use of his trademark "Pym Particles".
'''

########################################################################################################
# Function Declarations and initial declarations
########################################################################################################

again = True
options = ["encode a file", "decode a file", "exit"]

def getInput():
    repeat = True
    while repeat == True:
        for i in range (0, 3):
            print ("Enter {} to {}".format(i+1, options[i]))
        seleciton = input("Enter your choice:")
        if selction == 1:
            #encode
            repeat = False
            return True
        elif selection == 2:
            #decode
            repeat = False
            return True
        elif selection == 3:
            print ("You have selected 'Exit'. " + "\n" "Thanks for using Pym. Good-bye")
            repeat = False
            return False
        else:
            print ("Whoops! I couldn't understand your input, please try again")

def enode(source):
    if source.endswith('.txt'):
        #encode
    else:
        print ("Unsupported file format for compression. Pym supports compression of .txt files only")


def decode(source):
    if source.endswith('.pym'):
        #decode
    else:
        print ("Unsupported file format for decompression. Pym supports decompression of .pym files only")


########################################################################################################
# Where the magic happens
########################################################################################################


# Choose Wisely
while again = True:
    print ("Welcome to Pym. Please select from one of the following options:")
