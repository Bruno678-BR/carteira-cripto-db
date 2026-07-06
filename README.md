# Sistema de Captura e Armazenamento de Criptoativos 🚀

Aplicação orientada a objetos desenvolvida em **Python** integrada ao banco de dados relacional **MySQL**, focada no setor financeiro para registro, captura e armazenamento de dados e cotações de criptomoedas de forma estruturada.

## 🛡️ Diferenciais de Engenharia e Segurança
* **Arquitetura em Camadas (Pattern Repository):** Separação clara de responsabilidades entre a gestão da conexão (`database.py`) e os comandos de persistência SQL (`repository.py`).
* **Segurança da Informação (.env):** Utilização da biblioteca `python-dotenv` para encapsular e proteger as credenciais de acesso locais através de variáveis de ambiente, prevenindo vazamento de dados em commits públicos.
* **Integridade dos Dados:** Modelagem relacional inteligente utilizando uma Chave Primária Composta (`PRIMARY KEY (codigo, data_cripto)`), evitando com sucesso a entrada de registros duplicados na base.

## 🛠️ Tecnologias Utilizadas
* **Python** (Lógica de programação e POO)
* **MySQL** (Persistência e banco de dados relacional)
* **Git & GitHub** (Controle de versão e documentação)

## 📁 Estrutura do Projeto
* `main.py`: Orquestrador que executa e inicia o fluxo de teste do sistema.
* `database.py`: Gerencia e isola o ciclo de vida da conexão segura com o MySQL.
* `repository.py`: Camada abstrata responsável por executar queries (`INSERT INTO`) de forma limpa.
* `.gitignore`: Bloqueia o envio de arquivos confidenciais (`.env`) para a nuvem.

## 🔧 Como Executar Localmente
1. Clone este repositório.
2. Instale as dependências: `pip install mysql-connector-python python-dotenv`.
3. Crie um arquivo `.env` na raiz do projeto com as suas credenciais locais (`DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`).
4. Execute o script principal: `python main.py`.
