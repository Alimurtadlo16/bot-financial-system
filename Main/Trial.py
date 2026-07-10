import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Setup log sistem
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

SALDO_FILE = "saldo_ali.txt"

# Fungsi membaca saldo dari file teks
def baca_saldo():
    if not os.path.exists(SALDO_FILE):
        return 0
    with open(SALDO_FILE, "r") as file:
        try:
            return int(file.read().strip())
        except:
            return 0

# Fungsi menulis saldo baru ke file teks
def simpan_saldo(jumlah):
    with open(SALDO_FILE, "w") as file:
        file.write(str(jumlah))

# 1. Perintah /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.first_name
    saldo_sekarang = baca_saldo()
    pesan = (
        f"Halo {username}! 👋\n"
        f"Saldo lo saat ini: **Rp {saldo_sekarang:,}**\n\n"
        "Cara pakai bot ini:\n"
        "• Ketik `/set [angka]` buat atur/tambah saldo awal. Contoh: `/set 200000`\n"
        "• Ketik langsung chat biasa angka pengeluaran lo buat motong saldo. Contoh: `10000` atau `500`\n"
    )
    await update.message.reply_text(pesan, parse_mode="Markdown")

# 2. Perintah /set untuk atur saldo awal
async def set_saldo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Mengambil angka setelah kata /set
        jumlah = int(context.args[0])
        simpan_saldo(jumlah)
        await update.message.reply_text(f"💰 Mantap! Saldo awal lo berhasil diatur jadi: **Rp {jumlah:,}**", parse_mode="Markdown")
    except (IndexError, ValueError):
        await update.message.reply_text("⚠️ Format salah! Contoh yang bener: `/set 200000`")

# 3. Logika membaca chat teks biasa (Pengeluaran)
async def baca_pengeluaran(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teks_chat = update.message.text.strip()
    
    # Cek apakah isinya angka murni atau bukan
    if teks_chat.isdigit():
        biaya = int(teks_chat)
        saldo_lama = baca_saldo()
        
        if saldo_lama >= biaya:
            saldo_baru = saldo_lama - biaya
            simpan_saldo(saldo_baru)
            
            respon = (
                f"💸 **Pengeluaran dicatat:** Rp {biaya:,}\n"
                f"📉 **Sisa saldo lo sekarang:** Rp {saldo_baru:,}\n\n"
                "Awas boncos, kurangi jajan gak penting! 🧠"
            )
        else:
            respon = f"⚠️ **Dompet Jebol, Li!** Saldo lo cuma Rp {saldo_lama:,}, gak cukup buat bayar Rp {biaya:,}. Sadar diri yuk!"
            
        await update.message.reply_text(respon, parse_mode="Markdown")
    else:
        # Kalau Ali ketik teks biasa bukan angka murni
        await update.message.reply_text("🤖 Gue cuma paham angka murni sekarang, Li. Ketik nominal pengeluaran lo aja (contoh: `10000`).")

def main():
    TOKEN = "8764486282:AAFB5bPYXFbKJPdUp9Y5JmAedDLXpkGBPgU"
    
    print("Bot versi 2 sedang berjalan...")
    app = Application.builder().token(TOKEN).build()
    
    # Handler perintah
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("set", set_saldo_command))
    
    # Handler teks chat biasa (menggunakan MessageHandler)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, baca_pengeluaran))
    
    app.run_polling()

if __name__ == '__main__':
    main()