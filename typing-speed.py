import time,random
from termcolor import cprint

min = 1/60

word_list = [
    'Where are you, the gatekeeper shouted!',
    'the quick brown fox jumped over the lazy dogs',
    'for the Lord will come like a thief at night when no one expects',
    'this is where we separate the good from the bad.',
    'how do i tell him the Truth.'
]





def main():
    word = random.choice(word_list)

    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    cprint(word, 'green')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

    confirmation_flag = input('Hit "Enter" to start typing! ') or True

    if confirmation_flag:
        start = time.time()
        user_input = input('|> ')
        end = time.time()
        word_length = len(word)
        if len(user_input) < word_length:
            il = len(user_input)
            user_input += (word_length - il) * ';'
        # print(user_input)
        user_input = user_input[:word_length]
        tot_time = end - start
        tot_time = tot_time/60

        residual = 0
        for index,char in enumerate(word):
            if user_input[index] != char:
                residual+=1
        
        accuracy = (word_length - residual ) / word_length 
        speed = (word_length//5) / tot_time
        speed = accuracy * speed
        speed = round(speed)
        print(f'YOU HAD A SPEED OF {speed} WPM AND AND ACCURACY OF {round(accuracy * 100)}%')


if __name__ == '__main__':
    while True:
        main()
        print('\n \n')