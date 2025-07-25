# -*- coding: utf-8 -*-
"""calculo_metricas_ML.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aVD-XwCaBpoTAikEZFhRQNQlWj1HnPHP
"""

# 1. Importar bibliotecas
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix

# 2. Carregar dados
data = load_breast_cancer()
X, y = data.data, data.target

# 3. Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

modelo = DecisionTreeClassifier(random_state=42, max_depth=5)
modelo.fit(X_train, y_train)

# 5. Fazer previsões
y_pred = modelo.predict(X_test)

# 6. Matriz de confusão
matriz_confusao = confusion_matrix(y_test, y_pred)
print('Matriz de confusão:\n', matriz_confusao)

vn, fp, fn, vp = matriz_confusao.ravel()

# Total de amostras
N = vn + fp + fn + vp


sensibilidade = vp / (vp + fn)
especificidade = vn / (vn + fp)
acuracia = (vp + vn) / N
precisao = vp / (vp + fp)
f_score = 2 * (precisao * sensibilidade) / (precisao + sensibilidade)


print(f'\nAcurácia:       {acuracia:.3f}')
print(f'Sensibilidade:  {sensibilidade:.3f}')
print(f'Especificidade: {especificidade:.3f}')
print(f'Precisão:       {precisao:.3f}')
print(f'F1-Score:       {f_score:.3f}')