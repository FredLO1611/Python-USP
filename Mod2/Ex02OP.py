info = (int(input("Por favor, entre com o número de segundos que deseja converter: ")))
# dias = info//86400
# horas = (info%86400)/3600
# minutos = (horas%3600)
# segundos = (minutos%60)
dias = info//86400
resto1 = info-dias*86400
horas = resto1//3600
resto2 = resto1-horas*3600
minutos = resto2//60
resto3 = resto2 - minutos*60
segundos = resto3

print(f"{int(dias)} dias, {int(horas)} horas, {int(minutos)} minutos e {int(segundos)} segundos.")