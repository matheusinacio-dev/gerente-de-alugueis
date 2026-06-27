# Gerenciador de Aluguéis
## Gerencie os aluguéis, prazos e vencimentos dos seus bens mais valiosos direto do terminal

Esse programa Python fornece suporte para o cadastro e aluguél de bens únicos, sendo recomendado para empresas cansadas do controle analógico. Dessa forma, o empréstimo de maquinários ou equipamentos tecnológicos pode ser gerido sem problemas.

Nossa solução oferece rastreabilidade dos aluguéis, exigindo do usuário: nome, nome do cliente e data de devolução. Enquanto preenche automaticamente a data em que o produto foi alugado.

### Prévia

![Demo](assets/demo.gif)

### Como instalar e deixar pronto para uso (ou editar você mesmo)?

**Para rodar o programa**

Pré-requisito: [Python 3.10 ou superior](https://www.python.org/downloads/)

1. Baixe o arquivo `.py`
2. Abra com o Python
3. Use o menu como guia de navegação

> Não esqueça de salvar seus dados usando a opção `0` do menu. O arquivo `.json` gerado precisa estar na mesma pasta que o `.py` para funcionar corretamente.

---

**Para editar o código**

Pré-requisitos:
- [Git](https://git-scm.com/)
- Editor de código — recomendamos o [VS Code](https://code.visualstudio.com/download)

Com o terminal aberto no VS Code, clone o repositório:

```bash
git clone https://github.com/matheusinacio-dev/gerente-de-alugueis.git
```

Faça as alterações desejadas.


### Principais Funcionalidades

1 - Cadastro de novo produto (com os atributos: "nome_produto" e "descrição")
2 - Aluguél de produtos cadastrados (com os atributos adicionais: "nome_funcionario", "cliente", "data de aluguél" e "data de devolução")
3 - Devolver produto alugado que expira hoje (Exibe os aluguéis expirantes hoje para realizar a devolução)

### Como mantemos seus dados entre sessões?

O comportamento padrão dos dados preenchidos no terminal é sumir após o terminal ser encerrado ("morto").
Para evitar isso, criamos a funcionalidade "0 - Salvar lista de produtos". Que salva os dados coletados durante o uso (lista de diciónarios em python) em um arquivo especial .json (que é uma formatação de dados muito compatível a lista de dicionários em python). 
Em um primeiro uso, ao salvar, esse arquivo é criado. Nos usos seguintes, é atualizado.

Por fim esses dados salvos em .json são interpretados pela função carregar_produtos(), convertidos novamente em listas de dicionários em python e salvos na "variável principal" produtos. 

### Limitações atuais

Atualmente, a devolução de equipamentos só pode ser feita no dia do vencimento do prazo de aluguél (último dia). Isso limita  o uso real. Mas foi projetado para exibir e devolver apenas os aluguéis expirantes no dia.

Os vencimentos mensais, acessados pela opção do "menu principal" 4 - "Checar Vencimentos Mensais", são filtrados apenas pelo mês e ano (de hoje). Assim, mesmo que os prazos de aluguél estejam vencidos, o produto continua a ser exibido.
Devido a natureza de relátorio dessa funcionalidade, decidimos manter assim, haja vista que alguns prazos de vencimento podem atrazar.



### O que aprendemos durante o desenvolvimento?

Percebemos o uso real de estruturas condicionais (if/else e match/case) e de estruturas de repetição (for e while).
Da importãncia de dividir o código em funções, para:
- fácil identificação e resolução de problemas;
- fácil manutenção;
- reutilização de códigos repetitivos.

Também utilizamos algumas bibliotecas (date time, json e os) como soluções adequadas para construirmos algumas funcionalidades e diferenciais de uso, como melhor rastreabilidade.
