import time
from web3 import Web3
from config import config
from dex_interface import DexInterface
from gas_fee import GasFee
from oracle import Oracle
from arbitrage_logic import ArbitrageLogic
from telegram_bot import TelegramBot
from scheduler import Scheduler
from utils import setup_logger

logger = setup_logger()

def main_task():
    web3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com"))
    dex = DexInterface(web3)
    gas_fee = GasFee(web3)
    oracle = Oracle()
    arbitrage = ArbitrageLogic(dex, gas_fee, oracle)
    telegram = TelegramBot()

    # Exemplo de pares para arbitragem (endereços fictícios)
    pair_addresses = config.DEX_CONTRACTS

    success = arbitrage.execute_arbitrage(config.BASE_TOKEN, pair_addresses, simulation=(config.MODE=="simulation"))

    if success:
        message = telegram.format_trade_message(profit="positivo", risk_level="baixo", balance="1000 USDC")
    else:
        message = "Nenhuma operação executada ou lucro insuficiente."

    telegram.send_message(message)

def start_bot():
    scheduler = Scheduler(main_task, config.OPERATION_INTERVAL)
    scheduler.start()
    logger.info("Bot iniciado e agendado.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        scheduler.stop()
        logger.info("Bot parado manualmente.")

if __name__ == "__main__":
    start_bot()
