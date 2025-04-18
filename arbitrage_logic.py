from config import config

class ArbitrageLogic:
    def __init__(self, dex_interface, gas_fee, oracle):
        self.dex = dex_interface
        self.gas_fee = gas_fee
        self.oracle = oracle
        self.previous_gas_fee = None

    def calculate_net_profit(self, buy_price, sell_price, gas_cost):
        """
        Calcula o lucro líquido descontando o custo do gás.
        """
        gross_profit = sell_price - buy_price
        net_profit = gross_profit - gas_cost
        return net_profit

    def should_execute_trade(self, net_profit):
        """
        Decide se a operação deve ser executada com base no lucro líquido.
        """
        return net_profit > 0

    def execute_arbitrage(self, token_symbol, pair_addresses, simulation=True):
        """
        Executa a lógica de arbitragem:
        - Busca preços em diferentes DEXs
        - Calcula lucro líquido descontando taxas
        - Verifica se compensa executar
        - Executa ou simula a operação
        """
        # Exemplo simplificado
        prices = []
        for pair in pair_addresses:
            price = self.dex.get_price(token_symbol, pair)
            if price is not None:
                prices.append((pair, price))

        if len(prices) < 2:
            print("Não há pares suficientes para arbitragem.")
            return False

        # Encontrar menor preço para comprar e maior para vender
        buy_pair, buy_price = min(prices, key=lambda x: x[1])
        sell_pair, sell_price = max(prices, key=lambda x: x[1])

        # Buscar taxa de gás atual
        current_gas_fee = self.gas_fee.get_current_gas_fee()
        if self.previous_gas_fee is not None:
            if self.gas_fee.should_cancel_order(current_gas_fee, self.previous_gas_fee):
                print("Taxa de gás aumentou muito, cancelando operação.")
                return False
        self.previous_gas_fee = current_gas_fee

        # Calcular custo do gás em termos monetários (simplificado)
        gas_cost = current_gas_fee * 0.000001  # Ajustar conforme valor real

        net_profit = self.calculate_net_profit(buy_price, sell_price, gas_cost)
        print(f"Lucro líquido estimado: {net_profit}")

        if not self.should_execute_trade(net_profit):
            print("Operação não compensa, não executando.")
            return False

        # Executar ou simular compra e venda
        if simulation:
            print(f"Simulação: Comprar em {buy_pair} por {buy_price} e vender em {sell_pair} por {sell_price}")
        else:
            print(f"Executando arbitragem: Comprar em {buy_pair} por {buy_price} e vender em {sell_pair} por {sell_price}")
            self.dex.execute_trade(config.BASE_TOKEN, token_symbol, 1, simulation=False)  # Exemplo quantidade 1
            self.dex.execute_trade(token_symbol, config.BASE_TOKEN, 1, simulation=False)

        return True
