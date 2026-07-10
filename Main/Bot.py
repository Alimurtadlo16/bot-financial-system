from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "6415053036:AAEtgqR_uE6-O0PZ_vR_L0-eHn2xY1Z2c34"
myDompetGuweh = None


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nama_user = update.message.from_user.first_name
    await update.message.reply_text(
        f"Halo {nama_user}! Bot Finansial lo udah siap standby.\n\n"
        "Gunakan perintah berikut:\n"
        "👉 /set [angka] - Buat atur saldo awal\n"
        "👉 /keluar [angka] - Buat catat pengeluaran"
    )


async def set_saldo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global myDompetGuweh
    nama_user = update.message.from_user.first_name

    if not context.args:
        await update.message.reply_text(
            f"Format salah,!!! {nama_user}. Harusnya: /set [angka]\nContoh: /set 50000"
        )
        return

    try:
        angka_input = int(context.args[0])
        myDompetGuweh = angka_input
        await update.message.reply_text(
            f"Sip! Saldo awal {nama_user} berhasil diatur sebesar: Rp {angka_input:,}"
        )
    except ValueError:
        await update.message.reply_text(
            f"Waduh {nama_user}, yang lo masukin setelah perintah /set harus angka bulat ya!"
        )


async def keluar_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global myDompetGuweh
    nama_user = update.message.from_user.first_name

    if not context.args:
        await update.message.reply_text(
            f"Format salah, {nama_user}! Harusnya: /keluar [angka]\nContoh: /keluar 20000"
        )
        return
    if myDompetGuweh is None:
        await update.message.reply_text(
            f"Waduh {nama_user}, atur saldo awal lo dulu pake perintah /set [angka] ya!"
        )
        return

    try:
        nominal_keluar = int(context.args[0])

        if nominal_keluar > myDompetGuweh:
            await update.message.reply_text(
                f"Sisa saldo lo gak cukup, {nama_user}! Saldo saat ini cuma Rp {myDompetGuweh:,}"
            )
            return

        myDompetGuweh -= nominal_keluar
        await update.message.reply_text(
            f"Pengeluaran dicatat: Rp {nominal_keluar:,}\n"
            f"Sisa saldo {nama_user} sekarang: Rp {myDompetGuweh:,}"
        )
    except ValueError:
        await update.message.reply_text(
            f"Waduh {nama_user}, nominal pengeluaran harus berupa angka bulat!"
        )


def main():
    print("Bot lo udah standby, Li! Silakan tes di Telegram...")

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("set", set_saldo_command))
    application.add_handler(CommandHandler("keluar", keluar_command))
    application.run_polling()


if __name__ == "__main__":
    main()
