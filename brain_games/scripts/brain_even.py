#пользователю показывается случайное число. И ему нужно ответить yes, если число чётное, 
#или no — если нечётное:
#Welcome to the Brain Games!
#May I have your name? Bill
#Hello, Bill!
#Answer "yes" if the number is even, otherwise answer "no".
#Question: 15
#Your answer: yes
#В случае, если пользователь даст неверный ответ, необходимо завершить игру и вывести сообщение:
#'yes' is wrong answer ;(. Correct answer was 'no'.
#Let's try again, Bill!
#В случае, если пользователь ввел верный ответ, нужно отобразить:
#Correct!
#и приступить к следующему числу.
#Пользователь должен дать правильный ответ на три вопроса подряд. После успешной игры нужно вывести:
#Congratulations, Bill!
#Вывод должен получиться следующий:
#brain-even
#Welcome to the Brain Games!
#May I have your name? Sam
#Hello, Sam!
#Answer "yes" if the number is even, otherwise answer "no".
#Question: 15
#Your answer: no
#Correct!
#Question: 6
#Your answer: yes
#Correct!
#Question: 7
#Your answer: no
#Correct!
#Congratulations, Sam!
#Любой некорректный ввод считается ошибкой (например, n) и равносилен неправильному ответу.

#import block
import prompt
import random
from random import randint
import math
#from brain_games.cli import welcome_user


#создание функции проверка на четность
def is_eval(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'

print("Welcome to the Brain Games!")
name = prompt.string('May I have your name? ')
print('Hello, ' + name + '!')

def solution():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    
    while count < 3:
        num = randint(1, 100)
        print ('Question: ' + str(num))
        answer = prompt.string('Your answer: ')
        if answer == is_eval(num):
            print('Correct')
            count+=1
        else:
            if answer == 'no':
                print(answer + " is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, " + name)
                return 
            elif answer == 'yes':
                print(answer + " is wrong answer ;(. Correct answer was 'no'.\nLet's try again, " + name)
                return
            else: 
                print(answer + "is wrong" + name)
                return
            
    print('Congratulations, ' + name + '!')


solution()

