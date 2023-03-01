import json

# 1. Ler o arquivo JSON
with open('dados.json', 'r') as file:
    dados = json.load(file)

faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

# 2. Calcular o menor e o maior valor de faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# 3. Calcular a média mensal de faturamento
media_mensal = sum(faturamento) / len(faturamento)

# 4. Contar o número de dias com faturamento superior à média mensal
dias_acima_da_media = sum(1 for f in faturamento if f > media_mensal)

# Imprimir os resultados
print("Menor faturamento diário:", menor_faturamento)
print("Maior faturamento diário:", maior_faturamento)
print("Número de dias com faturamento acima da média mensal:", dias_acima_da_media)
