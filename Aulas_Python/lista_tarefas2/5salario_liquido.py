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
salario_total=0
contas=0
salarioB=float(input('Digite o Salário Bruto:'))
while (salarioB!=0):
    horasexced=0
    custo_hora=0
    saliq_total=0
    
    Horahomem=0
    imposto=0
    encargos=0
    custo_hora=salarioB/160
 
    horas=float(input('Digita as horas trabalhadas no mês:'))
    
    print(f'Salário Bruto: R$ {salarioB}')
    print(f'Horas trabalhadas: {horas}')
    
    if (horas<=160):
        horasexced=0
        print(f'Horas excedentes: {horasexced} horas')
        print(f'Horas c/50% aplicado: {horasexced}')
    
    else:
        horasexced=horas-160
        print(f'Horas excedentes:{horasexced} horas')
        print(f'Horas c/50% aplicado: {(horasexced)*1.5} horas')
        Horahomem=salarioB/160

    
    print(f'Valor hora homem: R$ {Horahomem}')
    adicional=Horahomem*horasexced*1.5
    print(f'Valor adicional p/ horas extras: R$ {adicional}')

    if (salarioB<800):
        
        print(f'Salário Bruto: R$ {salarioB}')

    if (800<=salarioB<=1600):
        imposto=0.08*salarioB
        encargos=0.05*salarioB
        
        print(f'Imposto 8%: R$ {imposto}')
        print(f'Encargos 5%: R$ {encargos}')
    
    if (salarioB>1600):
        imposto=0.15*salarioB
        encargos=0.07*salarioB
        
        print(f'Imposto 15%: R$ {imposto}')
        print("Encargos 7%: R$" ,'%.2f' %encargos)
    
    saliq=salarioB+adicional-imposto-encargos
    print(f'Salário liquido: R$ {saliq}')
    salario_total=salario_total+saliq
    contas=contas+1
    salarioB=float(input('Digite o Salário Bruto:'))

print(f'Total de Salários Liquidos calculados: R$ {salario_total}')
print(f'Você inseriu informações de {contas} funcionarios')