print("leave the input blank for result")

def average(li):
    x = sum(li) / len(li)
    print(x)

list1 = []
try: 
      while True: 
        list1.append(int(input("Enter the numbers:"))) 
          
except: 
    print(list1) 

try:
    while True:
        average(list1)
        break
except:
    print("you should add some numbers, then other charecters to get a average of those numbers")
