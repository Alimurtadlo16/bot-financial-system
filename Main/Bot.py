from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


class PengeluaranHarian:
    def __init__(self, name, saldoAwal):
        self.__name = name
        self.__saldoSaatIni = saldoAwal

    def penguranganTransaksi(self, expense):
        self.__saldoSaatIni = self.__saldoSaatIni - expense
        return self.__saldoSaatIni


myDompetGuweh = None


async def set_saldo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global myDompetGuweh
    nama_user = update.effective_user.first_name
    angka_input = int(context.args[0])
    myDompetGuweh = PengeluaranHarian(name=nama_user, saldoAwal=angka_input)
    await update.message.reply_text(
        f"Saldo awal {nama_user} diatur sebesar {angka_input}"
    )


async def keluar_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global myDompetGuweh
    if myDompetGuweh is None:
        await update.message.reply_text(
            "Belum ada saldo yang diatur. Silakan atur saldo terlebih dahulu."
        )
        return
    angka_input = int(context.args[0])
    saldo_terbaru = myDompetGuweh.penguranganTransaksi(angka_input)
    await update.message.reply_text(f"Saldo terbaru: {saldo_terbaru}")


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo Ali Murtadlo! Bot Finansial lo udah siap. Pake ./set --nominal-- buat mulai ya!"
    )


def main():
    TOKEN = "8764486282:AAFB5bPYXFbKJPdUp9Y5JmAedDLXpkGBPgU"

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("set", set_saldo_command))
    application.add_handler(CommandHandler("keluar", keluar_command))

    print("Bot lo udah standby, Li! Silakan tes di Telegram...")
    application.run_polling()


if __name__ == "__main__":
    main()
