# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for the Web Bot
from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False 


# Excel file path (updated)
EXCEL_FILE_PATH = 'C:\\Users\\matutino\\Desktop\\BotCity\\AutoRegisterBot\\funcionarios.xlsx'

# Função para realizar o clique
def clique():
    bot.click()

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")


    desktop_bot = DesktopBot()

    # Execute operations with the DesktopBot as desired
    # desktop_bot.control_a()
    # desktop_bot.control_c()
    # value = desktop_bot.get_clipboard()

    webbot = WebBot()

    # Configure whether or not to run on headless mode
    webbot.headless = False

    # Uncomment to change the default Browser to Firefox
    webbot.browser = Browser.CHROME


    # Uncomment to set the WebDriver path
    webbot.driver_path = ChromeDriverManager().install()

    # Opens the Google Forms URL.
    webbot.browse("https://forms.gle/RsScG4dLXhQwADbbA")

    # Wait for the page to load
    webbot.wait(5000)

    # Fill in the email field

    webbot.enter()
    webbot.wait(2000)
    email_field = webbot.find_element('//*[@id="identifierId"]', By.XPATH)
    email_field.send_keys("brena.cidade@ifam.edu.br")
    webbot.wait(2000)
    #webbot.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys("\n")  # Simulate pressing Enter
    webbot.enter()

    # Wait for the password field to load
    webbot.wait(3000)

    # Fill in the password field
    password_field = webbot.find_element('//*[@id="password"]/div[1]/div/div[1]/input', By.XPATH)
    password_field.send_keys("011.876.382-26")
    webbot.wait(2000)
    #webbot.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("\n")  # Simulate pressing Enter
    webbot.enter()

    # Wait for the form to load completely after login (if applicable)
    webbot.wait(10000)

    # Read the Excel file into a DataFrame
    df = pd.read_excel(EXCEL_FILE_PATH)

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Check if the employee is already registered
        if row['Status'] == 'Cadastrado':
            continue

        # Find and fill the form fields (adjust XPaths as needed)
        nome_completo_field = webbot.find_element(By.XPATH, '//input[@aria-label="Nome Completo"]') 
        nome_completo_field.send_keys(row['Nome Completo'])

        cargo_field = webbot.find_element(By.XPATH, '//input[@aria-label="Cargo"]') 
        cargo_field.send_keys(row['Cargo'])

        departamento_field = webbot.find_element(By.XPATH, '//input[@aria-label="Departamento"]') 
        departamento_field.send_keys(row['Departamento'])

        data_admissao_field = webbot.find_element(By.XPATH, '//input[@aria-label="Data de Admissão"]') 
        data_admissao_field.send_keys(row['Data de Admissão'])

        # Seleciona o Turno
        turno_imagem = {
            'Primeiro': 'primeiro_turno',
            'Segundo': 'segundo_turno',
            'Comercial': 'comercial_turno'
        }.get(funcionario['Turno'])  # Use 'Turno' em vez de 'turno'

        if not bot.find(turno_imagem, matching=0.97, waiting_time=10000):
            not_found("Turno option")
        else:
            clique()  # Chama a função clique aqui

        # Submit the form
        submit_button = webbot.find_element(By.XPATH, '//span[text()="Enviar"]')
        submit_button.click()

        # Update the status in the DataFrame
        df.at[index, 'Status'] = 'Cadastrado'

        # Save the updated DataFrame back to the Excel file
        df.to_excel(EXCEL_FILE_PATH, index=False)

        # Navigate back to the form for the next entry
        webbot.back()
        webbot.wait(5000)  # Wait for the form to reload

    # Wait 3 seconds before closing
    webbot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    webbot.stop_browser()

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
