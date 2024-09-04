import json

def calcularFaturamento():
    with open('dados.json', 'r') as file:
        dados = json.load(file)

    #Filtra apenas os dias com faturamento (valor > 0)
    faturamentoDiario = [dia['valor'] for dia in dados if dia['valor'] > 0]

    #Calcula o menor e o maior valor de faturamento
    menorValor = min(faturamentoDiario)
    maiorValor = max(faturamentoDiario)

    #Calcula a média mensal
    mediaMensal = sum(faturamentoDiario) / len(faturamentoDiario)

    #Conta os dias com faturamento superior à média mensal
    acimaMedia = sum(1 for valor in faturamentoDiario if valor > mediaMensal)

    #Exibe os resultados
    print(f"Menor valor de faturamento: {menorValor:.2f}")
    print(f"Maior valor de faturamento: {maiorValor:.2f}")
    print(f"Número de dias com faturamento acima da média: {acimaMedia}")

# Chama a função para executar o cálculo
calcularFaturamento()
