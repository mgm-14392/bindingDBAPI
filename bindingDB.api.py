import requests
import pandas as pd
import numpy as np

listtIDs= ['O00255','P00734','P07900','P14555','P27487','P35367','P48039','Q02083','Q6V1X1','Q9H2K2',
           'O00329','P00742','P08172','P14780','P28222','P35462','P48147','Q05586','Q86X55','Q9H3R0',
           'O00763','P00749','P08173','P14867','P28223','P35557','P48449','Q07075','Q8IXJ6','Q9NUW8',
           'O14649','P00750','P08183','P15144','P28335','P35790','P48736','Q07343','Q8N1Q1','Q9NYA1',
           'O43497','P00813','P08235','P16083','P28472','P36544','P49286','Q07817','Q8N5Z0','Q9UBN7',
           'O43570','P00915','P08246','P19793','P28845','P37268','P49354','Q08499','Q8NEB9','Q9UDY8',
           'O60341','P00918','P08311','P21397','P29274','P39086','P49759','Q09472','Q8TDU6','Q9UGN5',
           'O60678','P02753','P08473','P21554','P29475','P41143','P50579','Q13126','Q8WUI4','Q9UHL4',
           'O60885','P02766','P08912','P21964','P30305','P41145','P51681','Q13133','Q92731','Q9ULX7',
           'O60911','P03952','P09237','P22303','P30542','P41146','P53582','Q13224','Q92831','Q9Y233',
           'O75164','P03956','P09874','P22748','P30968','P41594','P53634','Q13490','Q93009',
           'O75460','P04150','P09917','P22894','P31213','P41595','P55055','Q13627','Q96EB6',
           'O75762','P05164','P09960','P23141','P31645','P41597','P55085','Q13946','Q96JM7',
           'O76074','P06276','P10275','P25103','P32297','P42336','P56524','Q15125','Q96LA8',
           'O76083','P06401','P10415','P25105','P33316','P43166','P56817','Q15661','P20231','Q96RI1',
           'O95271','P07384','P11086','P25774','P34913','P43235','P61073','Q16790','Q99720',
           'P00374','P07477','P11229','P25929','P34972','P43681','P78536','Q16853','Q9BY41',
           'P00491','P07550','P14416','P27338','P35228','P45452','P98170','Q6P179','Q9GZT9','Q9GZT9',
           'Q6P179',
           'P98170','Q15661,P20231','Q15661']

ddict = {}
for a, b in zip(*[iter(llliii)]*2):
    string = ','.join((a, b))
    print(string)
    url = 'http://www.bindingdb.org/axis2/services/BDBService/getLigandsByUniprots?uniprot={}&cutoff=1000&code=0&response=application/json'.format(string)
    r = requests.get(url)
    TEXT = r.json()

    length = len(TEXT['getLigandsByUniprotsResponse']['affinities'])

    for i in range(0,length):
        query = TEXT['getLigandsByUniprotsResponse']['affinities'][i]['query']
        smiles = TEXT['getLigandsByUniprotsResponse']['affinities'][i]['smile']
        affinityType = TEXT['getLigandsByUniprotsResponse']['affinities'][i]['affinity_type']
        affinityValue = TEXT['getLigandsByUniprotsResponse']['affinities'][i]['affinity']

        if query in ddict:
            ddict[query]['smiles'].append(smiles)
            ddict[query]['affinityType'].append(affinityType)
            ddict[query]['affinityValue'].append(affinityValue)

        else:
            ddict[query] ={}
            ddict[query]['smiles'] = []
            ddict[query]['smiles'].append(smiles)

            ddict[query]['affinityType'] = []
            ddict[query]['affinityType'].append(affinityType)

            ddict[query]['affinityValue'] = []
            ddict[query]['affinityValue'].append(affinityValue)


out = pd.concat((pd.DataFrame(data) for data in ddict.values()),
                keys=ddict.keys(), names = ["ID", ""], sort=False)
out.reset_index(level=0, inplace=True)
out.reset_index(drop=True, inplace=True)
print(len(out))
out.to_csv('/Users/marianagonzmed/Desktop/milig2dock2.csv')