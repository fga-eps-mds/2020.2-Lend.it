# Histórico de Revisão

| Data       | Versão | Descrição                                                                    | Autor(es)                        |
| :--------- | :----- | :--------------------------------------------------------------------------- | :------------------------------- |
| 09/02/2021 | 0.1    | Criação da estrutura do documento                                            | Thais Rebouças                   |
| 11/02/2021 | 0.2    | Criação dos subtópicos 1.1 e 1.6                                             | Matheus Afonso                   |
| 11/02/2021 | 0.2    | Criação dos subtópicos 3.1, 3.2 e 3.6                                        | Vinicius Saturnino               |
| 11/02/2021 | 0.2    | Criação dos subtópicos 3.4 e 3.7                                             | Matheus Monteiro                 |
| 11/02/2021 | 0.2    | Criação dos subtópicos 2.1 e 2.2                                             | Mateus Maia                      |
| 12/02/2021 | 0.3    | Revisão gramatical e estrutural de todo o documento                          | Thais Rebouças e Thiago Mesquita |
| 12/02/2021 | 0.3.1  | Criação do subtópico 1.4                                                     | Thais Rebouças                   |
| 12/02/2021 | 0.3.2  | Modificação dos subtópicos 1.1, 3.2, 3.6 e 3.7                               | Thais Rebouças                   |
| 12/02/2021 | 1.0    | Modificação dos subtópicos 2.1 e 2.2                                         | Thiago Mesquita                  |
| 17/02/2021 | 1.1    | Criação dos subtópicos 3.5.1 e 3.5.2                                         | Thais Rebouças                   |
| 17/02/2021 | 1.2    | Revisão gramatical e modificação do subtópico 2.2                            | Thiago Mesquita                  |
| 17/02/2021 | 1.3    | Criação do subtópico 4.4 e do tópico 5                                       | Thiago Mesquita e Thais Rebouças |
| 19/02/2021 | 1.4    | Modificação do tópico 2.1, adição de bullet points nos tópicos 3.4.2 e 3.4.3 | Thiago Mesquita                  |
| 19/02/2021 | 1.4    | Adição do tópico 1.2 e 4.1                                                   | Thais Rebouças                   |

# **1. Introdução**

### 1.1 Finalidade

Este documento tem como objetivo demonstrar as características do desenvolvimento da aplicação em questão. Além disso, visa auxiliar no contexto em que a ferramenta se aplica.

### 1.2 Escopo

Este projeto tem como finalidade a criação de um aplicativo mobile que possibilitará o encontro de pessoas que moram próximas e queiram compartilhar objetos de casa, diminuindo a distância entre vizinhos que podem se ajudar e suprirem suas necessidades de consumo em comunidade.
Na aplicação será possível aos usuários solicitarem um objeto para empréstimo, definindo a data de uso. E para os usuários que possuirem aquele objeto solicitado, será possivel atender ao pedido. Os pedidos mais próximos dos usuários serão exibidos no seu feed.
A aplicação possuirá um sistema de avaliação e denuncia para medir o nível de confiabilidade dos usuários.
Após a devolução do objeto, o proprietário poderá avaliar se ele foi entregue em boas condições e dentro do prazo estipulado.
No caso de um usuário não devolver o objeto dentro do prazo, o proprietário do mesmo poderá denunciar o perfil do usuário que pegou seu objeto. Cada denúncia e avaliação será contabilizada e exibida no perfil do usuário.
O aplicativo não possui fins lucrativos, e não se responsabiliza por quaisquer danos ou furtos dos objetos em questão.
A comunicação e encontro entre usuários deverá ser feita fora do aplicativo, portanto não nos responsabilizamos por quaisquer fatores decorrentes dessa comunicação.

### 1.4 Definições, Acrônimos e Abreviações

Estarão listadas neste tópico as definições, acrônimos e abreviações dos termos usados neste documento, para assim facilitar o compreendimento do público interessado no projeto.

| Sigla/Termo/Acrônimo | Definição                              |
| :------------------- | :------------------------------------- |
| MDS                  | Métodos de Desenvolvimento de Software |
| EPS                  | Engenharia de Produto de Software      |
| FGA                  | Faculdade do Gama                      |
| UNB                  | Universidade de Brasília               |

### 1.5 Referências

Documento de Visão: A estrutura de tópicos do documento de visão. IBM. Disponível em: https://goo.gl/BNAJtT. Acesso em: 11 de fevereiro de 2021;

### 1.6 Visão Geral

Através deste documento, é descrita de maneira detalhada e coesa as etapas de decisão, planejamento e desenvolvimento da aplicação, levando em questão os ambientes sociais, econômicos e o negócio aplicado no contexto da aplicação através dos problemas solucionados. Além disso, é apresentada a visão dos recursos, interfaces e configurações acima do ambiente da aplicação. Também são apresentados as restrições e impedimentos situacionais, além das etapas que contribuem para a qualidade e solidificação da aplicação em questões como desempenho, usabilidade e apresentação.

## **2. Posicionamento**

### 2.1 Oportunidade de negócios

Vivemos em uma sociedade em que recebemos muitos estímulos para consumo de produtos. O consumo em sí não é um problema, pois é necessário para a sobrevivência. O problema é o consumo exagerado, que leva à superprodução e a exploração excessiva dos recursos naturais, gerando vários problemas como a destruição de ecossistemas.
Segundo relatórios de respeitadas organizações ambientais, como a WWF e a WWI, consumimos mais do que a capacidade do planeta de se regenerar, alterando o equilíbrio da Terra. Reciclar é importante, porém não é o suficiente. Segundo relatório da Jefferies Financial, mesmo se os países tornarem a regulamentação muito mais rígida, ainda será difícil reciclar 50% dos resíduos plásticos do planeta em 10 anos. Desta forma, é necessário mudarmos a forma como consumimos e adotar modelos mais sustentáveis de consumo.
A aplicação em questão tem como objetivo introduzir uma cultura de reuso a partir do empréstimo de objetos usados, estimulando uma diminuição de consumo e ao mesmo tempo o uso de objetos até o fim do seu ciclo de vida.

### 2.2 Descrição do problema

| O problema é                                                                                  | que afeta       | cujo impacto é                                                                                                                         | uma boa solução seria                                                    |
| --------------------------------------------------------------------------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| O padrão de consumo insustentável e a massiva quantidade de resíduos provenientes dela mesmo. | O meio ambiente | Emissão de gases poluentes, contaminação do solo, degradação e devastação ambiental, e consequentemente, a destruição de ecossistemas. | Reduzir o consumo e utilizar os produtos até o fim do seu ciclo de vida. |

### 2.3 Sentença de Posição do Produto

| Para    | que                                                                                                                           | o produto       | que                                                | diferente de | nosso produto                                             |
| ------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------- | -------------------------------------------------- | ------------ | --------------------------------------------------------- |
| Pessoas | Desejam ajudar seus vizinhos com empréstimo de objetos, ou que necessitam de algum objeto ao invés de comprar um produto novo | Qualquer objeto | Será emprestado para outra pessoa que precisa usar | Reciclagem   | Busca utilizar os produtos até o fim do seu ciclo de vida |

## **3. Descrição dos Envolvidos e dos Usuários**

### 3.1 Resumo dos Envolvidos

| Nome                          | Descrição                                                            | Responsabilidade                                                                                                                        |
| :---------------------------- | :------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| Equipe de Desenvolvimento     | Estudantes do curso de Engenharia de Software das disciplinas de MDS | Contribuir ativamente com o desenvolvimento e implementação do software citado neste documento                                          |
| Equipe de Gestão do Projeto   | Estudantes do curso de Engenharia de Software das disciplinas de EPS | Gerenciar tempo, escopo, riscos, tomadas de decisões para garantir a viabilidade do projeto e garantir a aplicação dos princípios ágeis |
| Equipe de avaliação e suporte | Professor e Coaches das disciplinas de EPS e MDS                     | Auxiliar a equipe ao longo do desenvolvimento do projeto                                                                                |

### 3.2 Resumo dos Usuários

| Nome            | Descrição                                                               | Responsabilidade                                                                             |
| :-------------- | :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| Pessoas físicas | Pessoas que necessitam de bens materiais para execução de alguma tarefa | Utilizar e manter o sistema, alimentando a base de dados, e usufruir de suas funcionalidades |

### 3.3 Ambiente do Usuário

Os usuários poderão utilizar a aplicação por meio de dispositivos mobile.

### 3.4 Perfis dos Envolvidos

#### 3.4.1 Equipe avaliação e suporte

| Representantes    | Descrição                                                     | Tipo                                     | Responsabilidades                                                                                                                                                                               | Critério de sucesso                                                                                                             | Envolvimento |
| ----------------- | ------------------------------------------------------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Prof. Hilmer Neri | Equipe responsável pela avaliação e direcionamento do projeto | Professor e coach do grupo da disciplina | Direcionar e dar suporte a equipe de desenvolvimento e gestão, nas disciplinas Métodos de Desenvolvimento de Software e Engenharia de Produto de Software, quanto ao desenvolvimento do projeto | A entrega do projeto juntamente com uma documentação coerente estabelecida, a partir das orientações dadas ao longo do semestre | Alto         |

#### 3.4.2 Equipe de Desenvolvimento

| Representantes                                                                                                                                                                                                                   | Descrição                                            | Tipo                              | Responsabilidades                  | Critério de sucesso                                                                                  | Envolvimento |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | --------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------ |
| <ul><li>Mateus Cunha Maia Matheus Afonso de Souza</li><li>Matheus Yan Monteiro dos Santos Almeida</li><li>Vinicius de Sousa Saturnino</li><li>Thais Rebouças de Araujo</li><li>Thiago Mesquita Peres Nunes de Carvalho</li></ul> | Equipe responsável pelo desenvolvimento da aplicação | Estudantes de MDS da FGA UnB/Gama | Desenvolver a aplicação em questão | Entregar o software com as funcionalidades desejadas pelo público alvo dentro do prazo da disciplina | Alto         |

#### 3.4.3 Equipe de Gestão do Projeto

| Representantes                                                                                                                                                           | Descrição                                         | Tipo                              | Responsabilidades                                                                                                                                         | Critérios de Sucesso                                                                                                 | Envolvimento |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------ |
| <ul><li>Esio Gustavo Pereira Freitas</li><li>Lucas Dutra Ferreira do Nascimento</li><li>Youssef Muhamad Yacoub Falaneh</li><li>Rogério Silva dos Santos Júnior</li></ul> | Equipe responsável pelo gerenciamento do software | Estudantes de EPS da FGA UnB/Gama | Gerenciamento do tempo, escopo, riscos e tomadas de decisão para que a viabilidade do projeto seja instituída e garantir a aplicação dos princípios ágeis | Manter a motivação e produção da equipe alta e constante, para o software ser entregue com qualidade dentro do prazo | Alto         |

### 3.5 Perfis dos Usuários

#### 3.5.1 Proprietário de objetos

| Representantes   | Descrição                                          | Tipo                                         | Responsabilidades                                                               | Critérios de Sucesso                                                           | Envolvimento |
| ---------------- | -------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------ |
| Donos de objetos | Qualquer pessoa disposta a ajudar nas proximidades | Usuário com baixo/médio conhecimento técnico | Entrar em contato com o usuário que fez uma solicitação a qual ele pode atender | O proprietário deve conseguir entrar em contato com quem precisa do seu objeto | Alto         |

#### 3.5.2 Solicitante de objetos

| Representantes                                | Descrição                                               | Tipo                                         | Responsabilidades                      | Critérios de Sucesso                                                                                                                | Envolvimento |
| --------------------------------------------- | ------------------------------------------------------- | -------------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Usuário que realizará solicitações de objetos | Qualquer usuário que precise de algum objeto emprestado | Usuário com baixo/médio conhecimento técnico | Realizar uma solicitação na plataforma | O usuário deverá conseguir cadastrar uma solicitação no aplicativo que indicará o tipo de objeto que ela precisa e por qual período | Alto         |

#### 3.6 Principais Necessidades dos Usuários ou dos Envolvidos

| Necessidade                                                      | Prioridade | Preocupações                      | Solução Atual     | Soluções propostas  |
| :--------------------------------------------------------------- | :--------- | :-------------------------------- | :---------------- | :------------------ |
| Ter acesso a determinados objetos para realizar alguma atividade | Alta       | Evitar superprodução de materiais | Comprar o produto | Emprestar o produto |

#### 3.7 Alternativas e concorrências

#### 3.7.1 Tem açúcar?

O "Tem Açúcar?" é uma rede social de vizinhos que facilita a comunicação, colaboração e troca de gentilezas nas vizinhanças.

#### 3.7.2 Gimme back

Gimme back é um aplicativo que ajuda a ter mais controle sobre as coisas que empresta e até mesmo lembrar aquele amigo de devolver algo que você emprestou.

#### 3.7.3 IOU (O owe you)

IOU é um aplicativo que permite que você anote tudo o que emprestou a seus amigos, assim como o que tomou emprestado, desde dinheiro até itens, como livros, CDs, DVDs, etc. Este aplicativo oferece uma forma prática de você manter o controle de tudo o que emprestou e que pegou emprestado com os seus amigos e familiares.

## **4. Visão geral do Produto**

### 4.1 Perspectiva do Produto

Nossa aplicação se difere das demais do mercado por ser um facilitador de interações entre vizinhos, promovendo as ações de emprestar e pegar emprestado, além de possuir um sistema de avaliação e denúncia para tornar um perfil mais confiável ou não, gerando uma maior segurança na hora de usar a aplicação, para atrair até o público mais desconfiado.

### 4.2 Resumo dos Recursos

|                         Benefício para o Usuário                         |                                                       Recursos de suporte                                                       |
| :----------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------: |
|                  Sistema de avaliação entre os usuários                  |  O software une as informações dadas pelos usuários e calcula a nota de cada usuário, demonstrando a confiabilidade do perfil   |
| Facilidade em visualizar pedidos de empréstimos de objetos perto de casa |                                         Feed com as solicitações pŕoximas mais recentes                                         |
|                 Facilidade em fazer pedido de empréstimo                 | O usuário que tiver necessidade de pedir algo emprestado poderá o fazer com facilidade através de uma publicação de solicitação |

## **5. Recursos do Produto**

### 5.1 Cadastro

O usuário poderá criar um cadastro no aplicativo, para ter acesso ao sistema.

### 5.2 Acesso

O usuário poderá ter acesso ao sistema, através de uma autenticação por login.

### 5.3 Gerenciamento de empréstimos

O usuário poderá solicitar e/ou fornecer um empréstimo aos seus vizinhos.

### 5.4 Avaliação de usuário

O usuário poderá avaliar o outro após um empréstimo.

### 5.5 Sistema de denúncias

O usuário poderá denunciar o perfil de usuários que não devolveram o objeto emprestado dentro do prazo estipulado.

### 5.6 Sistema de geolocalização

Através da geolocalização, a aplicação vai exibir as solicitações de usuários mais próximos.
