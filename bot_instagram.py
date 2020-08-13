from selenium import webdriver
import time

class insta_bot:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        self.driver.get(f'https://instagram.com/'), time.sleep(4)

    def logar(self):
        #caixa de login / por login
        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(self.login)

        time.sleep(1)

        #caixa de senha / por senha
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(self.senha)

        #botão entrar
        self.driver.find_element_by_xpath('//button[@type="submit"]') \
            .click()

    def alvo(self, user):
        #perfil alvo
        time.sleep(4)
        self.driver.get(f'https://www.instagram.com/{user}')

        #seguidores do alvo
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        time.sleep(3)

        #seguir/rolagem
        cont = 0
        rolagem = False
        while True:
            try: #verifica se há botão de seguir
                self.driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF")

            except: #se não houver botão de seguir
                print('já seguindo...')
                rolagem = True

            else: #se haver botão de seguir
                self.driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF").click()
                print('--> Seguiu!!!')
                cont += 1
                time.sleep(3)

            if rolagem: #rolagem da barra de seguidores
                seguidores = self.driver.find_element_by_xpath("//div[@class='isgrP']")
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', seguidores)


bot = insta_bot('teste00bot', 'bot@teste01')
bot.logar()
bot.alvo('how_comic')
