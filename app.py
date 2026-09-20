tipo = input("Qual o tipo de uso de seu imóvel? (1=comercial, 2=casa ou 3=apartamento)")
consumo = float(input("Qual o consumo mensal de água em volume (m³)?"))    
if tipo == "3" and consumo <= 10:
    print("Consumo econômico – excelente controle de água!")
elif tipo == "3" or tipo == "2" and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")
elif tipo == "3" or tipo == "2" and consumo > 25:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
else:
    print("Tarifa comercial aplicada – consulte o plano corporativo.")