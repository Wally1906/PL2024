# TPC2 De PL

### Descrição do Problema

Para este exercício, é necessária a criação em Python um conversor dos elementos descritos na "Basic Syntax" de MarkDown para HTML. Para este fim, foram utilizadas expressões regulares (Regex) para a leitura e substituição dos elementos textuais desejados pelo exercício.

### Explicação da resolução do exercício:

Foi criada uma função parser, que lê o ficheiro HTML e vai substituindo as expressões em MarkDown pelas correspondentes em HTML. Para a conversão de todos os elementos, exceto da Lista Numerada, foram utilizadas expressões regulares da maneira convencionak. Para o caso específico da Lista Numerada, primeiro a lista é substituida apenas pelo <li></li> com o conteúdo de cada elemento. Depois(apesar de não ser a forma mais eficiente de ser feita) é lido o ficheiro outra vez para apanhar cada uma das listas completas e colocá-la entre os identificadores <ol></ol>

Para a execução do código, este foi executado como normal e funciona através da criação de um ficheiro .md que vai ser passado como argumento, e depois vai ser criado um ficheiro .html com o resultado.

### Teste

**Aqui estao alguns exemplos que podem** ser convertidos *para .html para ser testado*

1. Lista 1 elemento 1
2. Lista 1 elemento 2
3. Lista 1 elemento 3
4. Lista 1 elemento 4

`Nova Lista`

1. Lista 2 elemento 1
2. Lista 2 elemento 2
3. Lista 2 elemento 3
4. Lista 2 elemento 4


José Eduardo Silva Monteiro Santos Oliveira, A100547