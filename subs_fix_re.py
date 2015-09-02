import re
from datetime import datetime

def time_replacer(time_list):
  temp = []
  new_list = []
  new_temp = []
  for i in time_list:
    temp = i.split(':')
    msec = str(int(temp[2].split(',')[1])*1000)
    sec = temp[2].split(',')[0]
    min_ = temp[1]
    hr = temp[0]
    #create the datetime object of old time
    orig = datetime.strptime(hr + ':' + min_ + ':' + sec + '.' + msec, "%H:%M:%S.%f")
    delta = datetime.strptime('00:00:07.250000', "%H:%M:%S.%f")#write here by how much you want to move the subs behind
    final = orig - delta#comment it out if you want to postpone subs

    #for adding delay to the subs, we have to postpone them by delta
    '''origin = datetime.strptime('00:00:00.000000', "%H:%M:%S.%f")
    block = delta - origin
    final = orig + block
    final = str(final)
    temp[0] = final.split(':')[0].split(' ')[-1]'''

    #print final.split(':')[1]
    final = str(final)#comment this out too
    temp[0] = final.split(':')[0]#comment this out too
    temp[1] = final.split(':')[1]
    new_temp = final.split(':')[2].split('.')
    if len(new_temp) == 1:
      new_temp.append('0')
    #print new_temp
    #print new_temp[0], new_temp[1]
    new_temp[1] = str(int(new_temp[1])/1000)
    temp[2] = ','.join(new_temp)
    #final =
    new_list.append(':'.join(temp))
  return new_list[0] + ' --> ' + new_list[1]


regex = '\d\d:\d\d:\d\d,\d\d\d'
pattern = re.compile(regex)

f = open('C:\Users\Gaurav\Desktop\content.srt', 'r')#enter the directory of original subs file
f2 = open('subs.txt', 'w')

while True:
  check = f.readline()
  time_list = re.findall(pattern, check)
  if len(time_list) > 0:
    text = time_replacer(time_list)
    f2.write(text + '\n')
  else:
    f2.write(check)
  if len(check) == 0:
    break

f.close()
f2.close()
