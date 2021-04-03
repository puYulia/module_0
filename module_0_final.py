import numpy as np

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v4(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    score_min = 1
    score_max = 100
    
    count = 1
    predict = int(round(score_max/2))

    while number != predict:
        count += 1
        predict, score_min, score_max = iterstep(number, predict, score_min, score_max)

    return(count) # выход из цикла, если угадали


def iterstep(number, predict, score_min, score_max):
    if number > predict: 
        # Если искомое значение больше  
        
        # Меняем минимальный предел поиска на следующей итерации
        score_min = predict

        # Проверяем если предел поиска больше 2 (можно взять среднее значение диапазона), либо двигаемся пошагово
        if (score_max - score_min) > 2:
            predict_next = int(round(score_min + (score_max - score_min)/2))
        else:
            predict_next = predict + 1

    
    elif number < predict: 
        # Если искомое значение меньше

        # Меняем максимальный предел поиска на следующей итерации
        score_max = predict

        # Проверяем если предел поиска больше 2 (можно взять среднее значение диапазона), либо двигаемся пошагово
        if (score_max - score_min) > 2:
            predict_next = int(round(score_min + (score_max - score_min)/2))
        else:
            predict_next = predict - 1

    else:
        predict_next = number

    # Возвращаем значения для следующего шага поиска
    return predict_next, score_min, score_max


score_game(game_core_v4)

