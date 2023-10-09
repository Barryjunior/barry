import time
start_time=time.time()
import random
import string

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}") 
print(f"key: {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
Cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    Cipher_text += key[index]
    
    print(f"original message: {plain_text}")
    print(f"encrypted message: {Cipher_text}") 

#DECRYPT
Cipher_text = input("Enter a message to encrypt: ")
Plain_text = ""

for letter in Cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
    
    print(f"encrypted message: {Cipher_text}") 
    print(f"original message: {plain_text}")
    
    end_time=time.time()
    execution_time=end_time-start_time
    print("Execution time:", execution_time,"seconds")
    
    import psutil
    #Get the memory usage in bytes
    memory_usage=psutil.Process().memory_info().rss
    
    #Covert to megaytes
    memory_usage_mb=memory_usage/(1024*1024)
    
    print("Memory usage:", memory_usage_mb,"MB")
    
    import psutil
    #Get the CPU usage as a percetage
    cpu_usage=psutil.cpu_percent()
    
    print("CPU usage:", cpu_usage,"%")