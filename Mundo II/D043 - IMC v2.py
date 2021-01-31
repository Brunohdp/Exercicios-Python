print('\033[36;1m-='*6, '\033[4mDESAFIO 043 - IMC V2\033[0;1;36m', '=-'*6)
kg = float(input('\033[m| Digite seu peso: '))
m = float(input('| Digite sua altura (m): '))
imc = kg / (m**2)
print('\033[34;1m-'*60)
print('\033[31;1;4mProcessando...\033[m')
print('\033[34;1m-'*60)

if imc < 18.5:
    print(f'\033[mO seu \033[32;4;1mIMC\033[m é de \033[33;4;1m{imc:.1f}\033[m. Você está \033[1;4;33mABAIXO DO PESO\033[m!')
elif 18.5 <= imc <= 25:
    print(f'\033[mO seu \033[32;4;1mIMC\033[m é de \033[33;4;1m{imc:.1f}\033[m. Você está no seu \033[1;4;32mPESO IDEAL\033[m!')
elif 25 < imc <= 30:
    print(f'\033[mO seu \033[32;4;1mIMC\033[m é de \033[33;4;1m{imc:.1f}\033[m. Você está com \033[1;4;35mSOBREPESO\033[m!')
elif 30 < imc <= 40:
    print(f'\033[mO seu \033[32;4;1mIMC\033[m é de \033[33;4;1m{imc:.1f}\033[m. Você está com \033[1;4;33mOBESIDADE\033[m!')
else:
    print(f'\033[mO seu \033[32;4;1mIMC\033[m é de \033[33;4;1m{imc:.1f}\033[m. Você está com \033[31;4;1mOBESIDADE MÓRBIDA\033[m!')
