# Guia de Estilo e Identidade Visual

# Histórico de Revisão

| Data   | Versão | Modificação  | Autor  |
| :- | :- | :- | :- |
| 03/03/2021 | 1.0 | Criação da versão inicial do documento | Thais Rebouças |
| 04/03/2021 | 1.1 | Adição do tópico 1 e 4, e do subtópico 3.1 e 3.3 | Thais Rebouças |


# 1 Introdução
O seguinte documento objetiva informar e detalhar tecnicamente a construção do conjunto de elementos que representam visualmente a aplicação.

# 2 Apresentação da Identidade Visual


# 3 Detalhamento e Justificativas

## 3.1 Nome da aplicação
A escolha do nome da aplicação foi feita pensando em um nome curto e prático para a escrita e fala: **Lend.it** do inglês, que significa "empreste-o". Uma referencia ao principal objetivo da aplicação.

## 3.2 Fontes

As fontes utilizadas na aplicação serão:

 - **Poppins**(Open Font License), para títulos e 
 - **Open Sans**(Apache License, Version 2.0), para textos. 

Elas foram escolhidas por serem fontes que passam uma ideia amistosa e que possuem licenças que permitem uso gratuito.

### Uso das fontes

#### Incluindo no HTML

Coloca-se no <head> o seguinte trecho de código:

    <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">

	<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
    

#### Incluindo no CSS

Coloca-se no css, para a utilização das fontes:

	font-family: 'Poppins', sans-serif;
	font-family: 'Open Sans', sans-serif;


# 3.3 Paleta de cores

As cores foram selecionadas observando características do produto e sua finalidade, baseado na psicologia das cores.
Como a aplicação é baseada fortemente na confiança entre os usuários, por se tratar de empréstimos de objetos pessoais aos vizinhos, a cor primária que melhor se adequa para essa aplicação é o laranja.

![psicologia das cores](../../assets/img/identidade_visual/psicologia_cores.png)

O laranja sendo uma cor derivada do vermelho, tem características muito alegres e estimulantes, acabando por despertar o desejo de ação do usuário. Em relação ao vermelho, o laranja acaba tendo a vantagem de ser mais agradável aos olhos, menos agressivo.

Quando aplicado no mundo do marketing, ele pode significar criatividade, alegria e confiança.

A cor secundária escolhida é a cor complementar à primária no círculo cromático, o azul. Que tem como característica a capacidade de levar segurança e tranquilidade para as pessoas.

![paleta de cores](../../assets/img/identidade_visual/complementar.png)

* Depois de adicionar o preto e o branco o resultado foi:

![paleta de cores](../../assets/img/identidade_visual/primeira.png)

* Removendo o contraste:

![paleta de cores](../../assets/img/identidade_visual/segunda.png)

* Escurecendo um pouco mais as cores, o resultado final foi:

![paleta de cores](../../assets/img/identidade_visual/paleta_cores.png)

Primária: #FF931F,
Secundária: #005A7A.

# 4 Protótipo de Alta Fidelidade

O protótipo foi desenvolvido utilizando a ferramenta [Figma]() e pode ser conferido na íntegra [aqui]() 


