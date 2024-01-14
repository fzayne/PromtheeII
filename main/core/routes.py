import os
from main import app
from flask import render_template,request,session,redirect,url_for
import numpy as np
from core.csv import read_csv
from core.readJson import readJson
from core.promtheeII import calculPromtheeII
from core.models.initiateur import Initiateur
from core.models.decideur import Decideur

initiateur = Initiateur()
decideur1= Decideur('Decideur 1',6)
decideur2= Decideur("Decideur 2",4)
decideur3= Decideur("Decideur 3",5)
decideur4= Decideur("Decideur 4",5)

@app.route('/',methods=['GET','POST'])
def index():
    
    # return render_template("pages/initiateur.html")
    if request.method=='POST':
        initiateur.calculateScorage([decideur1,decideur2,decideur3,decideur4])
    return render_template("pages/initiateur.html",matrix=initiateur.performanceMatrix,categories=initiateur.critere,score=initiateur.score)
@app.route('/showMatrix',methods=['POST'])
def showMatrix():
    
    print(request.form)
    print(request.files)
    if 'Decideur 1' in request.form:
        decideur=decideur1
    elif 'Decideur 2' in request.form:
        decideur=decideur2
    elif 'Decideur 3' in request.form:
        decideur=decideur3
    elif 'Decideur 4' in request.form:
        decideur=decideur4 
    else:
        
        if 'file' in request.files:

            file=request.files['file'] 

            matrix_data,title=read_csv(file)
            # session["performanceMatrix"]=matrix_data
            initiateur.performanceMatrix=matrix_data
            initiateur.critere=title
            actions=[row[0] for row in initiateur.performanceMatrix]
            initiateur.actions=actions
            decideur1.action=actions
            decideur2.action=actions
            decideur3.action=actions
            decideur4.action=actions
            # return render_template("pages/initiateur.html",matrix=initiateur.performanceMatrix,categories=initiateur.critere)
            return redirect("/")   
    session["decideur"]=decideur.name
    # return redirect(url_for("decideur",dcname= decideur.name)) 
    return redirect("/decideur")
    # else:
    #     return "new"

    
# @app.route("/sendMatrix",methods=['POST'])
# def sendMat():
#     matrix=request.json
#     print(request.form.getlist("inputCell"))
#     matrix=np.array(matrix,dtype=float)
#     session['performanceMatrix']=matrix
#     return redirect(render_template('pages/decideur.html'))

@app.route("/decideur",methods=['POST','GET'])
def decideur():
    
    dcname=session["decideur"]
    if dcname==decideur1.name:
        decideur=decideur1
    if dcname==decideur2.name:
        decideur=decideur2
    if dcname==decideur3.name:
        decideur=decideur3
    if dcname==decideur4.name:
        decideur=decideur4
    # if request.method=='GET':
    #     # return render_template("pages/decideur.html")
    if request.method=='POST':
        
        # if 'Decideur 1' in request.form:
        #     decideur=decideur1
        # elif 'Decideur 2' in request.form:
        #     decideur=decideur2
        # elif 'Decideur 3' in request.form:
        #     decideur=decideur3
        # elif 'Decideur 4' in request.form:
        #     decideur=decideur4 
        # else:
        #      decideur=session['decideur']
        
        # session['decideur']=decideur

        # matrix,categories=readJson(decideur_name)
        # rank=[]
        
        if "calculer" in request.form:
            # weights=[row[0] for row in matrix]
            # perfMatrix=session['performanceMatrix']
            
            # rank=calculPromtheeII(weights,perfMatrix)
            # perfMatrix=np.array(perfMatrix,dtype=float)
            print(initiateur.performanceMatrix)
            decideur.calculatePromethee(initiateur.performanceMatrix)
            actions=[row[0] for row in initiateur.performanceMatrix]
            # print(actions)
    return render_template("pages/promthee.html",decideur=decideur.name,matrix=decideur.subjectiveParametre,categories=decideur.categories,rank=decideur.rank,index=decideur.action)