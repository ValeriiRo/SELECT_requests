import sqlalchemy
login = input('Внесение данных по музыкальному магазину в базу данных. \n Введите логин: ')
password = input('Введите пароль: ')
database = input('Введите название базы: ')
address = 'postgresql://' + login + ':' + password + '@localhost:5432/' + database
engine = sqlalchemy.create_engine(address)
connection = engine.connect()

sel = connection.execute("""SELECT title_albums, year_of_release FROM albums
WHERE year_of_release = 2018;
""")
print('Название и год выхода альбомов, вышедших в 2018 году:\n', *sel, '\n')

MAX_duration = connection.execute("""SELECT MAX(duration) FROM tracks;
""").fetchone()
sel = connection.execute(f"""SELECT track_name, duration FROM tracks
WHERE duration = {MAX_duration[0]};
""").fetchone()
print('Название и продолжительность самого длительного трека:\n', *sel, '\n')

sel = connection.execute("""SELECT track_name, duration FROM tracks
WHERE duration >= 210;
""")
print('Название треков, продолжительность которых не менее 3,5 минуты:\n', *sel, '\n')

sel = connection.execute("""SELECT title_collection, year_of_release FROM collection    
WHERE year_of_release >= 2018 AND year_of_release <=2020;
""")
print('Названия сборников, вышедших в период с 2018 по 2020 год включительно:\n', *sel, '\n')

sel = connection.execute("""SELECT name_performers FROM performers
WHERE name_performers NOT LIKE '%% %%'
""")
print('исполнители, чье имя состоит из 1 слова:\n', *sel, '\n')

sel = connection.execute("""SELECT track_name FROM tracks
WHERE track_name LIKE '%%мой%%' OR track_name LIKE '%%my%%' OR track_name LIKE '%%Мой%%' OR track_name LIKE '%%My%%';
""")
print('название треков, которые содержат слово "мой"/"my":\n', *sel, '\n')