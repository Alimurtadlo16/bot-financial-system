class PengeluaranHarian:
    def __init__(self, name, saldoAwal):
        self.__name = name
        self.__saldoSaatIni = saldoAwal

    def penguranganTransaksi(self, expense):
        self.__saldoSaatIni = self.__saldoSaatIni - expense
        return self.__saldoSaatIni

myDompetGuweh = None

async def set_saldo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Kita panggil variabel global di luar tadi biar bisa diisi di dalam fungsi ini
    global myDompetGuweh 
    
    nama_user = update.effective_user.first_name
    angka_input = int(context.args[0])
    
    # NAH! Di sinilah objek itu baru dibuat secara nyata pake data dari Telegram!
    myDompetGuweh = PengeluaranHarian(name=nama_user, saldoAwal=angka_input)
    
    # Kasih feedback ke chat Telegram lo
    await update.message.reply_text(f"Saldo awal {nama_user} diatur sebesar {angka_input}")