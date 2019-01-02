import json
import sys
import logging

logging.basicConfig(filename="status.log", level=logging.INFO)

def read():
    with open(sys.argv[1], 'r') as f:
        data=json.load(f)
        logging.info("Read done!")
    return data


def write(new_data,filename):
    with open(filename, 'w') as f:
        json.dump(new_data,f)

data=read()
data['features']=[k for k in data['features'] if k['properties']['STREET']=='JEFFERSON']
data['features']=sorted(data['features'],key=lambda x: x['properties']['LOT_NUM'])
print(data['features'])

write(data,'sorted.json')
logging.info("Write done!")