from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import random

# Вставь сюда токен от BotFather
TOKEN = "8308922837:AAGbmkjhcgyyqGDkjC9nDLo4oHZVRwvPSlk"

# -------------------- Команды --------------------

# /start — приветствие
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот, готов выполнять команды!")

# /help — список команд
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    commands = """
Список доступных команд:
/start — приветствие
/help — список команд
/ping — проверка бота
/say <текст> — повторяет текст
/time — показывает текущее время
/roll — кидает виртуальный кубик (1-6)
"""
    await update.message.reply_text(commands)

# /ping — проверка бота
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pong!")

# /say <текст> — повторяет текст
async def say(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = " ".join(context.args)
    if message:
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("Ты не написал, что сказать!")

# /time — текущее время
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    await update.message.reply_text(f"Текущее время: {now}")

# /roll — виртуальный кубик
async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = random.randint(1, 6)
    await update.message.reply_text(f"Выпало число: {number}")

# -------------------- Настройка бота --------------------

app = ApplicationBuilder().token(TOKEN).build()

# Регистрируем команды
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("ping", ping))
app.add_handler(CommandHandler("say", say))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("roll", roll))

# Запуск бота
app.run_polling()
