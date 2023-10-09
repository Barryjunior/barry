import time
start_time=time.time()
from cryptography.fernet 
import Fernet


message = 'hello world'

Key=Fernet.generate_key()
print(Key)


fernet_obj = Fernet(Key)


encrypted_message=fernet_obj.encrypt(message.encode())
print(encrypted_message)

decrypted_message =fernet_obj.decrypt(encrypted_message).decode()
print(decrypted_message)
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
          







