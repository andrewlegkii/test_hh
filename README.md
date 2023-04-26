# Описание работы кода

Данный код создает Telegram бота, который будет получать цену фьючерса ETHUSDT от биржи Binance каждые 60 секунд и оповещать пользователя в случае изменения цены на 1% и более. Бот будет отправлять цену пользователю, как в приватном чате, так и при использовании специальной кнопки "Get ETHUSDT Price".

# Запуск бота

1. Клонируйте себе репозиторий: git clone https://github.com/andrewlegkii/test_hh.git
2. Создайте и активируйте виртуальное окружение: python -m venv venv / source venv/Scripts/activate
3. Измените поля: bot_token и chat_id в eth.py
4. Установить все библиотеки: pip install -r requirements.txt
5. Запуск бота с помощью: python eth.py
6. @test_work_int_bot - проверка работоспособности.


