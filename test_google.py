import requests  # Подключаем библиотеку-почтальона


def test_google_status():
    # 1. Отправляем курьера (GET-запрос) на сайт Google
    response = requests.get("https://www.google.com")

    # 2. Смотрим, какой код ответа привез курьер
    # 200 - это международный код "Всё ОК"
    # assert проверяет: правда ли код равен 200?
    assert response.status_code == 200