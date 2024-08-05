#Faça o programa que calcule o salário líquido dos funcionários de uma empresa. O 
#salário líquido é composto por descontos e adicionais, seguindo as seguintes regras: 
#Descontos: 
#Salário bruto < 800,00 – não realizar nenhum desconto; 
#800,00 <= Salário bruto <=1600,00 – descontar 8% de Imposto de Renda e 5% de encargos. 
#>1600,00 – descontar 15% de Imposto de Renda e 7% de encargos. 
#Adicionais: 
#Caso  o  funcionário  tenha  trabalhado  mais  de  160  horas  no  mês,  divida  o  seu  salário 
#bruto  por  160  (representa  horas  trabalhadas)  e  calcule  50%  de  adicional  nas  horas 
#que excederam a 160. 
#O  usuário  deverá  digitar  o  salário  bruto  e  o  número  de  horas  trabalhadas  no  mês  de 
#cada funcionário, e deverá receber como resultado o salário líquido. O usuário poderá 
#calcular salário para N funcionários, para finalizar o programa o usuário deverá digitar 
#0 no salário bruto, ao finalizar o programa exibir o total geral dos salários líquidos.

salarioB=float(input('Digite o Salário Bruto:'))
horas=float(input('Digita as horas trabalhadas no mês:'))


if (salarioB<800):
    print(f'Salário Bruto: R$ {salarioB}')
    print(f'Salário Liquido: R$ {salarioB}')
    
if (800<=salarioB<=1600):
    imposto=0.08*salarioB
    encargos=0.05*salarioB
    saliq=salarioB-imposto-encargos
    print(f'Salário Bruto: R$ {salarioB}')
    print(f'Imposto 8%: R$ {imposto}')
    print(f'Encargos 5%: R$ {encargos}')
    print(f'Salário Liquido: R$ {saliq}')
    
if (salarioB>1600):
    imposto=0.15*salarioB
    encargos=0.07*salarioB
    saliq=salarioB-imposto-encargos
    print(f'Salário Bruto: R$ {salarioB}')
    print(f'Imposto 8%: R$ {imposto}')
    print(f'Encargos 5%: R$ {encargos}')
    print(f'Salário Liquido: R$ {saliq}')

print(f'Horas trabalhadas: {horas}')

if (horas<=160):
    print(f'Horas excedentes: 0')
    print('Horas c/50% aplicado: 0')
else:
    print(f'Horas excedentes:{horas-160}')
    print(f'Horas c/50% aplicado: {(horas-160)*1.5}')
    

