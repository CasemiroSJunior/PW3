dict_valores = {
    '1':'um',
    '2':'dois',
    '3':'três',
    '4':'quatro',
    '5':'cinco',
    '6':'seis',
    '7':'sete',
    '8':'oito',
    '9':'nove',
    '10':'dez',
    '11':'onze',
    '12':'doze',
    '13':'treze',
    '14':'quatorze',
    '15':'quinze',
    '16':'dezesseis',
    '17':'dezessete',
    '18':'dezoito',
    '19':'dezenove',
    '20':'vinte',
    '30':'trinta',
    '40':'quarenta',
    '50':'cinquenta',
    '60':'sessenta',
    '70':'setenta',
    '80':'oitenta',
    '90':'noventa',
    '100':'cem',
}


def cheque(valor):
    result = ''
    real, centavos = valor.split('.')
    if (int(real) > 1):
        result = dict_valores.get(real) + ' reais e ' + dict_valores.get(centavos) + " centavos"
    elif (int(real) == 1):
        result = dict_valores.get(real) + ' real e ' + dict_valores.get(centavos) + " centavos"
    else:
        result = dict_valores.get(centavos) + ' centavos'
    print(result)
    return result


assert cheque('0.50') == 'cinquenta centavos'
assert cheque('0.40') == 'quarenta centavos'
assert cheque('0.30') == 'trinta centavos'
assert cheque('0.20') == 'vinte centavos'
assert cheque('0.10') == 'dez centavos'
assert cheque('0.11') == 'onze centavos'
assert cheque('0.21') == 'vinte e um centavos'
assert cheque('1.50') == 'um real e cinquenta centavos'