# mounts = int(input('Введите номер месяца: '))
# season = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
# for mount, season in season.items():
#     print(f'{mount} - {season}')
# seasons = {'winter': [1, 2, 3], 'spring': [4, 5, 6], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
# for k, v in seasons.items():
#     print(mounts)
a = ['first', 1, 2, 3, 'second', 10, 20, 'third', 15, 56, 70, 'fourth', -50]
my_dict = {}
current_str = None

for e in a:
    if(type(e) == str):
        my_dict[e] = []
        current_str = e
    else:
        my_dict[current_str].append(e)