import websocket
import json
import time
import telegram

from telegram.ext import (Updater,
                          CommandHandler,
                          CallbackQueryHandler)

bot_token = '6155355153:AAFdVi1QCj_3g4Z3Rll-0W74cZwBwnC5KH8'
chat_id = '360300829'

last_price = None
change_threshold = 0.01
timeframe = 60*60

def on_message(ws, message):
    global last_price
    data = json.loads(message)
    if data['e'] == 'kline':
        kline = data['k']
        price = float(kline['c'])
        if last_price is not None:
            price_change = (price - last_price) / last_price
            if abs(price_change) >= change_threshold:
                text = f"Price change: {price_change:.2%}"
                bot = telegram.Bot(token=bot_token)
                bot.send_message(chat_id=chat_id, text=text)
        last_price = price

def on_close(ws):
    print("Ошибка подключения.")

def start(update, context):
    bot = context.bot
    text = "Нажмите на кнопку для получения цены ETHUSDT."
    button = telegram.InlineKeyboardButton(text="Get ETHUSDT Price", callback_data="get_price")
    keyboard = telegram.InlineKeyboardMarkup([[button]])
    bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard)

def button(update, context):
    query = update.callback_query
    if query.data == "get_price":
        if last_price is not None:
            text = f"Current price of ETHUSDT futures: {last_price:.2f}"
        else:
            text = "Попробуйте позже."
        query.answer(text=text)

updater = Updater(bot_token)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()

ws = websocket.WebSocketApp('wss://stream.binance.com:9443/ws/ethusdt@kline_1m',
                            on_message=on_message,
                            on_close=on_close)
ws.run_forever()
