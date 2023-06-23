from selenium import webdriver
import  time

class Pesquisa:
    options = webdriver.ChromeOptions()
    options.add_argument('lang=pt-br')
    print('Parte 1')
    def __init__(self):
        mensagem = "AuthenticGames"
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        self.driver.get('https://youtube.com')
        print('Parte 2')
        time.sleep(2)
        #<div class="sbib_b" id="sb_ifc50" dir="ltr">
        pesq = self.driver.find_element("xpath",'//input[@placeholder="Pesquisar"]')
        time.sleep(2)
        pesq.click()
        pesq.send_keys(mensagem)
        time.sleep(2)
        btn = self.driver.find_element("xpath",'//button[@aria-label="Pesquisar"]')
        btn.click()
        time.sleep(6)
        


openwebservice = Pesquisa()