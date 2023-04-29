from datetime import datetime
now = datetime.now().time()     # импорт времечко нынешнее 
#sab = данное событие

def log (now,sab):   #ФУНКЦИЯ LOG
  f = pen('log.txt','r+')
  f.write(f'main:  time-{now}.  ---> text-{sub} \n')
  f.close()

# purpur