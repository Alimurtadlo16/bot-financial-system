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
