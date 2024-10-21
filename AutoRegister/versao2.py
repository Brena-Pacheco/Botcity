import pandas as pd
from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager

# Função para ler o Excel e retornar os dados dos funcionários
def ler_dados_excel(caminho_arquivo):
    try:
        df = pd.read_excel(caminho_arquivo)
        # Filtrar apenas os funcionários que ainda não foram cadastrados
        df = df[df['Status'] != 'Cadastrado']
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo Excel não encontrado no caminho {caminho_arquivo}")
        return None

# Função para atualizar o status no Excel
def atualizar_status_excel(caminho_arquivo, df):
    try:
        df.to_excel(caminho_arquivo, index=False)
        print("Arquivo Excel atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar o Excel: {e}")

# Função principal de automação
def main():
    # Caminho do arquivo Excel
    caminho_excel = r"C:\Users\Brena\Downloads\cadastro\funcionarios.xlsx"

    # Ler os dados dos funcionários
    df_funcionarios = ler_dados_excel(caminho_excel)
    if df_funcionarios is None or df_funcionarios.empty:
        print("Nenhum funcionário para cadastrar ou erro ao carregar o arquivo.")
        return

    webbot = WebBot()

    # Configuração do navegador
    webbot.headless = False
    webbot.browser = Browser.CHROME
    webbot.driver_path = ChromeDriverManager().install()

    # Acessar o Google Forms
    webbot.browse("https://forms.gle/RsScG4dLXhQwADbbA")
    webbot.wait(5000)

    # Fazer login
    webbot.enter()
    webbot.wait(2000)
    email_field = webbot.find_element('//*[@id="identifierId"]', By.XPATH)
    email_field.send_keys("brena.cidade@ifam.edu.br")
    webbot.enter()
    webbot.wait(3000)

    password_field = webbot.find_element('//*[@id="password"]/div[1]/div/div[1]/input', By.XPATH)
    password_field.send_keys("011.876.382-26")
    webbot.enter()
    webbot.wait(10000)

    # Preenchimento do formulário com os dados de cada funcionário
    for index, funcionario in df_funcionarios.iterrows():
        webbot.wait(1000)
        webbot.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH).send_keys(funcionario['Nome'])
        webbot.wait(1000)
        webbot.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH).send_keys(funcionario['E-mail'])
        webbot.wait(1000)
        webbot.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH).send_keys(funcionario['CPF'])
        webbot.wait(1000)
        webbot.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH).send_keys(funcionario['Departamento'])
        webbot.wait(1000)
        webbot.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH).send_keys(funcionario['RG'])
        webbot.wait(1000)
        webbot.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea', By.XPATH).send_keys(funcionario['Endereco'])
        webbot.wait(1000)

        # Completar com outros campos conforme necessário
        webbot.wait(2000)
        
        # Enviar o formulário
        try:
            submit_button = webbot.find_element('//*[@id="submit_button_xpath"]', By.XPATH)  # Ajuste o XPath do botão de envio
            submit_button.click()
            webbot.wait(5000)  # Espera após envio
        except Exception as e:
            print(f"Erro ao tentar clicar no botão de envio: {e}")

        # Atualizar o status para "Cadastrado"
        df_funcionarios.at[index, 'Status'] = 'Cadastrado'

    # Atualizar o Excel com os novos status
    atualizar_status_excel(caminho_excel, df_funcionarios)

    # Fechar o navegador
    webbot.stop_browser()

if __name__ == '__main__':
    main()
