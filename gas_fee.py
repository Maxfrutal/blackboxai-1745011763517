from web3 import Web3

class GasFee:
    def __init__(self, web3: Web3):
        self.web3 = web3

    def get_current_gas_fee(self):
        """
        Retorna a taxa de gás atual na rede Polygon em Gwei.
        """
        try:
            gas_price = self.web3.eth.gas_price  # em wei
            gas_price_gwei = self.web3.fromWei(gas_price, 'gwei')
            return gas_price_gwei
        except Exception as e:
            print(f"Erro ao buscar taxa de gás: {e}")
            return None

    def should_cancel_order(self, current_fee, previous_fee, max_increase_percent=20):
        """
        Verifica se a ordem deve ser cancelada com base no aumento da taxa de gás.
        """
        if previous_fee is None:
            return False
        increase = ((current_fee - previous_fee) / previous_fee) * 100
        return increase > max_increase_percent
