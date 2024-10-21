"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/web/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Funções

# Função para pesquisar a cidade no Google
def pesquisar_cidade(bot, cidade):
    while len(bot.find_elements('//*[@id="APjFqb"]', By.XPATH)) < 1:
        bot.wait(1000)
        print('Carregando...')
    bot.find_element('//*[@id="APjFqb"]', By.XPATH).send_keys(cidade)
    bot.wait(1000)
    bot.enter()

# Função para extrair os dados de clima
def extrair_dados(bot):
    cont = 1  # Usado para contar os dias da previsão
    while True:
        dia_semana = bot.find_element(f'//*[@id="wob_dp"]/div[{cont}]/div[1]', By.XPATH).text
        temp_max = bot.find_element(f'//*[@id="wob_dp"]/div[{cont}]/div[3]/div[1]/span[1]', By.XPATH).text
        temp_min = bot.find_element(f'//*[@id="wob_dp"]/div[{cont}]/div[3]/div[2]/span[1]', By.XPATH).text
        
        # Exibe os dados no formato solicitado
        print(f"Dia: {dia_semana}")
        print(f"Temperatura: \n Max = {temp_max}°C / Min = {temp_min}°C")
        print("______\n")

        cont += 1
        if cont == 8:
            break

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME

    # Uncomment to set the WebDriver path
    bot.driver_path = ChromeDriverManager().install()

    # Opens the BotCity website.
    bot.browse("https://www.google.com")

    # Implement here your logic...
    try:
        pesquisar_cidade(bot, "manaus clima")
        bot.wait(1000)
        extrair_dados(bot)

    except Exception as ex:
        print(ex)
        bot.save_screenshot('erro.png')
    finally:
        bot.wait(3000)

    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
