from telegram import Bot
from telegram.utils.request import Request
from config import config
import datetime

class TelegramBot:
    def __init__(self):
        request = Request(con_pool_size=8)
        self.bot = Bot(token=config.TELEGRAM_BOT_TOKEN, request=request)
        self.chat_id = config.TELEGRAM_CHAT_ID

    def send_message(self, message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message_with_time = f"{timestamp} ⏰\n{message}"
        try:
            self.bot.send_message(chat_id=self.chat_id, text=message_with_time)
        except Exception as e:
            print(f"Erro ao enviar mensagem no Telegram: {e}")

    def format_trade_message(self, profit, risk_level, balance):
        emojis = {
            "profit": "💰",
            "risk": "⚠️",
            "balance": "💼"
        }
        message = (
            f"{emojis['profit']} Lucro estimado: {profit}\n"
            f"{emojis['risk']} Nível de risco: {risk_level}\n"
            f"{emojis['balance']} Saldo da carteira: {balance}"
        )
        return message
