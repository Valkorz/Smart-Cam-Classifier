# Checklist: Classificador de Imagens por Categoria

## **1. Definir Objetivo**
- [ ] Determinar o tema das categorias (ex.: curvas e retas, tipos de terreno, etc.).
- [ ] Decidir o número de categorias a serem classificadas.

---

## **2. Coleta ou Criação de Dataset**
- [ ] Escolher a fonte do dataset:
  - [ ] Procurar datasets públicos em plataformas como Kaggle ou Google Dataset Search.
  - [ ] Criar o próprio dataset, capturando imagens e rotulando-as manualmente.
- [ ] Garantir que o dataset esteja balanceado (quantidade similar de imagens por categoria).
- [ ] Dividir o dataset em:
  - [ ] Conjunto de treino (70%).
  - [ ] Conjunto de validação (15%).
  - [ ] Conjunto de teste (15%).

---

## **3. Pré-processamento das Imagens**
- [ ] Redimensionar todas as imagens para o mesmo tamanho (ex.: 128x128 pixels).
- [ ] Normalizar os valores dos pixels para o intervalo `[0, 1]`.
- [ ] Converter os rótulos em formato adequado (ex.: `one-hot encoding`).

---

## **4. Construção do Modelo**
- [ ] Criar uma Rede Neural Convolucional (CNN) usando TensorFlow/Keras:
  - [ ] Definir as camadas (Convolução, Pooling, Flatten, Dense, etc.).
  - [ ] Configurar o otimizador (ex.: Adam) e a função de perda (ex.: categorical crossentropy).
- [ ] Visualizar o resumo do modelo para garantir que a arquitetura está correta.

---

## **5. Treinamento do Modelo**
- [ ] Treinar o modelo com os dados de treino e validação:
  - [ ] Configurar o número de épocas (ex.: 10-20).
  - [ ] Definir o tamanho do batch (ex.: 32).
- [ ] Monitorar o desempenho durante o treinamento (acurácia e perda).

---

## **6. Avaliação do Modelo**
- [ ] Avaliar o modelo usando o conjunto de teste.
- [ ] Calcular métricas como acurácia, precisão e recall.
- [ ] Criar gráficos para visualizar o desempenho (ex.: curvas de treino/validação).

---

## **7. Classificação de Novas Imagens**
- [ ] Criar um script para carregar e classificar novas imagens.
- [ ] Exibir o resultado da classificação no terminal ou salvar os resultados em um arquivo.

---

## **8. Melhorias e Extras**
- [ ] Aplicar aumentação de dados para melhorar a robustez do modelo:
  - [ ] Rotação.
  - [ ] Zoom.
  - [ ] Espelhamento horizontal.
- [ ] Explorar Transfer Learning com modelos pré-treinados (ex.: MobileNet ou ResNet).

---

## **9. Documentação e Organização**
- [ ] Escrever README.md detalhado para o repositório:
  - [ ] Explicar o objetivo do projeto.
  - [ ] Instruções para executar o código.
  - [ ] Ferramentas e bibliotecas necessárias.
- [ ] Organizar o repositório:
  - [ ] Criar pastas para `dataset`, `scripts`, e `model`.
  - [ ] Salvar checkpoints do modelo treinado.

---

## **10. Teste e Feedback**
- [ ] Testar o modelo com diferentes tipos de imagens.
- [ ] Coletar feedback da equipe e iterar sobre o projeto, se necessário.
