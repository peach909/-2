Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='' 
for i in range(10,100): 
s += str(i) 
print(len(s)) 

while 1: 
k = int(input('k(1..180) ')) 
pc = (k+1)//2 
print(pc) 
print(s[(pc-1)*2:pc*2])