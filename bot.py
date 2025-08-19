from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Free", callback_data='free')],
        [InlineKeyboardButton("Join", callback_data='join')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 Welcome to Ayaan Office", reply_markup=reply_markup)

# Button click handler
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'free':
        await query.edit_message_text(text="🔥 Join karo best platform hai")
    elif query.data == 'join':
        await query.edit_message_text(text="✅ Thanks for joining Ayaan Office!")

def main():
    TOKEN = os.getenv("BOT_TOKEN")  # token render se milega
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()

if __name__ == "__main__":
    main()
