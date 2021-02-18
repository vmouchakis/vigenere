#This is a program that given a ciphertext and a key, can find the message that is
#encrypted with Vigenere algorithm (only A-Z and a-z).

def return_letter_value(c):
    #given a character, this function returns a value to ci and ki (0-25 for A-Z, 26-51 for a-z)
    #if character is SPACE or ENTER it returns -1, beacause it's easy to catch and avoid any mistake
    #(we do not want SPACE or ENTER to change after decryption)

    if ord(c) >= 65 and ord(c) <= 90:
        return ord(c) - 39
    elif ord(c) >= 97 and ord(c) <= 122:
        return ord(c) - 97
    else:
        return -1

#The name of the files must be given in the following for: file.txt .
#NOT file or "file" or "file.txt".
#It must be as it is in the directory.
cipher_text = input("Give cipher's file name: ")
key_text = input("Give key's file name: ")
message_text = input("Give the name you want your decrypted file have: ")

cipher = open(cipher_text, "r")
key = open(key_text, "r")
message = open(message_text, "w")

cipher_contents = cipher.read()
key_contents = key.read()
message_contents = ""

i = 0
j = 0
ci = 0  #ciphertext's letter value 0-25 for A-Z, 26-51 for a-z 
ki = 0  #key's letter value 0-25 for A-Z, 26-51 for a-z
dec = 0 #letter's value after decryption

print("\n\nYour ciphertext is being decrypted. . .\n\n")

while i < (len(cipher_contents)):
    #We start by decrypting every letter from the ciphertext with a letter from the key.
    #If the key ends, we start from the first letter of the key again

        if return_letter_value(cipher_contents[i]) != -1:
            ci = return_letter_value(cipher_contents[i])
            ki = return_letter_value(key_contents[j])

            dec = (ci - ki) % 52

            if dec >= 0 and dec <= 25:
                message_contents = message_contents + chr(dec + 65)
            elif dec >= 26 and dec <= 51:
                message_contents = message_contents + chr(dec + 71)
        else:
            j = j - 1
            message_contents = message_contents + cipher_contents[i]

        #print(message_contents)
        if j == len(key_contents) - 1:
            j = -1
    

        i += 1
        j += 1

print("Your cipher has been decrypted.\nHere is the message:")
print("\n" + message_contents)

message.write(message_contents)    
        
cipher.close()
key.close()
message.close()



