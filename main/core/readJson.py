import json
def readJson(decideur_name):
    if decideur_name=="Decideur 1":
        path="/home/fzayne/Documents/M2/DCTW/tp/PromtheeServer/main/config/data/decideur1.json"
    elif decideur_name=="Decideur 2":
        path="/home/fzayne/Documents/M2/DCTW/tp/PromtheeServer/main/config/data/decideur2.json"
    elif decideur_name=="Decideur 3":
        path="/home/fzayne/Documents/M2/DCTW/tp/PromtheeServer/main/config/data/decideur3.json"
    elif decideur_name=="Decideur 4":
        path="/home/fzayne/Documents/M2/DCTW/tp/PromtheeServer/main/config/data/decideur4.json"
    file=open(path)
    data = json.loads(file.read())
    categories = data.get("categories", [])

    # Creating a matrix
    matrix = []
    title=[]
    for category in categories:
        title.append(category['category'])
        matrix.append([
            category['weight'],
            category['tolerance'],
            category['low'],
            category['high']
        ])
    return (matrix,title)