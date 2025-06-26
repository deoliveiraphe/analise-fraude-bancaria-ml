"""
Utilitários gerais para o projeto de detecção de fraudes bancárias
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict, Any, Optional, Tuple
import warnings
warnings.filterwarnings('ignore')

def configurar_visualizacao():
    """
    Configura o ambiente de visualização com estilos personalizados
    """
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 12
    print("✅ Configurações de visualização aplicadas!")

def resumo_dataset(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Gera um resumo completo do dataset
    
    Args:
        df: DataFrame a ser analisado
        
    Returns:
        Dict com informações do dataset
    """
    resumo = {
        'shape': df.shape,
        'memory_usage_mb': df.memory_usage(deep=True).sum() / 1024**2,
        'missing_values': df.isnull().sum().sum(),
        'duplicates': df.duplicated().sum(),
        'numeric_columns': df.select_dtypes(include=[np.number]).columns.tolist(),
        'categorical_columns': df.select_dtypes(include=['object']).columns.tolist(),
        'datetime_columns': df.select_dtypes(include=['datetime64']).columns.tolist()
    }
    
    return resumo

def identificar_target(df: pd.DataFrame, possible_names: List[str] = None) -> Optional[str]:
    """
    Identifica automaticamente a coluna target do dataset
    
    Args:
        df: DataFrame
        possible_names: Lista de possíveis nomes para a variável target
        
    Returns:
        Nome da coluna target ou None se não encontrada
    """
    if possible_names is None:
        possible_names = ['fraud', 'is_fraud', 'fraudulent', 'target', 'label', 
                         'class', 'is_fraudulent', 'fraud_flag', 'fraude']
    
    for col in df.columns:
        if col.lower() in [name.lower() for name in possible_names]:
            return col
    
    return None

def analise_balanceamento(df: pd.DataFrame, target_col: str) -> Dict[str, Any]:
    """
    Analisa o balanceamento da variável target
    
    Args:
        df: DataFrame
        target_col: Nome da coluna target
        
    Returns:
        Dict com informações sobre o balanceamento
    """
    target_counts = df[target_col].value_counts()
    target_percentages = df[target_col].value_counts(normalize=True) * 100
    
    resultado = {
        'counts': target_counts.to_dict(),
        'percentages': target_percentages.to_dict(),
        'classes': len(target_counts)
    }
    
    if len(target_counts) == 2:
        minority_class = target_counts.min()
        majority_class = target_counts.max()
        resultado['imbalance_ratio'] = majority_class / minority_class
        
        if resultado['imbalance_ratio'] > 10:
            resultado['status'] = 'Altamente desbalanceado'
        elif resultado['imbalance_ratio'] > 3:
            resultado['status'] = 'Moderadamente desbalanceado'
        else:
            resultado['status'] = 'Relativamente balanceado'
    
    return resultado

def detectar_outliers_iqr(series: pd.Series, multiplicador: float = 1.5) -> Tuple[List, List]:
    """
    Detecta outliers usando método IQR
    
    Args:
        series: Série pandas
        multiplicador: Multiplicador do IQR para definir outliers
        
    Returns:
        Tupla com (indices_outliers, valores_outliers)
    """
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - multiplicador * IQR
    limite_superior = Q3 + multiplicador * IQR
    
    outliers_mask = (series < limite_inferior) | (series > limite_superior)
    outliers_indices = series[outliers_mask].index.tolist()
    outliers_values = series[outliers_mask].values.tolist()
    
    return outliers_indices, outliers_values

def criar_relatorio_qualidade(df: pd.DataFrame) -> str:
    """
    Cria um relatório de qualidade dos dados
    
    Args:
        df: DataFrame a ser analisado
        
    Returns:
        String com o relatório formatado
    """
    resumo = resumo_dataset(df)
    
    relatorio = f"""
    🔍 RELATÓRIO DE QUALIDADE DOS DADOS
    ===================================
    
    📊 Dimensões: {resumo['shape'][0]:,} linhas × {resumo['shape'][1]} colunas
    💾 Tamanho: {resumo['memory_usage_mb']:.2f} MB
    
    🧹 Qualidade:
    • Valores ausentes: {resumo['missing_values']:,}
    • Registros duplicados: {resumo['duplicates']:,}
    
    🏷️  Tipos de variáveis:
    • Numéricas: {len(resumo['numeric_columns'])}
    • Categóricas: {len(resumo['categorical_columns'])}
    • Data/Hora: {len(resumo['datetime_columns'])}
    
    """
    
    # Status geral
    if resumo['missing_values'] == 0 and resumo['duplicates'] == 0:
        relatorio += "✅ STATUS GERAL: EXCELENTE qualidade dos dados!\n"
    elif resumo['missing_values'] < len(df) * 0.05 and resumo['duplicates'] < len(df) * 0.01:
        relatorio += "✅ STATUS GERAL: BOA qualidade dos dados\n"
    else:
        relatorio += "⚠️  STATUS GERAL: Dados necessitam limpeza\n"
    
    return relatorio

def salvar_dataset_processado(df: pd.DataFrame, caminho: str, nome_arquivo: str):
    """
    Salva o dataset processado
    
    Args:
        df: DataFrame a ser salvo
        caminho: Caminho para salvar
        nome_arquivo: Nome do arquivo
    """
    import os
    
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    
    filepath = os.path.join(caminho, nome_arquivo)
    df.to_csv(filepath, index=False)
    print(f"✅ Dataset salvo em: {filepath}")
    print(f"📊 {len(df):,} registros salvos")
