import random   
import string   

pass_len = 6  

characters = string.ascii_letters + string.digits + string.punctuation 


password = ""  #first we created an empty password
for i in range(pass_len):  # here i is a single character. the loop will run pass_len (12) times, every single time a new random character will be created and that will be added to the empty password. At the end will have a password of 12 characters and the loop will stop. 
    password += random.choice(characters)  # it will create a new single character and add it to the password and continue it for pass_len times.



print("Your password is:", password) 
