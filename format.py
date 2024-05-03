name1 = 'Мастера кода'
name2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 10247.2
team2_time = 18015.2
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
chalange_result = result
# %s
print('В команде %s участников: %s ! ' % (name1, team1_num))
print('Итого сегодня в командах участников: %s и %s человек !' % (team1_num, team2_num))
# format()
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {} с !'.format(team2_time))
# f'{}'
print(f'Команды решили {score_1} и {score_2} задачи.')
print(f'Результат битвы: {chalange_result}')
print(f'Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
