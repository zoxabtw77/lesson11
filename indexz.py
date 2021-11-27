# while True:
#     try:
#         numOfTerms = int(input('Введите число слагаемых: '))
#         if numOfTerms < 2: raise ValueError('Число слагаемых должно быть равно или больше 2-м')
#         else: break
#     except ValueError as ve:
#         print(ve)

# while True:
#     try: 
#         acc = 0
#         for i in range(1, numOfTerms + 1):
#             num = int(input(f'Enter {i} term: '))
#             acc += num
            
#         if acc < 100: raise ValueError('Сумма меньше 100')
#         else: 
#             print(acc)
#             break
#     except ValueError as ve:
#         print(f'Сумма должна быть больше 100. Попробуйте ввести {numOfTerms} слагаемых заново')

# while True:
#     num = int(input('Enter prime number: '))
# try:
#      for factor in range(2, num):
#         if num % factor == 0: raise ValueError('your number is not prime')
#      else: break
# except ValueError as ve:
#     print(ve) 

# while True:
#     password = input('Enter password: ')
#     try:
#         if len(password) < 8: raise ValueError('Password should contain at least 8 characters')
#         else: break
#     except ValueError as ve:
#         print(ve)

# while True:
#     try:
#         numOfTerms = int(input('Введите число слагаемых: '))
#         if numOfTerms < 2: raise ValueError('Число слагаемых должно быть равно или больше 2-м')
#         else: break
#     except ValueError as ve:
#         print(ve)

# while True:
#     try: 
#         acc = 0
#         for i in range(1, numOfTerms + 1):
#             num = int(input(f'Enter {i} term: '))
#             acc += num
            
#         if acc < 100: raise ValueError('Сумма меньше 100')
#         else: 
#             print(acc)
#             break
#     except ValueError as ve:
#         print(f'Сумма должна быть больше 100. Попробуйте ввести {numOfTerms} слагаемых заново')


