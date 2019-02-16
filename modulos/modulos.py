import time, random, datetime
from datetime import datetime
from subprocess import run, PIPE

from sentidos.som import FREQUENCIA, doppler

print (FREQUENCIA)
doppler()
exit()

r = run(['apt-get', 'install', '-y', 'sl'], stdout=PIPE, stderr=PIPE)
#print(r.stdout.decode('utf-8'))
if  r.returncode != 0:
    print('DEU MERDA...')

letras = ['a', 'f', 'd']

print(random.randint(100, 9999))

time.sleep(2)
print(random.choice(letras))

print(datetime.datetime.now())

hoje = datetime.datetime.now()
print (hoje. strftime('%d/%m/%Y'))
