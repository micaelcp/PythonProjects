"""
Operadores aritmetricos
Adição (+)
Subtração (-)
Divição (/)
Multiplicação (*)
Modulo (%)
Exponenciação (**)
Parte inteira (//)

soma = 5 + 5
sub = 6 - 4
mult = 8 * 8
div = 4 / 2
mod1 = 4 % 2
mod2 = 5 % 2
exp = 5 ** 2
part = 8 // 5

print(soma, sub, mult, div, mod1, mod2, exp, part)

Operadores de Comparação

maior que (>)
menor que (<)
igual a (==)
diferente de (!=)
maior ou igual a (>=)
menor ou igual a (<=)

print(5 > 8)
print(5 < 8)
print(5 == 8)
print(5 != 8)
print(5 >= 8)
print(5 <= 8)

Operadores Lógicos

verifica se as duas condições são verdadeiras (and)
verifica se uma das condições é verdadeira (or)
inverte o valor booleano (not)
verifica se algo é igual a outro (is)

ativo = True
logado = False

print(ativo == True and logado == False)
print(ativo == True or ativo == False)
print(logado is True)
print(not ativo)

is possui outras funções falar depois ussando dir() no terminal


Manipulação de string

frase = 'Qualquer CoiSa r'

print(len(frase))
print(frase.replace('Qualquer', 'Uma'))#troca o primeiro paremtro da string pelo segundo
print(len(frase))#traz o tamanho da frase
print(frase.count('r'))#conta a quantidade de r
print(frase.find('r'))#traz a posição do primeiro r
print(frase.split())#separa os caracteres da string e coloca em uma lista
print(frase.upper())#tranforma a string inteira para maiusculo
print(frase.lower())#tranforma a string inteira para minusculo
print(frase.title())#tranforma a primeira letra de cada string para maisculo
print(frase.swapcase())#inverte a palavra o que estava maisculo vira minusculo e vice versa
print(frase.isupper())#verifica se a string é maiuscula
print(frase.islower())#verifica se a string é minuscula
print(frase.isalnum())#verifica se a string é número
print(frase.isalpha())#verifica se a string é letra
print(frase.isdigit())#verifica se a string é digito
print(frase.isspace())#verifica se a string é espaço
"""

"""
Estruturas condicionais
if, else ,elif
"""
"""
Estrutura condicional if, else em C

if(idade < 18){
    printf("menor de idade");
}else if(idade == 18){
    printf("Tem 18 anos");
}else{
    printf("maior de idade");
}
"""

"""
Estrutura condicional if, else em Java

if(idade < 18){
    System.out.println("menor de idade");
}else if(idade == 18){
    System.out.println("Tem 18 anos");
}else{
    System.out.println("maior de idade");
}
"""
idade = 26

if idade < 18:
    print("menor de idade")
elif idade == 18:
    print("tem 18 anos")
elif idade == 24:
    print("tem 24 anos")
else:
    print("maior de idade")

"""Estruturas Lógicas: and (e), or (ou), not (não), is (é)
Operadores unários:
    -not 
Operadores binários:
    -and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True   
Para o 'or', um ou outro valor precisa ser True 
Para o 'not', o valor do booleano é invertido 
Para o 'is', o valor é comparado com outro


ativo = False
logado = True

if ativo or logado:
    print("Bem-vindo usuário!")
else:
    print("Voce precisa ativar sua conta. Por favor, cheque seu e-mail")
"""

"""
#se não estiver ativo
if not ativo:
    print("Voce precisa ativar sua conta. Por favor, cheque seu e-mail")
else:
    print("Bem-vindo usuário!")
"""

"""
print(ativo is True)
"""
ativo = False
logado = True
nome = "daniel"
if ativo and logado:
    print("Bem-vindo usuário!")
else:
    print("Voce precisa ativar sua conta. Por favor, cheque seu e-mail")

"galera estava certo antes so tinha esquecido de mudar de ativo para nome"
if nome.isalpha():
    print("ok")
else:
    print("not ok")