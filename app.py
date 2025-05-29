from flask import Flask, render_template, request
import math

app = Flask(__name__)
# Вы передаете специальную переменную __name__, которая содержит имя текущего модуля Python.
# Она указывает экземпляру его расположение. Это необходимо, так как Flask устанавливает ряд путей за кадром.
def calculate_volume(shape, dimensions, precision):
    """Вычисляет объём фигуры с заданной точностью."""

    try:
        precision = int(precision) #это будет точность
        dimensions = [float(dim) for dim in dimensions] #преобразование все размеры в числа с пл. точкой
    except (ValueError, TypeError): #если что-то не так
        return None

    volume = 0.0 #инициализируем объем

    if shape == "cube":
        a = dimensions[0] # Берем первый элемент из dimensions
        volume = a ** 3 # Куб: V = a³
    elif shape == "sphere":
        r = dimensions[0] # Берем первый элемент из dimensions
        volume = (4/3) * math.pi * r ** 3 # Шар: V = (4/3)πr³
    elif shape == "cylinder":
        r, h = dimensions[0], dimensions[1]  # Берем два элемента
        volume = math.pi * r ** 2 * h # Цилиндр: V = πr²h
    elif shape == "cone":
        r, h = dimensions[0], dimensions[1] # Берем два элемента
        volume = (1/3) * math.pi * r ** 2 * h # Конус: V = (1/3)πr²h
    else:
        return None # Если каким-то чудом передана неизвестная фигура и что-то не так
    # Округляем результат до указанной точности и возвращаем
    # Если точность отрицательная - возвращаем без округления
    return round(volume, precision) if precision >= 0 else volume
# Декоратор route указывает, какой URL будет обрабатывать эта функция
# methods=['GET', 'POST'] - разрешаем оба типа HTTP-запросов - это база, все так делают
@app.route("/", methods=["GET", "POST"])
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
    app.run(debug=True)