print('Codigo de cargo: \n1 : Enfermeiro \n2 : Nutricionista \n3 : Medico(a)')
qtdenutri=0
totalsaln=0

while True:
    cargo=int(input('Informe um codigo de cargo:'))
    if cargo>=1 and cargo <=3:
        salario=float(input('Salario R$:'))
        if cargo ==2:
            qtdenutri+=1
            totalsaln+=salario
        
        resp=input('Deseja continuar [S/N]:')
        if resp.upper()=='N':
            break
    else:
        print('Codigo invalido!')
if qtdenutri>0:
    media=totalsaln/qtdenutri
    print(f'Media salarial das nutricionistas R$:{media:.2f}')
else:
    print('Nao foram inseridos dados sobre as nutricionistas.')