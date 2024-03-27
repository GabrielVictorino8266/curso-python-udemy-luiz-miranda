nome = "Gabriel"
altura = 1.8
peso = 75
calculo_imc = (peso / (altura**2))

print(nome," tem ", altura, ", \npesa ", peso, " kg e seu IMC e: ", calculo_imc)

print(f"""
Nome: {nome},
Altura: {altura},
Peso: {peso},
IMC: {calculo_imc:.2f}
""")