# Projeto de Teste Automatizado - SauceDemo

## Descrição
Este projeto contém testes automatizados para a aplicação SauceDemo utilizando Selenium WebDriver e Behave (BDD).  
O objetivo é validar os principais fluxos de login, tanto com credenciais válidas quanto inválidas, garantindo a qualidade da aplicação.

## Tecnologias Utilizadas
- Python 3.x  
- Selenium WebDriver  
- Behave (BDD)  
- Allure (relatórios de testes)  
- Git / GitHub  

## Estrutura do Projeto
/features # Cenários e arquivos .feature (BDD)
/steps # Implementação dos passos dos testes
/screenshots # Prints de falhas para análise
/environment.py # Configurações de ambiente para os testes


## Como Executar os Testes

1. Clone o repositório:  
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

## Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux / macOS  
venv\Scripts\activate         # Windows

## Instale as dependencias

pip install -r requirements.txt


## Execute os testes com Behave

behave


## Gere o relatório com Allure (se configurado)

allure serve ./reports


## Funcionalidades Testadas

Login válido
Login inválido (usuário ou senha incorretos)
Captura de screenshots em falhas
Geração de relatórios Allure


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença
Este projeto está licenciado sob a licença MIT.