def maior_possivel(digitos, remover, indice):
  if remover == 0: # quantidade de numeros a serem removidos for 0 retorna os digitos que restaram a partir do indice.
    return digitos[indice:]
  if len(digitos) - indice == remover: #se o tamanho da lista digitos menos o indice atual for igual ao tamanho dos numeros a serem removidos, ele retorna uma str vazia
    return ""
  
  digito_maximo = "-1" #começamos essa variavel com -1 para garantir que seja substituida
  indice_do_maximo = indice
  ultimo_indice = len(digitos) - remover
  
  for i in range (indice, ultimo_indice + 1): #percorrendo a lista e armazenando os maiores digitos
    if digitos[i] > digito_maximo:
      digito_maximo = digitos[i]
      indice_do_maximo = i
      if digito_maximo == '9':
        break
  return digito_maximo + maior_possivel(digitos, remover - (indice_do_maximo - indice), indice_do_maximo + 1) #recursão 
      
def entrada():
  while True:
    try:
      A, B = [int(i) for i in input().strip().split()] #receber as variaveis
      digitos = input().strip() #receber a sequencia
      resultado = maior_possivel(digitos, B, 0) #chamando a funçao para calcular os maiores digitos
      print(resultado)
    except EOFError:
      break
    


if __name__ =="__main__":
  entrada()
  
    