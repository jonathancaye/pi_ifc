from firebase import firebase
from time import strftime

data = str(strftime("%Y-%m-%d"))
#hora = str(strftime("%H:%M:%S"))
hora = str(strftime("%H:%M"))

url_firebase = 'https://projeto-rasp-01.firebaseio.com/'
firebase = firebase.FirebaseApplication(url_firebase, None)

# variaveis do leitor
kWh = 12345.0
kVArh = 01234.0
V = 230.0
A = 005.0
kW = 11.50
kVAr = 00.00
kVA = 11.50
p = 00.00

#JSON file
dados_enviar = {"Consumo_Ativo": kWh,
                "Consumo_Reativo": kVArh,
                "Voltagem": V,
                "Corrente": A,
                "Potência_Ativa": kW,
                "Potência_Reativa": kVAr,
                "Potência_Aparente": kVA,
                "Fator_Potência": p,
                }

# firebase.put(url, name, data)
# URL = profundidade da pasta
# name = conteiner de dados
# data = JSON file
URL = 'Medições/' + 'Medidor-01/' + data    # PROFUNDIDADE
NAME = hora                                 # CONTEINER
DATA = dados_enviar                         # JSON

# envia para o firebase
firebase.put(URL, NAME, DATA)
print('[OK] Armazenado no FireBase')
