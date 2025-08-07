from multiprocessing import context
import re
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import step 
from behave import register_type
import parse


import time


@parse.with_pattern(r'.*')
def parse_any_string(text):
    return text

register_type(anystr=parse_any_string)

def digitar_com_calma(element, texto, delay=0.1):
    for letra in texto:
        element.send_keys(letra)
        time.sleep(delay)

@given('que o usuário está na página de login')
def step_open_login_page(context):
    print ("STEP:Entrou no GIVEN")
    context.driver.get('https://www.saucedemo.com/')
    

@when('ele preenche o nome de usuário "{username}" e a senha "{password}"')
@when('ele preenche o nome de usuário "" e a senha "{password}"')
@when('ele preenche o nome de usuário "{username}" e a senha ""')
@when('ele preenche o nome de usuário "" e a senha ""')
def step_fill_credentials(context, username="", password=""):
    print(f"STEP: Preenchendo usuário: '{username}' | senha: '{password}'")

    wait = WebDriverWait(context.driver, 10)

    campo_usuario = wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
    campo_senha = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    botao_login = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))

    campo_usuario.clear()
    digitar_com_calma(campo_usuario, username)

    campo_senha.clear()
    digitar_com_calma(campo_senha,password)

    time.sleep(0.5)
    botao_login.click()


@then('ele deve ser redirecionado para a página de produtos')
def step_check_products_page(context):
    print("STEP: Verificando se está na página de produtos")
    assert "inventory" in context.driver.current_url
    time.sleep(5)
  


@then('ele deve ver uma mensagem de erro')
def step_ver_mensagem_erro(context):
    print("STEP: Entrou em Then invalido")
    time.sleep(2)
    erro = context.driver.find_element(By.CLASS_NAME, "error-message-container")
    mensagem = erro.text
    print("Mensagem de erro exibida:", mensagem)
    assert "Epic sadface" in mensagem or "Username and password" in mensagem
    
    
