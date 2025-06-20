import sqlite3


def init_db():
    conn = sqlite3.connect('car_rental.db')
    c = conn.cursor()

    # Создание таблицы автомобилей
    c.execute('''CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        марка TEXT,
        номер TEXT,
        цвет TEXT,
        год_выпуска INTEGER,
        модель TEXT,
        взял TEXT,
        дата TEXT,
        цена_проката INTEGER
    )''')

    # Создание таблицы пользователей
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT UNIQUE,
        password TEXT,
        created_at TEXT
    )''')

    # Проверка, пустая ли таблица cars
    c.execute("SELECT COUNT(*) FROM cars")
    if c.fetchone()[0] == 0:
        # Вставка начальных данных об автомобилях
        cars_data = [
            (
            'Toyota', 'А 001 АА 116', 'белый', 2019, 'Toyota Camry', 'Иванов Иван Иванович', '15 апреля 2023 г.', 3000),
            ('BMW', 'Е444МО', 'синий', 2020, '5 series', 'Андрей Ковальчук Андреевич', '27 мая 2023', 3500),
            ('Mercedes-Benz', 'М666АА', 'черный', 2021, 'E-Class', 'Мария Мачо Мариевна', '2023-04-28', 4000),
            ('Ford', 'Е777МР', 'Синий', 2020, 'Ford Focus', 'Петров Петр Петрович', '12.06.2023', 2500),
            ('Honda', 'М444ОР', 'Черный', 2021, 'Honda Civic', 'Сидоров Сидор Сидорович', '23.07.2023', 3000),
            ('BMW', 'О123КК', 'Белый', 2022, 'BMW X5', 'Кузнецова Ольга Ивановна', '04.08.2023', 3000),
            ('Toyota', 'А001ВС', 'Красный', 2019, 'Toyota Camry', 'Иванов Иван Иванович', '01.05.2023', 2000)
        ]
        c.executemany(
            'INSERT INTO cars (марка, номер, цвет, год_выпуска, модель, взял, дата, цена_проката) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            cars_data)

    conn.commit()
    conn.close()