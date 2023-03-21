#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
from time import sleep as sl

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
from time import sleep as sl


servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)



# Passo 1: Entrar no navegador
navegador.get("https://app.cocobambu.com/entrar?backPage=on-boarding%2Fdelivery%3FnextPage%3D%252Fdelivery")

navegador.maximize_window()

# passo 2: Clicar em "Casdastre-se"
navegador.find_element('xpath', '//*[@id="content"]/app-login/div/div/div[3]/ion-col[1]/span[2]').click()

# Passo 3: Inserior o nome completo na aba cadastre-se
navegador.find_element('xpath', '//*[@id="name"]/input').send_keys("Thalles Pereira da Silva Santos")


# Passo 4: Inserir o e-mail de cadastro
navegador.find_element('xpath', '/html/body/app-root/ion-app/div/div/desktop-modal/div[2]/register-popup/div/form/div[3]/ion-input/input').send_keys("cocobambu@uorak.com")

# Passo 5: Inserir a senha 
navegador.find_element('xpath', '//*[@id="formRegisterUser"]/div[5]/ion-input/input').send_keys("Cb61*2023")

# Passo 6: Confirmar senha
navegador.find_element('xpath', '//*[@id="formRegisterUser"]/div[7]/ion-input/input').send_keys("Cb61*2023")

sl(3)

# Passo 7: clicar no botão Selecionar seu Estado
navegador.find_element('xpath', '//*[@id="formRegisterUser"]/div[9]').click()

sl(3)

# Passo 8: Selecionar seu Estado
espera1 = (By.XPATH,'/html/body/app-root/ion-app/ion-action-sheet/div[2]/div/div[1]/button[8]')
         
element = WebDriverWait(navegador, 30).until(EC.element_to_be_clickable(espera1)) 
element.click()


# Passo 9: Clicar na opção de notificação personalizadas
navegador.find_element('xpath', '/html/body/app-root/ion-app/div/div/desktop-modal/div[2]/register-popup/div/form/div[11]/ion-item[1]/ion-checkbox').click()

# Passo 10: Aceitar os termos e condições de uso
navegador.find_element('xpath', '//html/body/app-root/ion-app/div/div/desktop-modal/div[2]/register-popup/div/form/div[11]/ion-item[2]').click()

sl(3)
# Passo 11: Aceitar
navegador.find_element('xpath', '//*[@id="content"]/terms-and-conditions/base-button/button').click()


# Passo 12: Cadastrar usuário
navegador.find_element('xpath', '/html/body/app-root/ion-app/div/div/desktop-modal/div[2]/register-popup/div/div[1]/button').click()


# Passo 13: Fechar dialog de código enviado para o e-mail
espera1 = (By.XPATH,'/html/body/app-root/ion-app/div/div/desktop-modal/div/email-spam-popup/div/div/base-button/button')
         
element = WebDriverWait(navegador, 30).until(EC.element_to_be_clickable(espera1)) 
element.click()


# In[ ]:




