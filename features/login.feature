Feature: Login no sistema SauceDemo

  Scenario: Login com credenciais válidas
    Given que o usuário está na página de login
    When ele preenche o nome de usuário "standard_user" e a senha "secret_errada"
    Then ele deve ser redirecionado para a página de produtos

  Scenario: Tentativa de login com credenciais inválidas
    Given que o usuário está na página de login
    When ele preenche o nome de usuário "usuario_errado" e a senha "senha_errada"
    Then ele deve ver uma mensagem de erro

  Scenario: Tentativa de login com campo de usuário vazio
    Given que o usuário está na página de login
    When ele preenche o nome de usuário "" e a senha "secret_sauce"
    Then ele deve ver uma mensagem de erro 
  
  Scenario: Tentativa de login com campo de senha vazio
    Given que o usuário está na página de login
    When ele preenche o nome de usuário "standard_user" e a senha ""
    Then ele deve ver uma mensagem de erro 

  Scenario: Tentativa de login com usuário bloqueado
    Given que o usuário está na página de login
    When ele preenche o nome de usuário "locked_out_user" e a senha "secret_sauce"
    Then ele deve ver uma mensagem de erro 

  
 