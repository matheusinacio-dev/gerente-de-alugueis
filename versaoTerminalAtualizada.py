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
         # O método strip() remove os espaços em branco no início e no fim da string. quando nenhum parâmetro é passado.
         # Garantindo que as comparações sejam feitas com os valores tratados e assim, evitando erros. 
        valor = input(mensagem).strip()

        if valor:
            return valor

        print("Erro: o campo não pode ficar vazio.")


'''
1 - "posicionando" uma lista para receber os valores filtrados - criada depois

    Analogia - "Em casa com goteira, [ ] seca a poça. Já o .clear() tampa a fonte (goteira)"
2 -  método .clear() limpa todos os valores da lista da memória, ideal para vários endereços ("variáveis") com os "mesmos valores" da "mesma fonte (objeto)" .
        O uso é diferente de limpar uma lista com [ ], pois nesse caso os valores são substituidos pelo [ ]. 
        O que significa que caso os valores tenha/estejam em mais de um endereço (variáveis), eles irão continuar existido.
        Logo, a limpeza com [ ] para mais de uma variável com o "mesmo valor" vindo da "mesma fonte (objeto)" não funciona.

3 - percorrer todos os elementos (dicionários) da lista produtos um a um
4 - "variável temporária" produto se torna um dicionário
5 - acessar uma chave do dicionário e verificar se o seu valor corresponde ao estado filtrado
6 - Caso corresponda (True) - adicionar dicionário em uma lista de valores filtrados
'''
def filtrar_estado(nova_lista, estado):
    nova_lista.clear() # Explicação no tópico 2 acima
    for produto in produtos:
        if produto["estado"] == estado:
            nova_lista.append(produto)
    
    

produtos = []
booleano = True


while True:
    atividade = validar_prenchimento(f'''========================================================
Qual ação você deseja executar?
1 - Cadastro de novo produto
2 - Visualização de produtos emprestados ("em uso")
3 - Visualização de produtos disponíveis ("disponível")
                                     
Digite o número da ação desejada:''')
    
    # Dentro do loop infinito, cria uma lógica de navegação centralizada em um menu guiado por números.
    # Em que cada número leva a uma "atividade" diferente definida em cases no match/case
    match atividade:
        case "1":
            while True :
                '''
        Cria um dicionário novo a cada volta do loop. Sem que os dados persistam depois de usados.
            - Devido ao "coletor de lixo" do python, que verá a lista produtos como a única referência.
        Evitando que os valores das próximas voltas sejam sobre-escritos pelos valores da volta 1. 
        Caso criassemos uma variável global, teríamos um único endereço de informações para ser ocupado. 
            - Então as informações repetiriam a cada volta do loop.
        Já com a variável local, a cada volta um novo endereço é criado.
                '''
                produto = {} 

                
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
                            qnt = int(validar_prenchimento("Quantidade: "))
                            produto.update({
                                            "nome_produto": nome_prod,
                                            "estado": estado,
                                            "qnt": qnt,
                                          
                    })
                            produtos.append(produto)
                            print(produtos)
                            break
                        elif qual_estado.lower() == "n":
                            estado = "em uso"
                            qnt = int(validar_prenchimento("Quantidade: "))
                            funcionario = validar_prenchimento("Qual o seu nome? ")
                            cliente = validar_prenchimento("Nome do cliente: ")
                            data_hora = datetime.now().strftime("DATA: %d/%m/%Y HORA: %H:%M") # explicação na linha 1, junto do import
                            produto.update({
                                            "nome_produto": nome_prod,
                                            "estado": estado,
                                            "qnt": qnt,
                                            "cliente": cliente,
                                            "funcionário": funcionario,
                                            "data_hora": data_hora
                    })
                            produtos.append(produto)
                            print(produtos)
                            break
                        else :
                            print(f"Por favor, prencha o estado corretamente.")
                            continue
              
                

             
                quer_continuar = validar_prenchimento("Você deseja cadastrar outro produto? (S) - Sim | (N) - Não: ")
                if quer_continuar.lower() == "s":
                        continue
                else :
                        break
        case "2":
              '''
              Explicação na linha 35 
              - aqui o paramêtro nova_lista antes "posicionado" recebe a lista produtos_emprestados criada
              '''
              produtos_emprestados = []
              filtrar_estado(produtos_emprestados, "em uso")
              
              print(f"Essa é a lista de produtos emprestados:\n{produtos_emprestados}")       

        case "3":
              '''
              Explicação na linha 35 
              - aqui o paramêtro nova_lista antes "posicionado" recebe a lista produtos_disponiveis criada
              '''
              produtos_disponiveis = []
              filtrar_estado(produtos_disponiveis, "disponível")
              
              print(f"Essa é a lista de produtos disponíveis:\n{produtos_disponiveis}")  
