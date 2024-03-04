# TPC3 De PL

### Descrição do Problema

Para este exercício, é necessário criar um programa que some todas as sequências de dígitos que encontre num texto. Quando se encontrar a string "on" começa-se a somar todos os números que se encontrar a um contador. Se for encontrada a string "off" não se adiciona mais ao contador até encontrar outro "on". Caso encontre o caráter "=" deve devolver a soma até esse caráter.
Para este fim, foram utilizadas expressões regulares (Regex) para a leitura e adição dos elementos textuais necessários para a resolução do exercício.

### Explicação da resolução do exercício:

Primeiramente coloca-se todos os números e strings pedidos pelo exercício numa lista. Depois percorre-mo-la, somando sempre que o contador estiver ativo, ou seja, quando a string "on" começou a permitir a contagem e nenhuma string "off" foi encontrada desde essa "on", as sequências de números ao contador.Quando é encontrado um "=" é devolvido o valor da soma.

Para a execução do código, este foi executado como normal e é passado um ficheiro de input que vai ser analizado.

### Teste

ao12sdohaohddon13houfha03nvoawoFfndnaowi=asdawg
daowdhoh=13412Onadsniuhaasdon23anodd akwd=no
26auiwfa babsfasfaongffdapdjasodoff231

José Eduardo Silva Monteiro Santos Oliveira, A100547