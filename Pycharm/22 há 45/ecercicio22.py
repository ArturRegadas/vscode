print('\033[0;31mvamos saber algumas coisas sobre seu nome')
nome=input('digite seu nome: ')
print('')
print('\033[34mseu nome somente com letras maiusculas ficaria: \033[1;33m{}\033[m'.format(nome.upper()))
print('\033[1;35m=-\033[m'*35)
print('\033[0;34mseu nome somente com letras minusculas ficaria: \033[1;33m{}\033[m'.format(nome.lower()))
print('\033[1;35m=-\033[m'*35)
substituicao=nome.replace(' ','')
print('\033[34mseu nome tem \033[1;33m{}\033[m \033[34mletras'.format(len(substituicao)))
print('\033[1;35m=-\033[m'*35)
particao=nome.split()
part1=particao[0]
print('\033[34mseu primeiro nome é \033[1;33m{}\033[m\033[34m e ele tem \033[1;33m{}\033[m\033[34m letras '.format(part1, len(part1)))