import streamlit as st
from PIL import Image # Для картинок
import numpy as np # Для имитации модельки


# 1. Настройка страницы (делаем красиво сразу)
st.set_page_config(page_title="Image Classifier", layout="centered")

# 2. Заголовок и описание
st.title("🖼 Классификатор изображений")
st.write("Загрузите фото, чтобы для классификации")


# Загрузка модели, кешируется, чтобы не грузить при каждом чихе
# @st.cache_resource
# def load_model():
#     # Здесь ребята будут загружать свои веса:
#     # model = torch.load('model.pth')
#     # model.eval()
#     return "Модель загружена!"


# model = load_model()


# --- ЛОГИКА ПРЕДСКАЗАНИЯ ---
# def predict(image):
#     """
#     Место для магии ML.
#     image — это объект PIL Image.
#     """
#     # Пример препроцессинга (изменить размер под вход модели):
#     img_resized = image.resize((224, 224))
#
#     # Имитация работы модели (заменить на реальный вызов)
#     # prediction = model(img_resized)
#     confidence = np.random.random()  # Рандом для примера
#     label = "Кот 🐱" if confidence > 0.5 else "Собака 🐶"
#
#     return label, confidence


# uploaded_file = st.file_uploader("Выберите картинку...", type=["jpg", "jpeg", "png"])
#
# if uploaded_file is not None:
#     # Отображаем загруженное изображение
#     image = Image.open(uploaded_file)
#
#     # Создаем две колонки для интерфейса
#     col1, col2 = st.columns(2)
#
#     with col1:
#         st.image(image, caption='Ваше фото', use_container_width=True)
#
#     with col2:
#         st.write("### Результат анализа")
#         if st.button('Классифицировать'):
#             with st.spinner('Думаю...'):
#                 label, score = predict(image)
#
#                 # Красивый вывод результата
#                 st.success(f"Это **{label}**")
#                 st.metric(label="Уверенность", value=f"{score:.2%}")
#
#                 # Можно добавить прогресс-бар для наглядности
#                 st.progress(score)
# else:
#     st.info("💡 Подсказка: загрузите файл формата JPG или PNG в поле выше.")

# Красивая подпись
st.divider()
st.caption("Developed for you. Yes, exactly | Hackathon 2026")


from pathlib import Path

# Получаем путь к текущему файлу
BASE_DIR = Path(__file__).resolve().parent

# Добавляем к модели внутри папки проекта
MODEL_PATH = BASE_DIR / "models" / "weights.pth"

# MODEL_PATH поймет любая ОС
st.write(f"Загружаю модель из: {MODEL_PATH}")