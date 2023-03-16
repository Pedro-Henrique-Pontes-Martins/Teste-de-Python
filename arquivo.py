nascimento = 2000
nome = 'Pedro'
anoAtual = 2023

def calcularIdade(nome, nascimento, anoAtual):
    idade = str(anoAtual - nascimento)
    print('A idade de '+ nome +' é de ' + idade +' anos.')

calcularIdade(nome, nascimento, anoAtual)
