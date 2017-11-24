import json
from urllib.request import urlopen

crastreio=input("Entre com o código de rastreio: ")
url="http://api.postmon.com.br/v1/rastreio/ect/"+crastreio

resp = urlopen(url).read().decode('utf-8')
respJson = json.loads(resp)

print ( )
print ("=====================================")
print ( )
print ("Situação para o código de rastreio {}".format(respJson["codigo"]))
print ( )
print ("====== Histórico ======")
print ( )

historico = respJson["historico"]
i = 0
while i < len(historico):
	info = (historico[i])
	print ("Detalhes: {}".format(info['detalhes']))
	print ("Local: {}".format(info['local']))
	print ("Data: {}".format(info['data']))
	print ("Situação: {}".format(info['situacao']))
	print ( )
	i = i + 1

print ("=====================================")