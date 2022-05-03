Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = float(input("Введите коэффициент a "))
b = float(input("Введите коэффициент b "))
if (a == 0 and b == 0):
    print("Бесконечное количество решений.")
if (a == 0 and b != 0):
    print("Решений нет.")
if (a != 0):
    print(b/a))
    
SyntaxError: multiple statements found while compiling a single statement
