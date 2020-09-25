# Raio X do Test-Driven Development

Anotações do curso

## Exemplos de acidentes por falta de teste

- 1983 - sistema de monitoramento da URSS detectou erradamente 5 mísseis americanos
- Costa Concordia - instrumentos mediram errado o aprofundamento
- Therac-25 - excesso de radiação
- Mars Climate Orbiter - problema conversão de unidade
- IPO Facebook - muita gente, não se tinha a cotação
- Toyota Camry - controle de aceleração
- Airbus A400M - equipes com softwares de versão diferente

Standish Group Chaos Report 2010 - 2/3 dos projetos de software falham

## TAFT - Test All the Fucking Time

Origem do termo: Bryan Liles

Testes automáticos

Eurípedes: A grande coragem para mim é a prudência.

Não faça *Big Design Upfront*. Faça rascunhos antes de imaginar todo o projeto.

INPUT --> PROCESSAMENTO --> OUTPUT

Pro cliente só interessa o *output*. Mas passamos boa parte do tempo no input e no processamento, de forma que esquecemos de focar no que interessa, que é o output.

## Essência de um teste

Ver arquivo [essencia_test.py](essencia_test.py)

## Kata

Significa *forma*. Movimentos praticados no treino de artes marciais, realizados em conjunto ou individualmente.

**Erro** é diferente de **falha**.

Erro: qualquer exceção que não seja `AssertionError`. Tem prioridade sobre falhas.

Falha: `AssertionError`. Expectativa não está sendo cumprida.

