# Boas-vindas ao do projeto Restaurant Orders!

Projeto feito durante o curso de desenvolvimento web na trybe.

A lanchonete ficticia Pão na Chapa possui um sistema de faturamento de pedidos de clientes que salva o nome da pessoa, o pedido realizado e o dia da semana do atendimento.</br>

A gerência da lanchonete quer aumentar suas vendas e melhorar sua gestão interna e, para isso, te contratou para implementar um projeto de melhorias. </br>

Em um primeiro momento, você deverá atuar para que o sistema gere relatórios com informações sobre os pedidos e as pessoas clientes que frequentam a lanchonete.</br>

Em um segundo momento, o foco do projeto deverá ser o controle do estoque de ingredientes para garantir que o cardápio digital da Pão na Chapa sempre ofereça produtos que estão disponíveis no estoque, evitando frustrações por parte das pessoas clientes. </br>

## Habilidades exercitadas:
  - Trabalhar com `Hashmap` e `Dict` e; </br>
  - Trabalhar com `Set`. </br>


# Desenvolvimento
<details>
  <summary>
    <h3>
      Antes de começar a desenvolver</summary><br />
    </h3>

  1. Clone o repositório

  - Use o comando: `git@github.com:mabiiak/restaurant-orders.git`.
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd restaurant-orders`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
  4. Crie uma branch a partir da branch `master`

  - Verifique que você está na branch `master`
    - Exemplo: `git branch`
  - Se não estiver, mude para a branch `master`
    - Exemplo: `git checkout master`
  - Crie uma branch à qual você vai submeter os `commits` do seu projeto
    - Você deve criar uma branch no seguinte formato: `nomedeusuario-nome-do-projeto`
    - Exemplo: `git checkout -b nome-restaurant-orders`

  5. Adicione a sua branch com o novo `commit` ao repositório remoto

  - Usando o exemplo anterior: `git push -u origin nome-restaurant-orders`

  7. Crie um novo `Pull Request` _(PR)_

  - Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/mabiiak/restaurant-orders/pulls)
  - Clique no botão verde _"New pull request"_
  - Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
  - Coloque um título para a sua _Pull Request_
    - Exemplo: _"Cria tela de busca"_
  - Clique no botão verde _"Create pull request"_
  - Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
  - **Não se preocupe em preencher mais nada por enquanto!**
  - Volte até a [página de _Pull Requests_ do repositório](https://github.com/mabiiak/restaurant-orders/pulls) e confira que o seu _Pull Request_ está criado

</details>

<details>
  <summary><h3>Ambiente Virtual</h3></summary><br />
  O Python oferece um recurso chamado de ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  :eyes: Caso precise desativar o ambiente virtual, execute o comando "deactivate". 
  :warning: Lembre-se de ativar novamente o ambiente virtual quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

## Requisitos
    ✅ 1.1 - Será validado se, ao executar o método analyze_log, os dados são preenchidos de forma correta no arquivo data/mkt_campaign.txt

    ✅ 1.2 - Será validado se, ao executar o método analyze_log com um arquivo inexistente, o método retorna um erro

    ✅ 1.3 - Será validado se, ao executar o método analyze_log com uma extensão inválida, o método retorna um erro

    ✅ 2.1 - Será validado se, ao instanciar a classe TrackOrders pela primeira vez, o método retorna a quantidade de pedidos é igual a zero

    ✅ 2.2 - Será validado se, ao executar o método add_new_order, o método deve adicionar um pedido

    ✅ 2.3 - Será validado se, ao executar get_most_ordered_dish_per_costumer, o método retorna o prato mais pedido

    ✅ 2.4 - Será validado se, ao executar get_never_ordered_per_costumer, o método retorna o pedido que o cliente nunca fez

    ✅ 2.5 - Será validado se, ao executar get_days_never_visited_per_costumer, o método retorna o dias que o cliente nunca visitou

    ❌ 2.6 - Será validado se, ao executar o método get_busiest_day, o método retorna o dia mais movimentado	

    ❌ 2.7 - Será validado se, ao executar o método get_least_busy_day, o método retorna o dia menos movimentado

    ❌ 3.1 - Será validado se, ao executar o método get_quantities_to_buy, o método retorna a lista atualizada de ingredientes
    
    ❌ 3.2 - Será validado se, ao executar o método get_quantities_to_buy o método retorna toda a quantidade de ingredientes há se comprar de hamburguer	
    
    ❌ 3.3 - Será validado se, ao executar o método get_quantities_to_buy, o método retorna a lista atualizada dos ingredientes que usam receitas diferentes	
    
    ❌ 4.1 - Será validado se, ao adicionar uma quantidade maior de ingredientes, o método retorna false	
    
    ❌ 4.2 - Será validado se, ao executar o método get_available_dishes, o método retorna todos os pratos onde os pratos tem ingredientes	
    
    ❌ 4.3 - Será validado se, ao executar o método get_available_dishes, não o método retorna os pratos o qual os ingredientes não sejam suficientes para prepará-los
