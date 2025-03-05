from telegram.ext import ContextTypes
from telegram import Update

from .constant import TEXT


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(TEXT)


# Recieve message from user
async def recieve_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Your message: {update.message.text}")
