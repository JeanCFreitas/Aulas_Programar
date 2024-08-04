num=int(input('Digite Numero entre 0 e 100:'))
chv=25
dst=0
if(num>100 or num<0):
    print('ERRO: NÚMERO MAIOR QUE 0 OU MENOR QUE 100')
elif(num>chv):
    print(f"chave é {chv}")
    dst=num-chv
    print(f"A diferença entre {num} e {chv} é {dst}")
else:
    print(f"chave é {chv}")
    dst=chv-num
    print(f"A diferença entre {num} e {chv} é {dst}")
