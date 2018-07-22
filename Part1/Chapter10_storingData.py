import json

familyInfo={
    "Ethan": {"height": 73, "middle name": "Thomas"},
    "Bailey": {"height": 63, "middle name": "Rose"},
    "Connor": {"height": 68, "middle name": "Patrick"}
    }

'''with open("family.json", 'w') as file:
    json.dump(familyInfo, file)'''
with open("family.json") as doc:
    for key, element in json.load(doc).items():
        print key+" "+str(element)
    