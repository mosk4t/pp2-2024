def custom_sleep(n, delay): 
    start_time = 0 
    while start_time <=  delay: 
        start_time += 0.00004  
    return n**(1/2)
print("Input: ")
n = int(input())
delay = int(input())
print(f"Square root of {n} after {delay} is {custom_sleep(n, delay)}")