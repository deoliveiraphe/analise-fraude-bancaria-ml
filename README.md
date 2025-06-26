# 🔍 Detecção de Fraudes Bancárias com Machine Learning

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Sistema avançado de detecção de fraudes bancárias utilizando técnicas de Machine Learning não supervisionado para identificar transações anômalas em tempo real.**

## 🎯 Visão Geral

Este projeto implementa um **sistema completo de detecção de fraudes bancárias** utilizando o algoritmo **Isolation Forest** para análise de anomalias. Diferente de abordagens tradicionais supervisionadas, este sistema aprende o comportamento "normal" das transações e identifica qualquer desvio significativo como potencial fraude.

### 🌟 Principais Características

- **🤖 Aprendizado Não Supervisionado**: Não requer dados rotulados de fraude
- **📊 Score de Risco Contínuo**: Sistema de pontuação de 0-100 para cada transação
- **⚡ Detecção em Tempo Real**: Capacidade de análise instantânea de transações
- **📈 Análise Interpretável**: Identificação das características que tornam uma transação suspeita
- **🎨 Visualizações Ricas**: Dashboards e gráficos para análise exploratória

## 🏗️ Arquitetura do Projeto

```
📦 analise-fraude-bancaria-ml/
├── 📊 data/
│   ├── bank_transactions_data.csv         # Dataset original (10.000 transações)
│   └── 🔧 processed/                      # Dados processados
│       ├── X_processed.npy               # Features normalizadas
│       ├── scaler.pkl                    # StandardScaler treinado
│       ├── feature_names.pkl             # Nomes das features
│       └── preprocessing_summary.pkl      # Resumo do pré-processamento
│
├── 🤖 models/
│   ├── isolation_forest_model.pkl        # Modelo principal treinado
│   └── model_summary.pkl                 # Métricas e parâmetros do modelo
│
├── 📈 results/
│   ├── predictions.npy                   # Predições do modelo
│   ├── risk_analysis_summary.csv         # Resumo da análise de risco
│   ├── 🖼️ plots/                         # Visualizações geradas
│   │   ├── distribuicao_valor_transacoes.png
│   │   ├── distribuicao_idade_clientes.png
│   │   ├── contagem_transacoes_canal.png
│   │   └── score_risco_visualizacoes.png
│   └── 🎯 scores/
│       ├── risk_scores_detailed.csv      # Scores detalhados por transação
│       └── technical_analysis_summary.pkl
│
├── 📓 notebooks/
│   ├── fase1_analise_exploratoria.ipynb  # EDA e visualizações
│   ├── fase2_pre_processamento.ipynb     # Feature engineering
│   ├── fase3_isolation_forest.ipynb      # Treinamento do modelo
│   └── fase4_score_de_risco.ipynb        # Sistema de scoring
│
├── 📚 docs/
│   └── Detecção de Fraudes Bancárias.md  # Documentação técnica completa
│
├── 🔧 src/
│   ├── __init__.py
│   └── utils.py                          # Funções auxiliares
│
└── 📋 config/
    └── config.py                         # Configurações do projeto
```

## 🚀 Resultados Principais

### 📊 Performance do Modelo

- **Taxa de Detecção**: 2% das transações identificadas como anômalas
- **Precisão Qualitativa**: Alto grau de plausibilidade nas anomalias detectadas
- **Score de Risco**: Sistema de pontuação contínua 0-100 implementado
- **Interpretabilidade**: Identificação clara dos fatores de risco

### 🎯 Perfil das Anomalias Detectadas

O modelo identificou transações anômalas com as seguintes características:

1. **💰 Comportamento Financeiro Agressivo**: 
   - Transações que consomem proporção elevada do saldo disponível
   - Valores significativamente acima da média histórica

2. **🔐 Padrões de Acesso Suspeitos**:
   - Múltiplas tentativas de login
   - Acesso em horários atípicos

3. **🌐 Preferência por Canais Digitais**:
   - Maior incidência em canais Online e Agência
   - Duração de transação atípica

### 📈 Distribuição de Risco

| Categoria de Risco | Quantidade | Percentual | Ação Recomendada |
|-------------------|------------|------------|-------------------|
| **Muito Baixo (0-25)** | ~7.500 | 75% | ✅ Aprovação automática |
| **Baixo (25-50)** | ~1.500 | 15% | ✅ Aprovação com monitoramento |
| **Médio (50-75)** | ~750 | 7.5% | 👀 Monitoramento ativo |
| **Alto (75-90)** | ~200 | 2% | ⚠️ Revisão manual |
| **Muito Alto (90-100)** | ~50 | 0.5% | 🚨 Bloqueio imediato |

## 🛠️ Tecnologias Utilizadas

### Core ML & Data Science
- **Python 3.8+**: Linguagem principal
- **Scikit-learn**: Algoritmo Isolation Forest e pré-processamento
- **Pandas & NumPy**: Manipulação e análise de dados
- **Joblib & Pickle**: Serialização de modelos

### Visualização & Análise
- **Matplotlib & Seaborn**: Visualizações estáticas
- **Plotly**: Gráficos interativos
- **Jupyter Notebook**: Ambiente de desenvolvimento

### Desenvolvimento & Deploy
- **Git**: Controle de versão
- **Poetry/Pip**: Gerenciamento de dependências

## ⚡ Quick Start

### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/analise-fraude-bancaria-ml.git
cd analise-fraude-bancaria-ml
```

### 2. Configure o Ambiente
```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

### 3. Execute os Notebooks
```bash
jupyter notebook
```

**Ordem de execução recomendada:**
1. `notebooks/fase1_analise_exploratoria.ipynb` - Análise exploratória dos dados
2. `notebooks/fase2_pre_processamento.ipynb` - Feature engineering e normalização
3. `notebooks/fase3_isolation_forest.ipynb` - Treinamento do modelo
4. `notebooks/fase4_score_de_risco.ipynb` - Sistema de scoring de risco

### 4. Utilize o Modelo Treinado

```python
import joblib
import pandas as pd
import numpy as np

# Carregar modelo e scaler
modelo = joblib.load('models/isolation_forest_model.pkl')
scaler = joblib.load('data/processed/scaler.pkl')

# Preparar nova transação
nova_transacao = pd.DataFrame({
    'TransactionAmount': [5000],
    'CustomerAge': [25],
    'AccountBalance': [10000],
    # ... outras features
})

# Normalizar e predizer
X_novo = scaler.transform(nova_transacao)
score_anomalia = modelo.decision_function(X_novo)[0]
risk_score = calcular_score_risco(score_anomalia)

print(f"Score de Risco: {risk_score:.2f}/100")
```

## 📋 Metodologia Detalhada

### Fase 1: Análise Exploratória de Dados (EDA)
- **Objetivo**: Compreender o perfil do comportamento "normal"
- **Descobertas**: 
  - Transações concentradas em valores baixos (R$ 0-250)
  - Base de clientes bimodal (18-30 e 50-60 anos)
  - Distribuição equilibrada entre canais de atendimento

### Fase 2: Feature Engineering
- **Transformações**:
  - Encoding de variáveis categóricas
  - Normalização com StandardScaler
  - Criação de features derivadas (ratios, flags temporais)
- **Resultado**: 15+ features otimizadas para detecção de anomalias

### Fase 3: Treinamento do Modelo
- **Algoritmo**: Isolation Forest
- **Parâmetros**: 
  - `contamination=0.02` (2% de anomalias esperadas)
  - `n_estimators=100`
  - `random_state=42`
- **Validação**: Análise qualitativa das anomalias detectadas

### Fase 4: Sistema de Scoring
- **Score de Risco**: Conversão para escala 0-100
- **Categorização**: 5 faixas de risco com ações específicas
- **Interpretabilidade**: Identificação de features mais discriminativas

## 📊 Visualizações Disponíveis

O projeto gera automaticamente várias visualizações para análise:

### 📈 Análise Exploratória
- Distribuição de valores de transação
- Demografia dos clientes
- Padrões de uso por canal
- Análise temporal das transações

### 🎯 Análise de Anomalias
- Distribuição dos scores de risco
- Comparação: transações normais vs anômalas
- Scatter plots de features discriminativas
- Dashboard de categorização de risco

## 🎯 Casos de Uso em Produção

### 1. Sistema de Alertas em Tempo Real
```python
def avaliar_transacao(risk_score):
    if risk_score >= 90:
        return "🚨 BLOQUEAR IMEDIATAMENTE"
    elif risk_score >= 75:
        return "⚠️ REVISAR MANUALMENTE"
    elif risk_score >= 50:
        return "👀 MONITORAR"
    else:
        return "✅ APROVAR"
```

### 2. Impacto Operacional
- **Revisão Manual**: ~2% das transações (alto valor, sustentável)
- **Bloqueio Automático**: ~0.5% das transações (casos extremos)
- **Redução de Falsos Positivos**: Foco em anomalias realmente significativas

## 🔍 Features Mais Discriminativas

1. **AmountToBalanceRatio**: Proporção valor/saldo (mais importante)
2. **LoginAttempts**: Número de tentativas de acesso
3. **TransactionAmount**: Valor da transação
4. **Channel_Online**: Uso do canal online
5. **TransactionHour**: Horário da transação

## 📈 Métricas de Sucesso

### Avaliação Qualitativa
✅ **Plausibilidade**: Anomalias detectadas fazem sentido como fraude  
✅ **Acionabilidade**: Resultados claros para investigação  
✅ **Interpretabilidade**: Explicação clara dos fatores de risco  

### Performance Operacional
- **Eficiência Computacional**: Modelo rápido e escalável
- **Baixo Overhead**: Apenas 2% das transações para revisão
- **Alta Confiabilidade**: Detecção consistente de padrões suspeitos

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**Paulo Henrique Oliveira**
- GitHub: [@pholiveira3](https://github.com/pholiveira3)
- LinkedIn: [Paulo Henrique Oliveira](https://linkedin.com/in/paulo-henrique-oliveira)
- Email: seu.email@exemplo.com

## 🙏 Agradecimentos

- Comunidade Scikit-learn pela excelente documentação
- Jupyter Project pelo ambiente de desenvolvimento
- Comunidade Python de Data Science

---

**⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!**

---

### 📝 Últimas Atualizações

- **v1.0.0**: Sistema completo de detecção de fraudes implementado
- **v1.1.0**: Adicionado sistema de scoring contínuo (0-100)
- **v1.2.0**: Melhorias nas visualizações e documentação
