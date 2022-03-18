v_numerico1=int(input('digite el primer velor: '))
v_numerico2=int(input('digite el segundo valor: '))
operando=input('digite el operando: ')

match operando:
    case '+':
        resultado = v_numerico1 + v_numerico2
    case '-':
        resultado = v_numerico1 - v_numerico2
    case '*':
        resultado = v_numerico1 * v_numerico2
    case '/':
        resultado = v_numerico1 / v_numerico2
    case _:
        resultado = None
        print('Operación inválida')

if resultado is not None:
    print(f'{v_numerico1}{operando}{v_numerico2} = {resultado}')
