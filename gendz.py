
# sample_logs = [
#     "192.168.1.1 - [23/Mar/2025:10:15:15] \"GET /home HTTP/1.1\" 200 1240",
#     "192.168.1.2 - [23/Mar/2025:10:16:05] \"GET /nonexistent HTTP/1.1\" 404 503",
#     "192.168.1.3 - [23/Mar/2025:10:16:15] \"GET /about HTTP/1.1\" 200 850",
#     "192.168.1.1 - [23/Mar/2025:10:17:05] \"GET /contact HTTP/1.1\" 200 945",
#     "192.168.1.4 - [23/Mar/2025:10:18:22] \"GET /old-page HTTP/1.1\" 404 512",
#     "192.168.1.2 - [23/Mar/2025:10:19:17] \"GET /another-missing HTTP/1.1\" 404 503",
#     "192.168.1.5 - [23/Mar/2025:10:20:01] \"GET /products HTTP/1.1\" 200 1655",
#     "192.168.1.4 - [23/Mar/2025:10:21:14] \"GET /missing-again HTTP/1.1\" 404 500"
# ]
# logs=list(filter(lambda logs:logs.split()[-2]=='404',sample_logs))
# unique_ips=set(logs.split()[0] for logs in logs)
# for ip in unique_ips:
#     print(ip)

import time

def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs)  
        end_time = time.time() 
        print( f"{func.__name__} : {end_time - start_time} seconds")
        return result
    return wrapper

@decorator
def sumOfNums():
    time.sleep(0) 
    num1=int(input())
    num2=int(input())
    print("Sum:",num1+num2)

sumOfNums()
