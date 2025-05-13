from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

SITE_LINKI = "https://heylink.me/bayjguvenilirsite"  # ← buraya kendi linkini yaz

async def site_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.strip().lower() == "!site":
        mesaj = "Bay J tarafından test edildi"
        buton = [[InlineKeyboardButton("Güvenilir Siteler", url=SITE_LINKI)]]
        klavye = InlineKeyboardMarkup(buton)
        await update.message.reply_text(mesaj, reply_markup=klavye)

# 🟡 Değişiklik burada: token artık ortam değişkeninden geliyor
BOT_TOKEN = os.environ["BOT_TOKEN"]

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, site_handler))
    print("Bot çalışıyor...")
    app.run_polling()
