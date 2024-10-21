# Import for the Web Bot
from botcity.web import WebBot, Browser
import requests
import mysql.connector
from webdriver_manager.chrome import ChromeDriverManager

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def obter_cotacao_dolar():
    # Obtendo a cotação do dólar da API
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    response = requests.get(url)
    data = response.json()
    
    # Retorna o valor "high" da cotação do dólar
    return float(data['USDBRL']['high'])

def atualizar_preco_dolar(cotacao_dolar):
    # Conectando ao banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Insira sua senha do MySQL aqui
        database="banco"
    )
    
    cursor = conexao.cursor()

    # Consultando todos os produtos
    cursor.execute("SELECT id, preco_real FROM produto")
    produtos = cursor.fetchall()

    # Atualizando o preço em dólar
    for produto in produtos:
        id_produto = produto[0]
        preco_real = float(produto[1])  # Convertendo DECIMAL para float
        preco_dolar = preco_real * cotacao_dolar

        cursor.execute("UPDATE produto SET preco_dolar = %s WHERE id = %s", (preco_dolar, id_produto))

    conexao.commit()
    cursor.close()
    conexao.close()

def main():
    # Runner passes the server URL, task id, and access token
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID: {execution.task_id}")
    print(f"Task Parameters: {execution.parameters}")

    bot = WebBot()

    # Configurando para rodar em modo não headless (com navegador visível)
    bot.headless = False

    # Configurando o browser como Chrome (usando msedge-selenium-tools no caso de Edge)
    bot.browser = Browser.CHROME
    
    bot.driver_path = ChromeDriverManager().install()

    # Abre o navegador para acessar o site de cotação (a página é apenas ilustrativa aqui)
    bot.browse("https://economia.awesomeapi.com.br/last/USD-BRL")

    # Obtendo cotação do dólar
    cotacao_dolar = obter_cotacao_dolar()
    print(f"Cotação do dólar obtida: {cotacao_dolar}")

    # Atualizando o preço dos produtos no banco de dados
    atualizar_preco_dolar(cotacao_dolar)
    print("Preços em dólar atualizados com sucesso.")

    # Espera 3 segundos antes de fechar
    bot.wait(3000)

    # Finaliza e limpa o navegador
    bot.stop_browser()

    # Marca a tarefa como finalizada no BotMaestro
    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Task Finished OK."
    )

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
