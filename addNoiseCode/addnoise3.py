import os
import re
import random
i=1
j=0
noiseFinal = ''

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

def replacechar(line):
    noise = line
    if(re.search('ก',line)):
        noise = re.sub(r"ก", "ำ", line)
    elif(re.search('ฏ',line)):
        noise = re.sub(r"ฏ", "ฎ", line)
    elif(re.search('ไ',line)):
        noise = re.sub(r"ไ", "/", line)
    elif(re.search('ใ',line)):
        noise = re.sub(r"ใ", "ว", line)
    elif(re.search('็',line)):
        noise = re.sub(r"็", "ํ", line)
    elif(re.search('ว',line)):
        noise = re.sub(r"ว", "ย", line)
    elif(re.search('้',line)):
        noise = re.sub(r"้", "๋", line)
    elif(re.search('เ',line)):
        noise = re.sub(r"เ", "้", line)
    elif(re.search('ุ',line)):
        noise = re.sub(r"ุ", "ถ", line)
    elif(re.search('ง',line)):
        noise = re.sub(r"ง", "ย", line)
    elif(re.search('น',line)):
        noise = re.sub(r"น", "ฯ", line)
    elif(re.search('า',line)):
        noise = re.sub(r"า", "ษ", line)
    elif(re.search('ต',line)):
        noise = re.sub(r"ต", "ค", line)
    elif(re.search('ด',line)):
        noise = re.sub(r"ด", "พ", line)
    elif(re.search('ณ',line)):
        noise = re.sub(r"ณ", "น", line)
    elif(re.search('บ',line)):
        noise = re.sub(r"บ", "ช", line)
    elif(re.search('ย',line)):
        noise = re.sub(r"ย", "ว", line)
    elif(re.search('ม',line)):
        noise = re.sub(r"ม", "า", line)
    elif(re.search('ล',line)):
        noise = re.sub(r"ล", "ง", line)
    elif(re.search('ร',line)):
        noise = re.sub(r"ร", "ณ", line)
    elif(re.search('พ',line)):
        noise = re.sub(r"พ", "ำ", line)
    elif(re.search('ข',line)):
        noise = re.sub(r"ข", "บ", line)
    elif(re.search('จ',line)):
        noise = re.sub(r"จ", "ข", line)
    elif(re.search('ป',line)):
        noise = re.sub(r"ป", "ผ", line)
    elif(re.search('อ',line)):
        noise = re.sub(r"อ", "ด", line)
    else:
        noise = insert(noise)
    return noise

def insert(line):
    noise = list(line)
    pos = -1
    if(re.search('ก',line)):
        pos = re.search('ก',line)
        char = 'ด'
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
        char = 'ๆ'
    elif(re.search('ใ',line)):
        pos = re.search('ใ',line)
        char = 'ว'
    elif(re.search('ว',line)):
        pos = re.search('ว',line)
        char = 'ซ'
    elif(re.search('เ',line)):
        pos = re.search('เ',line)
        char = 'ะ'
    elif(re.search('ง',line)):
        pos = re.search('ง',line)
        char = 'ล'
    elif(re.search('น',line)):
        pos = re.search('น',line)
        char = 'ฯ'
    elif(re.search('า',line)):
        pos = re.search('า',line)
        char = 'ท'
    elif(re.search('ต',line)):
        pos = re.search('ต',line)
        char = 'น'
    elif(re.search('ด',line)):
        pos = re.search('ด',line)
        char = 'พ'
    elif(re.search('บ',line)):
        pos = re.search('บ',line)
        char = 'ข'
    elif(re.search('ย',line)):
        pos = re.search('ย',line)
        char = 'จ'
    elif(re.search('ม',line)):
        pos = re.search('ม',line)
        char= 'า'
    elif(re.search('ล',line)):
        pos = re.search('ล',line)
        char = 'ฃ'
    elif(re.search('ร',line)):
        pos = re.search('ร',line)
        char = 'า'
    elif(re.search('พ',line)):
        pos = re.search('พ',line)
        char= 'โ'
    elif(re.search('ข',line)):
        pos = re.search('ข',line)
        char = 'จ'
    elif(re.search('จ',line)):
        pos = re.search('จ',line)
        char = 'ญ'
    elif(re.search('ป',line)):
        pos = re.search('ป',line)
        char  = 'ก'
    elif(re.search('อ',line)):
        pos = re.search('อ',line)
        char = 'ด'
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

with open('addnoise2.txt', 'w', encoding="utf-8") as output_file:
    with open('data.txt', encoding="utf-8") as f:
                for line in f:
                    j+=1
                    if(re.search([ก-ฮ])):
                        if(j >= 4500001):
                            if(len(line) == 2):
                                noiseFinal = 'i'+insert(line)
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
                            if(noiseFinal == '\n'):
                                print(j)
                            output_file.write(noiseFinal)
                            # print(j)
                            # print(noiseFinal)
                        if(j == 6000000):
                            break