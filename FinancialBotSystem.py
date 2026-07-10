from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


class FinancialBot:
    def __init__(self, token: str):
        # Constructor: Inisialisasi bot dengan token lo
        self.application = Application.builder().token(token).build()
        self.setup_handlers()

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        # Method buat ngerespon perintah /start
        await update.message.reply_text(
            "Halo Ali! Gue Murtadlo_bot. Siap bantu lo pantau keuangan biar nggak boncos lagi. 🚀\n\n"
            "Gunakan /pake [jumlah] [keperluan] buat catat pengeluaran lo nanti!"
        )

    def setup_handlers(self):
        # Daftarkan command ke bot
        self.application.add_handler(CommandHandler("start", self.start_command))

    def run(self):
        # Jalankan bot secara real-time (Polling)
        print("Bot lagi jalan, Li... Coba chat /start di Telegram!")
        self.application.run_polling()

    def stop(self):
        # Hentikan bot
        self.application.stop()
        print("Bot sudah berhenti.")


if __name__ == "__main__":
    # GANTI STRING DI BAWAH INI PAKE TOKEN LO
    TOKEN = "8764486282:AAFB5bPYXFbKJPdUp9Y5JmAedDLXpkGBPgU"

    bot = FinancialBot(TOKEN)
    bot.run()
