// Находим элемент <select id="shape"> — это выпадающий список с фигурами
document.getElementById("shape").addEventListener("change", function () {
    const shape = this.value; // Получаем текущее выбранное значение ("cube", "sphere", "cylinder" или "cone")
    
    const dimensionsDiv = document.getElementById("dimensions-input"); 
    // Контейнер, куда будут вставляться поля для ввода параметров (например, радиуса или высоты)

    dimensionsDiv.innerHTML = ""; 
    // Очищаем контейнер от старых полей, если пользователь уже что-то выбирал раньше

    // В зависимости от выбранной фигуры — вставляем соответствующие поля
    if (shape === "cube") {
        // Куб — нужно только одно поле: сторона a
        dimensionsDiv.innerHTML = '<label>Сторона (a): <input type="number" name="dimensions[]" step="any" required></label>';
    } else if (shape === "sphere") {
        // Шар — нужно одно поле: радиус r
        dimensionsDiv.innerHTML = '<label>Радиус (r): <input type="number" name="dimensions[]" step="any" required></label>';
    } else if (shape === "cylinder" || shape === "cone") {
        // Цилиндр или конус — нужно два поля: радиус и высота
        dimensionsDiv.innerHTML = `
            <label>Радиус (r): <input type="number" name="dimensions[]" step="any" required></label>
            <label>Высота (h): <input type="number" name="dimensions[]" step="any" required></label>
        `;
    }
});
