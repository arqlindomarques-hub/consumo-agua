os.system ("cls" if os.name =="nt" else "clear")
#limpa o sistema
tipo = input("Qual o tipo de uso de seu imóvel? (1=comercial, 2=casa ou 3=apartamento)")
#entrada de informação, no caso tipo de apartamento, por número
consumo = float(input("Qual o consumo mensal de água em volume (m³)?"))  
#entrada de informação, consumo em volume, número  
if tipo == "3" and consumo <= 10:
    #se for apartamento e o consumo for menor ou igual a 10, então:
    print("Consumo econômico – excelente controle de água!")
elif tipo == "3" or tipo == "2" and consumo <= 25:
    #se for apartamento ou casa e o consumo for menor ou igual a 25, então:
    print("Consumo moderado – dentro do padrão residencial.")
elif tipo == "3" or tipo == "2" and consumo > 25:
    #se for apartamento ou casa e o consumo for maior que 25, então:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
else:
    #se for comercial, então:
    print("Tarifa comercial aplicada – consulte o plano corporativo.")