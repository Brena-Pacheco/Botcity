

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for the Web Bot
from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

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

    # Opens the BotCity website.
    webbot.browse("https://forms.gle/RsScG4dLXhQwADbbA")

    # Implement here your logic...
    # Wait for the page to load
    webbot.wait(5000)

    # Fill in the email field
    
    webbot.enter()
    webbot.wait(2000)
    email_field = webbot.find_element('//*[@id="identifierId"]', By.XPATH)
    email_field.send_keys("hercules.freitas@ifam.edu.br")
    webbot.wait(2000)
    #webbot.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys("\n")  # Simulate pressing Enter
    webbot.enter()

    # Wait for the password field to load
    webbot.wait(3000)

    # Fill in the password field
    password_field = webbot.find_element('//*[@id="password"]/div[1]/div/div[1]/input', By.XPATH)
    password_field.send_keys("845.108.112-68")
    webbot.wait(2000)
    #webbot.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("\n")  # Simulate pressing Enter
    webbot.enter()

    # Wait for the form to load
    webbot.wait(10000)

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
