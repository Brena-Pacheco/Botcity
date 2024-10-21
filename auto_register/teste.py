from botcity.web import WebBot, By

def main():
    webbot = WebBot()
    webbot.headless = False  # Para ver o navegador enquanto o bot executa

    # Abrir o formulário Google
    webbot.browse("https://forms.gle/RsScG4dLXhQwADbbA")

    # Esperar até que a página carregue completamente
    webbot.wait(5000)

    # Preencher o campo de email
    email_field = webbot.find_element(By.XPATH, '//input[@type="email"]')
    email_field.send_keys("teamargus.zlacademy@gmail.com")
    webbot.find_element(By.XPATH, '//input[@type="email"]').send_keys("\n")  # Simular Enter

    # Esperar o campo de senha carregar
    webbot.wait(3000)

    # Preencher o campo de senha
    password_field = webbot.find_element(By.XPATH, '//input[@type="password"]')
    password_field.send_keys("#123456789Abc")
    webbot.find_element(By.XPATH, '//input[@type="password"]').send_keys("\n")  # Simular Enter

    # Esperar o formulário carregar
    webbot.wait(5000)

    # Preencher o formulário
    # Exemplo para preencher um campo de texto
    text_field = webbot.find_element(By.XPATH, '//input[@type="text"]')
    text_field.send_keys("Resposta do campo de texto")

    # Exemplo para selecionar uma opção de múltipla escolha
    multiple_choice_option = webbot.find_element(By.XPATH, '//div[@role="radio" and contains(text(), "Opção 1")]')
    multiple_choice_option.click()

    # Submeter o formulário
    submit_button = webbot.find_element(By.XPATH, '//span[text()="Enviar"]')
    submit_button.click()

    # Esperar para garantir que o envio foi concluído
    webbot.wait(5000)

    # Finalizar a sessão do navegador
    webbot.stop_browser()

if __name__ == '__main__':
    main()
