# Detecção de Fraudes Bancárias com Análise de Anomalias

# Introdução

Este documento serve como um guia completo e prático para o desenvolvimento de um sistema de detecção de fraudes bancárias utilizando técnicas de **Aprendizado de Máquina Não Supervisionado**, especificamente a **Detecção de Anomalias**.

Diferente de abordagens tradicionais onde o modelo aprende com exemplos rotulados de "fraude" e "não fraude", nossa missão aqui é ensinar um algoritmo a entender o que constitui um **comportamento transacional "normal"**. Qualquer transação que desvie significativamente desse padrão de normalidade será classificada como uma anomalia e, consequentemente, uma forte candidata a fraude a ser investigada.

## Fase 0: Fundamentos e Estratégia Analítica

Antes de escrever uma única linha de código, precisamos solidificar nossa estratégia.

### 0.1. Por que Detecção de Anomalias?

No cenário real, muitas vezes não temos um conjunto de dados perfeitamente rotulado. A detecção de anomalias é a abordagem correta quando:

- **Rótulos são inexistentes ou não confiáveis:** Não temos uma coluna `IsFraud`.
- **Fraudes são raras e evoluem:** Novos tipos de fraude surgem constantemente. Um modelo treinado para reconhecer fraudes antigas pode não detectar as novas.
- **O objetivo é encontrar o "estranho":** Queremos que o sistema nos alerte sobre qualquer coisa que fuja ao padrão, em vez de apenas procurar por padrões já conhecidos.

### 0.2. O Algoritmo Principal: Isolation Forest (Floresta de Isolamento)

Para este projeto, nosso principal algoritmo será o **Isolation Forest**.

- **Conceito Intuitivo:** Imagine que cada transação é uma pessoa em uma sala lotada. As "pessoas normais" estão no meio da multidão, e é preciso muito esforço (muitas divisões/paredes) para isolá-las. As "pessoas anômalas" estão sozinhas nos cantos da sala; com pouquíssimas paredes, conseguimos isolá-las do resto.
- **Como Funciona:** O algoritmo constrói várias árvores de decisão aleatórias. A pontuação de anomalia de uma transação é baseada no número médio de divisões necessárias para isolá-la. Transações que são isoladas rapidamente (com poucas divisões) recebem uma pontuação de anomalia alta.
- **Por que ele?** É computacionalmente eficiente, performa muito bem em datasets grandes e é um padrão da indústria para detecção de anomalias em dados tabulares.

### 0.3. Métricas de Sucesso (Qualitativas)

Como não temos "respostas certas" para comparar, a avaliação do nosso modelo será qualitativa. Nosso sucesso será medido pela nossa capacidade de responder "sim" a estas perguntas:

1. **Plausibilidade:** O perfil das anomalias detectadas faz sentido como fraude? (Ex: valores muito altos, muitas tentativas de login, horários de madrugada).
2. **Acionabilidade:** As anomalias encontradas são claras o suficiente para que um analista humano possa iniciar uma investigação?
3. **Interpretabilidade:** Conseguimos explicar por que uma transação específica foi considerada uma anomalia, analisando suas características?

## Fase 1: Configuração do Ambiente e Análise Exploratória (EDA)

O objetivo desta fase foi carregar os dados, fazer uma limpeza inicial e entender o perfil do comportamento "normal" através de visualizações.

### Resumo das Descobertas da Fase 1

Com base na sua análise dos gráficos, definimos o perfil de uma transação "normal":

- **Valor da Transação:** A grande maioria das transações é de baixo valor, concentrando-se na faixa de **R$ 0 a R$ 250**.
- **Faixa Etária:** A base de clientes é **bimodal**, com dois grupos principais: jovens entre **18 e 30 anos** e clientes mais maduros entre **50 e 60 anos**.
- **Canal Mais Utilizado:** Os canais são bem distribuídos, com **Branch (Agência)** sendo ligeiramente o mais comum, seguido de perto por ATM e Online.
- **Dados Ausentes:** O dataset está completo e **não possui valores ausentes**, o que simplifica a etapa de limpeza.

## Fase 2: Engenharia de Features e Pré-processamento

Nesta fase, transformamos nosso conhecimento de negócio em informação útil para o modelo, criando novas variáveis que capturam o **contexto** de uma transação e preparando os dados para o algoritmo. O resultado final desta fase foi o array `X_processed`, pronto para o treinamento.

## Fase 3: Treinamento do Modelo e Análise das Anomalias

Nesta fase, treinamos o modelo Isolation Forest com uma `contamination` de 2% e adicionamos as previsões ao nosso dataframe. A análise comparativa revelou o perfil das transações anômalas.

## Fase 4: Conclusão e Perfil da Anomalia

Com base na análise quantitativa da Fase 3, podemos agora construir um perfil claro e acionável do que o nosso modelo considera uma transação anômala, nossa melhor aproximação de uma fraude.

### 4.1. O Perfil da Anomalia: Decifrando os Sinais

As anomalias detectadas pelo modelo Isolation Forest apresentam um perfil distinto e plausível de atividade fraudulenta. As características, ordenadas pela sua capacidade de discriminação, são:

1. **Comportamento Financeiro Agressivo (`AmountToBalanceRatio`):** Esta foi a feature mais impactante. As anomalias, em média, envolvem transações que consomem uma proporção drasticamente maior do saldo disponível na conta. Isso sugere um comportamento de "esvaziar a conta", típico de fraudadores que obtêm acesso a fundos.
2. **Dificuldade de Acesso (`LoginAttempts`):** O número de tentativas de login é significativamente maior nas transações anômalas. Este é um forte indicativo de atividade suspeita, como tentativas de força bruta, uso de credenciais roubadas ou dificuldade do fraudador em acessar a conta.
3. **Valores de Transação Elevados (`TransactionAmount`):** Como esperado, o valor monetário das transações anômalas é consideravelmente maior do que o das transações normais, fugindo do padrão de "gastos baixos" que observamos na Fase 1.
4. **Uso de Canais Digitais (`Channel_Online` e `Channel_Branch`):** As anomalias são mais propensas a ocorrer nos canais **Online** e em **Agências (Branch)** em comparação com o comportamento normal. Isso pode indicar a exploração de vulnerabilidades específicas desses canais.
5. **Horários e Duração (`TransactionHour` e `TransactionDuration`):** As transações anômalas tendem a ocorrer em horários diferentes dos normais e a ter uma duração ligeiramente maior, o que pode refletir a complexidade ou a falta de familiaridade do fraudador com o sistema.

### 4.2. Conclusão do Projeto

Este projeto demonstrou com sucesso a eficácia da abordagem de **Detecção de Anomalias** para identificar fraudes em um cenário onde não há dados rotulados. Através de uma cuidadosa **análise exploratória** e, crucialmente, de uma **engenharia de features** focada em comportamento, fomos capazes de treinar um modelo **Isolation Forest** que identificou um conjunto de transações com características altamente suspeitas e consistentes com padrões de fraude conhecidos.

O perfil da anomalia que construímos não é apenas um resultado estatístico; é um insight de negócio valioso.

### 4.3. Implicações de Negócio e Próximos Passos

Um modelo como este pode ser implementado em um ambiente de produção para:

- **Gerar Alertas em Tempo Real:** As transações marcadas como anômalas podem ser enviadas para uma equipe de analistas de fraude para investigação imediata, antes que a transação seja liquidada.
- **Criar um "Score de Risco":** Em vez de uma classificação binária, a pontuação de anomalia do Isolation Forest pode ser usada como um score contínuo de risco para cada transação.
- **Bloqueio Preventivo:** Transações que ultrapassam um certo limiar de anomalia podem ser automaticamente bloqueadas e exigir uma verificação adicional do cliente (ex: autenticação de dois fatores).