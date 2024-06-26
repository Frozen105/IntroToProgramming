import sys

from math import sqrt

    
def keygen(characters):
    '''
    This is your key generator. It takes a list of characters, in any random order, and 
    converts them into a key using the same logic as the Polybius Square (i.e. one letter gets two numbers
    according to the placement on the table (row and column)).
    
    Although it is based off the Polybius square, it is enhanced: it allows more than 25 characters,
    it allows any combination of characters, and it allows you to switch characters so that you get your own
    secret unique key. For instance, in the Polybius square the usual order is "A,B,C,D(...)". Here you can, if you want
    use something like "E,F,A,B,(...)"
    
    Feel free to try it out by either using the 'mykey1.txt', 'mykey2.txt' files
    provided, or by modifying the 'mykey1.txt' in any way you like.
    '''


    sub_tup=()
    tup=()
    if int(sqrt(len(characters)))**2 == (int(len(characters))):    
        tup_number = int(sqrt(len(characters)))
    else:
        tup_number = int(sqrt(len(characters)))+1
    n=len(characters)/tup_number
    for i in range(len(characters)):
        sub_tup = sub_tup + (characters[i],)
        if len(sub_tup)>=n:
            tup= tup + (sub_tup,)
            sub_tup=()
    if sub_tup != ():
        tup= tup + (sub_tup,)
    return tup

def getcode_part1(character, used_key):
    '''
    Necessary functionality for the getcode_final function
    '''
    for row in range(len(used_key)):
            for col in range(len(used_key[row])):
                if character == used_key[row][col]:
                    return str(row)+str(col)

def getcode_final(character, used_key):  
    ''' 
    This function takes the character, the key used to encrypt,
    and transforms the character into a pair of numbers (corresponding to row
    and column on the defined table)
    '''
    
    result = getcode_part1(character, used_key)             
    if isinstance(result,str):
        return result
    else:
        return 'XX'


def encrypt(message, used_key):
    '''
    This function generalizes the encryption of one character, and encrypts a whole message.
    It is essentially a use of the getcode_final functionality to encrypt a chain of characters.
    '''
    
    encrypted_message=''
    for i in range(len(message)):
        character=message[i]
        encrypted_message = encrypted_message + getcode_final(character, used_key) 
    return encrypted_message

def generate_encrypted_message():
    ''' This is the final encrypt function with all functionalities.
    
    It takes user inputted text and returns numbers.
    We use a key, generated by the keygen function and our provided table of characters, to encrypt.
    When there are characters not contained in the key, it replaces them with '?ERROR?'
    '''
   
    try:
        filedirect=input("\n|\n|\n|Enter name of the .txt file intended for encryption: ")+".txt"
        with open(file = filedirect, mode="r") as f: 
            filedata=f.read()
            message=filedata
    except:
        print("""\n|\n|\nAN ERROR HAS OCCURRED. Please make sure you entered the correct file name,
and that the file is in the same directory you are running this script from.\n|\n|""")
        input("Press any key to exit.")
        sys.exit(-1)
         
    for letter in "^~<>»«_#';:!":
        message = message.replace(letter, "?ERROR?")
    
    try:
        key_file_name=input("\n|\n Enter name of the key .txt file: ")+".txt"
        with open(file = key_file_name, mode="r") as f:
            key1=f.read()
    except:
        print("""\n|\n|\nAN ERROR HAS OCCURRED. Please make sure you entered the correct file name,
and that the key file is in the same directory you are running this script from.\n|\n|""")
        input("Press any key to exit.")
        sys.exit(-1)
         
    key1=list(key1)
    key1=keygen(key1)
    encrypt(message, key1)
    with open("encrypted_message.txt",mode="w") as f_out:
        f_out.write(encrypt(message,key1))
    print("\n|\n|\nEncrypted text file generated! Please check the directory.")
    
generate_encrypted_message()

input("Press any key to exit.")
sys.exit(-1)
