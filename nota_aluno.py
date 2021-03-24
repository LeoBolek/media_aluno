# Cálculo básico da média do aluno

nota_1 = float(input('Insira a primeira nota do aluno: '))
nota_2 = float(input('Insira a segunda nota do aluno: '))
nota_3 = (nota_1 + nota_2) / 2
print(f'A nota do aluno foi {nota_3}')

if(nota_3 >= 5):
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')

