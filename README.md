# 🧪 Projeto de Teste Automatizado - SauceDemo

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Behave](https://img.shields.io/badge/BDD-Behave-brightgreen)
![Selenium](https://img.shields.io/badge/Selenium-Automation-yellowgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

## ✨ Descrição

Este projeto automatiza cenários de teste na aplicação [SauceDemo](https://www.saucedemo.com/) utilizando **Selenium WebDriver** com **Behave (BDD)**.

Os testes cobrem autenticação (login válido e inválido), com geração de relatórios e captura de falhas via screenshot.

---

## 📂 Estrutura do Projeto

```
📁 features/          → arquivos .feature com os cenários de teste
📁 steps/             → implementação dos passos em Python
📁 screenshots/       → prints automáticos de falhas nos testes
📁 reports/           → relatórios gerados com Allure
📄 environment.py     → configurações de ambiente do Behave
📄 requirements.txt   → dependências do projeto
📄 README.md          → este arquivo ✨
```

---

## 🚀 Como Executar os Testes

## bash
# 1. Clone o repositório
git clone https://github.com/Maia-laura/Meu_Teste_Automtizado.git
cd Meu_Teste_Automtizado

# 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # macOS/Linux

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute os testes
behave

# 5. Gere o relatório com Allure (opcional)
allure serve ./reports
```

---

## ✅ Funcionalidades Testadas

- 🔐 Login válido
- ❌ Login inválido
- 📸 Captura automática de prints em falhas
- 📊 Geração de relatório com Allure

---

## 📸 Demonstração

> *Aqui você pode colocar um print ou um GIF do navegador executando o teste.*

---

## 🤝 Contribuindo

Contribuições são sempre bem-vindas!  
Abra uma issue ou envie um pull request com melhorias, correções ou sugestões.

---

## 📝 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

### 💖 Feito com carinho por [@Maia-laura](https://github.com/Maia-laura)