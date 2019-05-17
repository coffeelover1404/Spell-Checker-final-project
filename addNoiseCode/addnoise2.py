import os
import re
import random
i=1
j=0
noiseFinal = ''

def replacechar(line):
    noise = line
    if(re.search('ก',line)):
        noise = re.sub(r"ก", "แ", line)
    elif(re.search('ฎ',line)):
        noise = re.sub(r"ฎ", "ฏ", line)
    elif(re.search('ไ',line)):
        noise = re.sub(r"ไ", "ๆ", line)
    elif(re.search('ใ',line)):
        noise = re.sub(r"ใ", "ม", line)
    elif(re.search('็',line)):
        noise = re.sub(r"็", "เ", line)
    elif(re.search('ว',line)):
        noise = re.sub(r"ว", "ง", line)
    elif(re.search('้',line)):
        noise = re.sub(r"้", "ื", line)
    elif(re.search('เ',line)):
        noise = re.sub(r"เ", "ด", line)
    elif(re.search('ุ',line)):
        noise = re.sub(r"ุ", "ะ", line)
    elif(re.search('ง',line)):
        noise = re.sub(r"ง", "บ", line)
    elif(re.search('น',line)):
        noise = re.sub(r"น", "ย", line)
    elif(re.search('า',line)):
        noise = re.sub(r"า", "ส", line)
    elif(re.search('ต',line)):
        noise = re.sub(r"ต", "จ", line)
    elif(re.search('ด',line)):
        noise = re.sub(r"ด", "แ", line)
    elif(re.search('ณ',line)):
        noise = re.sub(r"ณ", "ษ", line)
    elif(re.search('บ',line)):
        noise = re.sub(r"บ", "ข", line)
    elif(re.search('ย',line)):
        noise = re.sub(r"ย", "บ", line)
    elif(re.search('ม',line)):
        noise = re.sub(r"ม", "ใ", line)
    elif(re.search('ล',line)):
        noise = re.sub(r"ล", "ฃ", line)
    elif(re.search('ร',line)):
        noise = re.sub(r"ร", "ี", line)
    elif(re.search('พ',line)):
        noise = re.sub(r"พ", "ภ", line)
    elif(re.search('ข',line)):
        noise = re.sub(r"ข", "ช", line)
    elif(re.search('จ',line)):
        noise = re.sub(r"จ", "ย", line)
    elif(re.search('ป',line)):
        noise = re.sub(r"ป", "ผ", line)
    elif(re.search('อ',line)):
        noise = re.sub(r"อ", "ิ", line)
    else:
        noise = insert(noise)
    return noise

def insert(line):
    noise = list(line)
    pos = -1
    if(re.search('ก',line)):
        pos = re.search('ก',line)
        char = 'ห'
    elif(re.search('ๆ',line)):
        pos = re.search('ๆ',line)
        char = 'ไ'
    elif(re.search('ณ',line)):
        pos = re.search('ณ',line)
        char = 'ย'
    elif(re.search('ธ',line)):
        pos = re.search('ธ',line)
        char = 'พ'
    elif(re.search('ฯ',line)):
        pos = re.search('ฯ',line)
        char = 'น'
    elif(re.search('ไ',line)):
        pos = re.search('ไ',line)
        char = 'ำ'
    elif(re.search('ใ',line)):
        pos = re.search('ใ',line)
        char = 'ม'
    elif(re.search('ว',line)):
        pos = re.search('ว',line)
        char = 'บ'
    elif(re.search('เ',line)):
        pos = re.search('เ',line)
        char = 'ด'
    elif(re.search('ง',line)):
        pos = re.search('ง',line)
        char = 'ว'
    elif(re.search('น',line)):
        pos = re.search('น',line)
        char = 'จ'
    elif(re.search('า',line)):
        pos = re.search('า',line)
        char = 'ี'
    elif(re.search('ต',line)):
        pos = re.search('ต',line)
        char = 'ร'
    elif(re.search('ด',line)):
        pos = re.search('ด',line)
        char = 'แ'
    elif(re.search('บ',line)):
        pos = re.search('บ',line)
        char = 'ล'
    elif(re.search('ย',line)):
        pos = re.search('ย',line)
        char = 'บ'
    elif(re.search('ม',line)):
        pos = re.search('ม',line)
        char= 'ท'
    elif(re.search('ล',line)):
        pos = re.search('ล',line)
        char = 'บ'
    elif(re.search('ร',line)):
        pos = re.search('ร',line)
        char = 'ี'
    elif(re.search('พ',line)):
        pos = re.search('พ',line)
        char= 'ะ'
    elif(re.search('ข',line)):
        pos = re.search('ข',line)
        char = 'ช'
    elif(re.search('จ',line)):
        pos = re.search('จ',line)
        char = 'น'
    elif(re.search('ป',line)):
        pos = re.search('ป',line)
        char  = 'ห'
    elif(re.search('อ',line)):
        pos = re.search('อ',line)
        char = 'แ'
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

def swap(line):
    noise = list(line)
    length = len(line)
    if(length-2 <= 2):
        noise = replacechar(line)
    else:
        ran = random.randint(1,len(line)-2)
        temp = noise[ran-1]
        noise[ran-1] = noise[ran]
        noise[ran] = temp
        noise = ''.join(noise)
    return noise

def deletechar(line):
    noise = list(line)
    ran = random.randint(1,len(line)-1)
    noise[ran-1] = ''
    noise = ''.join(noise)
    return noise

with open('addnoise2.txt', 'w', encoding="utf-8") as output_file:
    with open('data.txt', encoding="utf-8") as f:
                for line in f:
                    j+=1
                    if(re.search([ก-ฮ])):
                        if(j >= 4500001):
                            if(len(line) == 2):
                                noiseFinal = ''+insert(line)
                            else:
                                noiseFinal = ''
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
                        if(j == 6000000):
                            break