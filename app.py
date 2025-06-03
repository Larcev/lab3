from flask import Flask, render_template, request
import math
#request — нужен для обработки данных от клиента (например, из формы).
#render_template — подгружает HTML-файлы из папки templates.

app = Flask(__name__) #Создаёт объект app, который и есть веб-приложение.
# Вы передаете специальную переменную __name__, которая содержит имя текущего модуля Python.
# Она указывает экземпляру его расположение. Это необходимо, так как Flask устанавливает ряд путей за кадром.
def calculate_volume(shape, dimensions, precision):
    """Вычисляет объём фигуры с заданной точностью."""
    try:
        # Преобразуем точность в целое число
        precision = int(precision)
        # Если точность вне допустимого диапазона — сбрасываем на 2
        if precision < 0 or precision > 10:
            precision = 2
    except (ValueError, TypeError):
        # Если точность не число или пустая — тоже сбрасываем на 2
        precision = 2

    try:
        # Преобразуем размеры в числа с плавающей точкой
        dimensions = [float(dim) for dim in dimensions]
    except (ValueError, TypeError):
        return None  # Если хотя бы один из размеров некорректен

    volume = 0.0  # Инициализируем переменную объёма

    if shape == "cube":
        a = dimensions[0]
        volume = a ** 3
    elif shape == "sphere":
        r = dimensions[0]
        volume = (4 / 3) * math.pi * r ** 3
    elif shape == "cylinder":
        r, h = dimensions[0], dimensions[1]
        volume = math.pi * r ** 2 * h
    elif shape == "cone":
        r, h = dimensions[0], dimensions[1]
        volume = (1 / 3) * math.pi * r ** 2 * h
    else:
        return None  # Неподдерживаемая фигура

    return round(volume, precision)

# Декоратор route указывает, какой URL будет обрабатывать эта функция
# methods=['GET', 'POST'] - разрешаем оба типа HTTP-запросов - это база, все так делают
@app.route("/", methods=["GET", "POST"]) 
# Это маршрут: говорит Flask, что делать при заходе на URL /.
# GET — когда пользователь просто открывает страницу.
# POST — когда пользователь отправляет форму.


def index():
    """
    Основная функция, обрабатывающая главную страницу.
    Отображает форму и выводит результаты расчетов.
    """
    result = None  # Инициализируем переменную для результата
    if request.method == "POST":
        shape = request.form.get("shape") # получаем тип фигуры
        dimensions = request.form.getlist("dimensions[]") #список размеров
        precision = request.form.get("precision", default=2) #точность, без изменений будет 2 символа
        result = calculate_volume(shape, dimensions, precision) #считаем функцию выше

    # Рендерим шаблон index.html, передавая в него результат
    # Шаблон находится в папке templates/
    return render_template("index.html", result=result)

# Запускаем Flask-приложение
# debug=True включает режим отладки (автоперезагрузка при изменениях, подробные ошибки)
if __name__ == "__main__":
    app.run(debug=True) # Без app.run() Flask-приложение не запустится напрямую.
