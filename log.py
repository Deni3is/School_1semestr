from datetime import datetime
now = datetime.now().time()     # импорт времечко нынешнее 
#sab = данное событие

def log (now,sab):   #ФУНКЦИЯ LOG
  f = pen('log.txt','a')
  f.write(f'main:  time-{now}.  ---> text-{sub} \n')  #sab  данное событие
  f.close()

# purpur