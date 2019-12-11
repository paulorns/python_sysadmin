import logging

logging.basicConfig(
    filename = 'aula10.log',
    level = logging.DEBUG,
    format = '%(asctime)s [ %(levelname)s ] %(name)s\n %(funcName)s [%(filename)s, %(lineno)sl ] %(message)s',
    # Retorno:
    # 22:00 [info] python app [app.py, 23] module not found
    datefmt = '[ %d/%m/%Y %H:%M:%S ]'
)

logging.debug('Mensagem de Debug')
logging.info('Mensagem de info')
logging.warning('Mensagem de warning')
logging.error('Mensagem de error')
logging.critical('Mensagem de critical')


# Usando logs

def soma(n1, n2):
    return n1 + n2
try:
    a = soma(3,3)
    logging.info(f'Soma efetuada com sucesso, {a}')
    print(a)
except TypeError as v:
    logging.error(v)