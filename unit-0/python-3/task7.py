import re 
pattern = re.compile('[А-Я][а-я]*\W')
type(pattern) == re.Pattern

def parseCsvLine(line):
    items = []
    state = "init"
    buff = ''
    for c in line:
        if state=='init':
            if c=='"':
                state = "value"
            else:
                pass
        elif state=='value':
            if c=='"':
                state='quote'
            else:
                buff += c
        elif state=='quote':
            if c=='"':
                buff += '"'
                state = 'value'
            else:
                items.append(buff)
                buff = ''
                if c==',':
                    state = 'init'
                else:
                    state = 'awaitDelim'
        elif state=='awaitDelim':
            if c==',':
                state = 'init'
            else:
                pass
    return items

class atdict(dict):
    __getattr__= dict.__getitem__
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__

def readCsv(filename,mapcol={},limit=-1):
    f = open(filename)    
    i = -1
    data = []
    def decode(mapping):
        if type(mapping)==str:
            return (mapping, lambda x: x)
        if type(mapping)==dict:
            key = mapping['key']
            parse = lambda x: x
            if 'type' in mapping:
                if mapping['type']==str:
                    parse = lambda x: x
                elif mapping['type']==int:
                    parse = lambda s: int(s)
                elif mapping['type']==float:
                    parse = lambda s: float(s)
            return (key, parse)
        raise "can't decode"

    mapping = {}
    for line in f:
        i+=1
        if i==0:
            headers = parseCsvLine(line)
            for hi, header in enumerate(headers):
                key = "c"+str(hi)
                parse = lambda s: s               
                for mk, mv in mapcol.items():
                    if type(mk)==re.Pattern:
                        if mk.search(header):
                            dec = decode(mv)
                            key = dec[0]
                            parse = dec[1]
                    if type(mk)==str:
                        if mk==header:
                            dec = decode(mv)
                            key = dec[0]
                            parse = dec[1]
                if not(hi in mapcol):
                    mapping[hi] = [key, parse]
                else:
                    dec = decode(mv)
                    key = dec[0]
                    parse = dec[1]
                    mapping[hi] = [key, parse]
        if i>0:
            items = parseCsvLine(line)
            rec = atdict()
            for idx, itm in enumerate(items):
                if idx in mapping:
                    rec[mapping[idx][0]] = mapping[idx][1](itm)
            data.append(rec)
        if i>limit and limit>0:
            break
    f.close()
    return data

data = readCsv(
    'StudentsPerformance.csv'
    , mapcol={
        'gender' : 'sex',
        'race/ethnicity' : 'race',
        'parental level of education' : 'parents',
        'lunch' : 'lunch',
        'test preparation course' : 'prep',
        'math score' : {
            'key' : 'mscore',
            'type' : int
        },
        'reading score' : {
            'key' : 'rscore',
            'type' : int
        },
        'writing score' : {
            'key' : 'wscore',
            'type' : int
        }
    }
    #, limit=10
)

###################################################
#len(data)
len([ x for x in data if x.parents == "bachelor's degree" ])
len(set([ x.parents for x in data ]))


len([ x for x in data if x.lunch=='standard' ]) / len(data)

len([ x for x in data if x.race=='group C' ])
len(set([ x.race for x in data ]))

########################
rscoreAvg = sum([x.rscore for x in data])/len(data)
len([x for x in data if x.rscore < rscoreAvg])

set([x.sex for x in data])
femaleData = [x for x in data if x.sex == 'female']

sum([x.rscore for x in femaleData])/len(femaleData)
studWScoreMore90 = [x for x in data if x.wscore > 90]
len([x for x in studWScoreMore90 if x.lunch=='standard'])/len(studWScoreMore90)

################
maleData = [x for x in data if x.sex == 'male']
len([x for x in maleData if x.lunch == 'standard' ])
len([x for x in maleData if x.prep == 'completed' ])
len([x for x in femaleData if x.parents == "master's degree" ])
set([x.race for x in data ])
len([x for x in data if x.race == 'group C' and x.prep == 'completed'])

len([x for x in femaleData if x.parents == "master's degree" and x.mscore > 90 ])
#################
string = 'abcdef'
string[::-1]

'Hello' in 'Hello, Dolly!'.lower() 
'ARE'.lower() in 'how are you?'.upper() 
'your' in 'WhAt Is YoUr NaMe?'.lower() 
'apples'.upper() in 'I like APPLES'.upper() 


X ='55,66'
float(X.replace(',', '.')) 
float(X.replace(',', '.'))

import re
ptrn = re.compile('\W\d*\w+\s!')
ptrn.search('=13x !')

import re
pattern = re.compile('\d\d\d')
secret = pattern.findall('2 x 2 = 4') 

#####################

mscoreMax = max([ x.mscore for x  in data ])
mscoreMaxData = [ x for x  in data if x.mscore == mscoreMax ]
sum([ x.rscore for x in mscoreMaxData ])/len(mscoreMaxData)

lunchBad = [x for x in data if x.lunch in ['free/reduced']]
sum([ x.wscore for x in lunchBad ])/len(lunchBad)