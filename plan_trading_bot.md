# Plano Detalhado para Bot de Arbitragem em Python na Rede Polygon

## Informações Coletadas

- O bot deve operar na rede Polygon, utilizando DEXs confiáveis e pares de liquidez.
- Usar USDC como moeda base para comprar e vender.
- Usar MATIC para taxas de gás.
- Buscar automaticamente os valores das criptomoedas e as taxas de gás.
- O foco principal é arbitragem: detectar diferenças de preço entre DEXs (ex: USDC a 5 reais em uma DEX e 5,45 em outra).
- Calcular lucro descontando taxas para garantir operações positivas (sem prejuízo).
- Implementar segurança:
  - Salvar dados sensíveis em arquivo `.env`.
  - Cancelar ordens se o tempo de rede ou taxa de gás aumentar muito.
  - Stop loss automático se perda ultrapassar 5%.
- Trabalhar com juros compostos nas operações.
- Integrar Telegram para notificações de operações, resultados, riscos e saldo da carteira.
- Usar emojis e timestamps nas mensagens do Telegram.
- Executar operações a cada 4 minutos.
- Auto-reiniciar o bot a cada 12 horas caso ele pare.
- Rodar 24/7 em servidor VPS.

## Plano de Implementação por Arquivo

- `.env`
  - Armazenar chaves privadas, API keys do Telegram, e outras variáveis sensíveis.
  - Incluir chave privada da carteira MetaMask.

- `config.py`
  - Carregar variáveis do `.env`.
  - Configurações gerais do bot (intervalos, limites, endereços de contratos, etc).
  - Implementar configuração para modo simulação e modo operação real.

- `dex_interface.py`
  - Funções para interagir com DEXs na Polygon (ex: Uniswap, Sushiswap).
  - Buscar preços, pares de liquidez.
  - Adaptar para suportar modo simulação (não executar ordens reais).

- `gas_fee.py`
  - Funções para buscar taxas de gás atuais na rede Polygon.
  - Monitorar variações para cancelar ordens se necessário.

- `oracle.py`
  - Implementar oráculo para buscar informações externas e ajudar a prever o mercado.
  - Integrar dados do oráculo na lógica de arbitragem.

- `arbitrage_logic.py`
  - Implementar lógica de arbitragem com juros compostos.
  - Calcular lucro líquido descontando taxas.
  - Avaliar se a operação compensa (lucro líquido positivo) antes de executar.
  - Gerenciar stop loss e controle de risco.
  - Diferenciar comportamento entre modo simulação e modo real.
  - Utilizar dados do oráculo para decisões de arbitragem.

- `telegram_bot.py`
  - Integração com Telegram para envio de mensagens.
  - Formatação com emojis e timestamps.

- `scheduler.py`
  - Agendar execução das operações a cada 4 minutos.
  - Auto-reiniciar o bot a cada 12 horas se necessário.

- `main.py`
  - Ponto de entrada do bot.
  - Inicializar componentes, carregar configurações e iniciar scheduler.

- `utils.py`
  - Funções auxiliares gerais (logs, formatação, etc).

## Dependências

- `web3.py` para interação com a blockchain Polygon.
- `python-dotenv` para carregar variáveis do `.env`.
- `requests` para chamadas HTTP (ex: APIs de taxas).
- `python-telegram-bot` para integração com Telegram.
- `schedule` ou `APScheduler` para agendamento de tarefas.
- Outras bibliotecas auxiliares conforme necessidade.

## Próximos Passos

- Confirmar o plano com o usuário.
- Criar o arquivo `.env.example` com variáveis necessárias.
- Implementar os módulos conforme o plano.
- Testar integração com Polygon e Telegram.
- Validar lógica de arbitragem e segurança.
- Preparar para rodar 24/7 em VPS.

---

Por favor, confirme se o plano está de acordo ou se deseja alguma alteração antes de eu iniciar a implementação.
