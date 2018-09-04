from firebase import firebase
url_firebase = 'https://projeto-rasp-01.firebaseio.com/'
firebase = firebase.FirebaseApplication(url_firebase, None)

ender = '/Medições' + '/Medidor-01' + '/2018-09-02'
consulta = '/22:52'

result = firebase.get(ender, consulta)

print('-=' * 20)

for key, value in result.items():
    print(f'{key:<20}', end='')
    print(f'{value:>20}')

print('-=' * 20)
