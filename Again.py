import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


class FinancialBot:
    def __init__(self, token: str):
        self.application = Application.builder().token(token).build()
        self.setup_handlers()

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "Halo Ali! Gue Murtadlo_bot. Siap bantu lo pantau keuangan biar nggak boncos lagi. 🚀\n\n"
            "Gunakan /pake [jumlah] [keperluan] buat catat pengeluaran lo nanti!\n"
            "Contoh: /pake 50000 beli seblak"
        )

    async def pake_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if len(context.args) < 2:
            await update.message.reply_text(
                "Format salah, Li! Contoh yang bener: /pake 50000 beli seblak"
            )
            return

        try:
            jumlah = int(context.args[0])
            keperluan = " ".join(context.args[1:])
            await update.message.reply_text(
                f"✅ Berhasil dicatat, Li!\n"
                f"💰 Jumlah: Rp {jumlah:,}\n"
                f"🛒 Keperluan: {keperluan}"
            )
        except ValueError:
            await update.message.reply_text(
                "Jumlahnya harus pake angka dong, Li! Jangan pake huruf."
            )

    def setup_handlers(self):
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("pake", self.pake_command))

    def run(self):
        print("Bot lagi jalan, Li... Coba chat /start atau /pake di Telegram!")
        self.application.run_polling()

    async def stop(self):
        await self.application.stop()
        print("Bot sudah berhenti.")


if __name__ == "__main__":
    TOKEN = "8764486282:AAFB5bPYXFbKJPdUp9Y5JmAedDLXpkGBPgU"

    bot = FinancialBot(TOKEN)
    bot.run()
