import json

data = {}
data['sprites'] = []
data['sprites'].append({
    'name': 'Tree1',
    'color': 'green',
    'shape':[10,0, 40,0, 30,10, 30,20, 40,35, 40,40, 30,45,
             20,45, 10,35, 10,25, 20,20, 20,10, 10,0]
    
})
data['sprites'].append({
    'name': 'Tree2',
    'color': 'green',
    'shape':[0,0, 0,0, 0,0, 0,0]
})
data['sprites'].append({
    'name': 'Tree3',
    'color': 'green',
    'shape':[0,0, 0,0, 0,0, 0,0]
})

with open('sprites.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
