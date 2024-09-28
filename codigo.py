import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados de exemplo para o supermercado
dados_supermercado = {
    'Produto': ['Arroz', 'Feijão', 'Leite', 'Ovos', 'Óleo', 'Macarrão', 'Sabão', 'Detergente', 'Café', 'Açúcar'],
    'Categoria': ['Alimentos', 'Alimentos', 'Laticínios', 'Alimentos', 'Alimentos', 'Alimentos', 'Limpeza', 'Limpeza', 'Bebidas', 'Alimentos'],
    'Preço Unitário': [10, 8, 5, 12, 7, 6, 15, 3, 12, 4],
    'Quantidade Vendida': [300, 250, 100, 50, 20, 350, 40, 60, 80, 120],
    'Estoque': [50, 80, 200, 300, 150, 20, 200, 190, 170, 50],
    'Margem de Lucro (%)': [10, 12, 15, 8, 10, 10, 20, 18, 25, 10]
}

df = pd.DataFrame(dados_supermercado)

# Exibindo o DataFrame
print(df)


# Definindo uma quantidade mínima de vendas esperada
quantidade_minima = 100

# Filtrando produtos com vendas abaixo do esperado
produtos_baixa_venda = df[df['Quantidade Vendida'] < quantidade_minima]
print("Produtos com vendas baixas:\n", produtos_baixa_venda[['Produto', 'Quantidade Vendida']])

# Criando uma coluna que calcula o índice de estoque/vendas
df['Estoque/Vendas'] = df['Estoque'] / df['Quantidade Vendida']

# Filtrando produtos com excesso de estoque (índice alto)
excesso_estoque = df[df['Estoque/Vendas'] > 2]
print("Produtos com excesso de estoque:\n", excesso_estoque[['Produto', 'Estoque', 'Quantidade Vendida', 'Estoque/Vendas']])

# Calculando a margem média de lucro por categoria
margem_por_categoria = df.groupby('Categoria')['Margem de Lucro (%)'].mean()
print("Margem média de lucro por categoria:\n", margem_por_categoria)

# Filtrando categorias com margem de lucro abaixo de um valor mínimo
margem_minima = 12
categorias_baixa_margem = margem_por_categoria[margem_por_categoria < margem_minima]
print("Categorias com margem de lucro baixa:\n", categorias_baixa_margem)

# Gráfico de barras para produtos com excesso de estoque
plt.figure(figsize=(10, 6))
sns.barplot(x='Produto', y='Estoque/Vendas', data=excesso_estoque)
plt.title('Produtos com Excesso de Estoque')
plt.ylabel('Estoque / Quantidade Vendida')
plt.xticks(rotation=45)
plt.show()

# Gráfico de barras para margem média de lucro por categoria
plt.figure(figsize=(10, 6))
margem_por_categoria.plot(kind='bar', color='lightgreen')
plt.title('Margem de Lucro Média por Categoria')
plt.ylabel('Margem de Lucro (%)')
plt.xlabel('Categoria')
plt.show()
