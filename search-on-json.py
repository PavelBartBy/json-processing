import json


def read(filename):
    with open(filename) as f:
        data=json.load(f)
        print("Read done!")
    return data


def write(new_data,filename):
    with open(filename, 'w') as f:
        json.dump(new_data,f)

file=r'C:\Users\BART\json-processing\citylots.json'
data=read(file)
data['features']=[k for k in data['features'] if k['properties']['STREET']=='JEFFERSON']
data['features']=sorted(data['features'],key=lambda x: x['properties']['LOT_NUM'])
print(data['features'])

write(data,'sorted.json')