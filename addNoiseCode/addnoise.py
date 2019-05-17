import os
import re
import random
i=1
j=0
noiseFinal = ''

def replacechar(line):
    noise = line
    if(re.search('ก',line)):
        noise = re.sub(r"ก", "ห", line)
    elif(re.search('ไ',line)):
        noise = re.sub(r"ไ", "ำ", line)
    elif(re.search('ใ',line)):
        noise = re.sub(r"ใ", "ไ", line)
    elif(re.search('็',line)):
        noise = re.sub(r"็", "้", line)
    elif(re.search('ว',line)):
        noise = re.sub(r"ว", "ส", line)
    elif(re.search('้',line)):
        noise = re.sub(r"้", "่", line)
    elif(re.search('เ',line)):
        noise = re.sub(r"เ", "ะ", line)
    elif(re.search('ุ',line)):
        noise = re.sub(r"ุ", "ั", line)
    elif(re.search('ง',line)):
        noise = re.sub(r"ง", "ว", line)
    elif(re.search('น',line)):
        noise = re.sub(r"น", "ร", line)
    elif(re.search('า',line)):
        noise = re.sub(r"า", "่", line)
    elif(re.search('ต',line)):
        noise = re.sub(r"ต", "น", line)
    elif(re.search('ด',line)):
        noise = re.sub(r"ด", "ก", line)
    elif(re.search('ณ',line)):
        noise = re.sub(r"ณ", "ร", line)
    elif(re.search('บ',line)):
        noise = re.sub(r"บ", "ล", line)
    elif(re.search('ย',line)):
        noise = re.sub(r"ย", "น", line)
    elif(re.search('ม',line)):
        noise = re.sub(r"ม", "ท", line)
    elif(re.search('ล',line)):
        noise = re.sub(r"ล", "ช", line)
    elif(re.search('ร',line)):
        noise = re.sub(r"ร", "น", line)
    elif(re.search('พ',line)):
        noise = re.sub(r"พ", "ะ", line)
    elif(re.search('ข',line)):
        noise = re.sub(r"ข", "จ", line)
    elif(re.search('จ',line)):
        noise = re.sub(r"จ", "ต", line)
    elif(re.search('ป',line)):
        noise = re.sub(r"ป", "แ", line)
    elif(re.search('อ',line)):
        noise = re.sub(r"อ", "แ", line)
    else:
        noise = insert(noise)
    return noise

def insert(line):
    noise = list(line)
    pos = -1
    if(re.search('ก',line)):
        pos = re.search('ก',line)
        char = 'แ'
    elif(re.search('ๆ',line)):
        pos = re.search('ๆ',line)
        char = 'ฟ'
    elif(re.search('ณ',line)):
        pos = re.search('ณ',line)
        char = 'ร'
    elif(re.search('ธ',line)):
        pos = re.search('ธ',line)
        char = 'ะ'
    elif(re.search('ฯ',line)):
        pos = re.search('ฯ',line)
        char = 'น'
    elif(re.search('ไ',line)):
        pos = re.search('ไ',line)
        char = 'ห'
    elif(re.search('ใ',line)):
        pos = re.search('ใ',line)
        char = 'ฝ'
    elif(re.search('ว',line)):
        pos = re.search('ว',line)
        char = 'ง'
    elif(re.search('เ',line)):
        pos = re.search('เ',line)
        char = '้'
    elif(re.search('ง',line)):
        pos = re.search('ง',line)
        char = 'บ'
    elif(re.search('น',line)):
        pos = re.search('น',line)
        char = 'ย'
    elif(re.search('า',line)):
        pos = re.search('า',line)
        char = 'ส'
    elif(re.search('ต',line)):
        pos = re.search('ต',line)
        char = 'จ'
    elif(re.search('ด',line)):
        pos = re.search('ด',line)
        char = 'เ'
    elif(re.search('บ',line)):
        pos = re.search('บ',line)
        char = 'ย'
    elif(re.search('ย',line)):
        pos = re.search('ย',line)
        char = 'น'
    elif(re.search('ม',line)):
        pos = re.search('ม',line)
        char= 'ใ'
    elif(re.search('ล',line)):
        pos = re.search('ล',line)
        char = 'ช'
    elif(re.search('ร',line)):
        pos = re.search('ร',line)
        char = 'ต'
    elif(re.search('พ',line)):
        pos = re.search('พ',line)
        char= 'ำ'
    elif(re.search('ข',line)):
        pos = re.search('ข',line)
        char = 'บ'
    elif(re.search('จ',line)):
        pos = re.search('จ',line)
        char = 'ข'
    elif(re.search('ป',line)):
        pos = re.search('ป',line)
        char  = 'แ'
    elif(re.search('อ',line)):
        pos = re.search('อ',line)
        char = 'ิ'
    else:
        char = ''
    if(char == ''):
        noise = deletechar(noise)
    else:
        # print('pos:',pos.start())
        # print('line:',len(line))
        if(int(pos.start()) == len(line)-2):
            noise = noise[:int(pos.start())] + list(char) + list('\n')
            noise = ''.join(noise)
        else:
            noise = noise[:int(pos.start())] + list(char) + noise[int(pos.start()):]
            noise = ''.join(noise)
    return noise

def deletechar(line):
    noise = list(line)
    ran = random.randint(1,len(line)-1)
    noise[ran-1] = ''
    noise = ''.join(noise)
    return noise

def swap(line):
    noise = list(line)
    length = len(line)
    if(length-2 <= 1):
        noise = insert(line)
    else:
        ran = random.randint(1,len(line)-2)
        temp = noise[ran-1]
        noise[ran-1] = noise[ran]
        noise[ran] = temp
        noise = ''.join(noise)
    return noise

with open('addnoise1.txt', 'w', encoding="utf-8") as output_file:
    with open('data.txt', encoding="utf-8") as f:
                for line in f:
                    j+=1
                    noiseFinal = ''
                    if(re.search([ก-ฮ])):
                        if(line == 'ๆ\n' or line == 'ฯ\n' or line == 'ณ\n'):
                            noiseFinal = ''+insert(line)
                        else:
                            if(i == 1):
                                noiseFinal = ''+replacechar(line)
                                i += 1
                            # if(re.search(r'^.{2}$',line)):
                            elif(i == 2):
                                noiseFinal = ''+deletechar(line)
                                i += 1
                            elif(i == 3):
                                noiseFinal = ''+swap(line)
                                i += 1
                            else:
                                noiseFinal = ''+insert(line)
                                i = 1
                        output_file.write(noiseFinal)
                        # print(j)
                        # print(noiseFinal)
                        if(j == 2000000):
                            break