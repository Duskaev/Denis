def is_palindrome(s):
    palindrome=str(s).lower(s).replace(' ','').replace(',','') #Преобразуем все в строку, приводим все к нижнему регистру, удалаем пробелы и запятые
    palindrome=palindrome1[::-1] #вводим еще одну переменную для сравнения
    if palindrome==palindrome1: #сравниваем наши переменные
        retrum True
    else:
        retrum False