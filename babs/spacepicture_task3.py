import requests
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

# URL API, которое возвращает картинку
image_url = "https://api.nasa.gov/planetary/apod?api_key=" + "FOeCmPAedw5YUQ48iUKEOtVLeZqyLbLOwjYKu2vh"  # замените на реальный URL API

# Отправляем GET-запрос
response = requests.get(image_url, stream=True)

# Проверяем успешность запроса
if response.status_code == 200:
    son = response.json()
else:
    print(f"Ошибка: {response.status_code}")

picture = son["url"]
print(son["url"])

p = requests.get(picture)
out = open("image.jpg", "wb")
out.write(p.content)
out.close()

root = tk.Tk()
root.title("Картинка дня от NASA")

# Загружаем изображение
# Убедитесь, что файл image.png находится в той же директории, что и скрипт
# Или укажите полный путь к файлу
try:
    image = ImageTk.PhotoImage(file="image.jpg")
except:
    print("Не удалось загрузить изображение. Проверьте путь и формат файла.")
    exit()

# Создаем виджет для отображения изображения
label = tk.Label(root, image=image)
label.pack()

# Запускаем главный цикл
root.mainloop()
