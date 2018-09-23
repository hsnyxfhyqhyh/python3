import json

data = '{  \
    "president": { \
        "name": "Zaphod Beeblebrox",  \
        "species": "Betelgeusian"  \
    }  \
}'
o = json.loads(data)

print(o['president']['name'])
