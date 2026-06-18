'''
Importar da biblioteca datetime a parte "datetime"
Explicação do uso em código:
Criamos a variável data_hora para armazenar as informações de data e horário.
Atribuimos a ela o valor datetime.now() 
    - que dentro da biblioteca datetime pega as informações do momento presente, isso é do prenchimento das perguuntas.
Depois formatamos os dados capturados usando o método com a seguinte ordem:
    .strftime("Dia/Mês/Ano - Horas: Minutos")
'''

from datetime import datetime

'''
Função validar_prenchimento recebe o parametro mensagem, que é prenchido pelo usuário.
Nessa função, temos um loop infinito com uma simples validação de valor não vazio. 
Se o valor é prenchido, o return confirma o resultado e sai do loop. 
Se não, exibe um aviso no terminal e o loop infinito roda de novo. 
Assim o usuário pode prencher o campo.
'''

def validar_prenchimento(mensagem):
    while True:
        valor = ""
        # O método strip() remove os espaços em branco no início e no fim da string, quando nenhum parâmetro é passado.
        # Garantindo que as comparações sejam feitas com os valores tratados e assim, evitando erros. 
        valor = input(mensagem).strip()

        if valor:
            return valor

        print("Erro: o campo não pode ficar vazio.")






produtos = []
booleano = True

while booleano :
   '''
    Cria um dicionário novo a cada volta do loop. Sem que os dados persistam depois de usados.
        - Devido ao "coletor de lixo" do python, que verá a lista produtos como a única referência.
    Evitando que os valores das próximas voltas sejam sobre-escritos pelos valores da volta 1. 
    Caso criassemos uma variável global, teríamos um único endereço de informações para ser ocupado. 
        - Então as informações repetiriam a cada volta do loop.
    Já com a variável local, a cada volta um novo endereço é criado.
   '''
   produto = {} 
   funcionario = validar_prenchimento("Qual o seu nome? ")
   nome_prod = validar_prenchimento("Nome do Produto: ")
   '''
   Explicação do prenchimento do estado:
   S/s e N/n atribuem respectivamente os valores "disponível" e "em uso".
    - Quebrando  o loop infinito e dando sequência aos questionamentos.
   Qualquer outra resposta dispara um aviso e exibe a "pergunta" novamente.
   '''

   while True:
        qual_estado = validar_prenchimento(f"Preste atenção!!! \nO produto está disponível? (S - disponível | N - em uso) ")
        if qual_estado.lower() == "s":
            estado = "disponível"
            break
        elif qual_estado.lower() == "n":
            estado = "em uso"
            break
        else :
            print(f"Por favor, prencha o estado corretamente.")
            continue
   qnt = int(validar_prenchimento("Quantidade: "))
   cliente = validar_prenchimento("Nome do cliente: ")
   data_hora = datetime.now().strftime("DATA: %d/%m/%Y HORA: %H:%M") # explicação na linha 1, junto do import

   produto.update({
        "nome": nome_prod,
        "estado": estado,
        "qnt": qnt,
        "cliente": cliente,
        "funcionário": funcionario,
        "data_hora": data_hora
    })
   produtos.append(produto)
    
   quer_continuar = validar_prenchimento("Você deseja cadastrar outro produto? (S) - Sim | (N) - Não: ")
   if quer_continuar.lower() == "s":
        booleano = True
   else :
        booleano = False
       
   print(produtos)

