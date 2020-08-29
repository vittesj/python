seconds_time = int(input('Введите секунды:'))
print(f'{seconds_time // 3600 % 24:02d}:{seconds_time // 60 % 60:02d}:{seconds_time % 60:02d}')
