import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Carregar variáveis do .env
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    MODE = os.getenv("MODE", "simulation")  # simulation ou real
    OPERATION_INTERVAL = int(os.getenv("OPERATION_INTERVAL", 240))  # segundos
    AUTO_RESTART_INTERVAL = int(os.getenv("AUTO_RESTART_INTERVAL", 43200))  # segundos
    DEX_CONTRACTS = os.getenv("DEX_CONTRACTS", "").split(",")  # lista de endereços

    # Configurações adicionais
    STOP_LOSS_PERCENT = 5  # percentual de stop loss
    BASE_TOKEN = "USDC"
    GAS_TOKEN = "MATIC"

config = Config()
