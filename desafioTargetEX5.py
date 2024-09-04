
texto = input("Informe uma string para ser invertida: ")
#variavel que irá guardar a string invertida
texto_invertido = ""

#for para percorrer a string de trás para frente
for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]

print("String invertida:", texto_invertido)
