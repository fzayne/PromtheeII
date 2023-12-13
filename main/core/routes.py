import os
from main import app
from flask import render_template,request,session,redirect
import numpy as np
from core.csv import read_csv
from core.readJson import readJson
from core.promtheeII import calculPromtheeII


@app.route('/')
def index():
    return render_template("pages/initiateur.html")
@app.route('/showMatrix',methods=['POST'])
def showMatrix():
    
    print(request.form)
    print(request.files)
    if 'file' in request.files:
        
        file=request.files['file']

        matrix_data,title=read_csv(file)
        session["performanceMatrix"]=matrix_data

        return render_template("pages/initiateur.html",matrix=matrix_data,categories=title)
    # else:
    #     return "new"

    
@app.route("/sendMatrix",methods=['POST'])
def sendMat():
    matrix=request.json
    print(request.form.getlist("inputCell"))
    matrix=np.array(matrix,dtype=float)
    session['performanceMatrix']=matrix
    return redirect(render_template('pages/decideur.html'))

@app.route("/decideur",methods=['POST','GET'])
def decideur():
    if request.method=='GET':
        return render_template("pages/decideur.html")
    elif request.method=='POST':
        
        if 'Decideur 1' in request.form:
            decideur_name = 'Decideur 1'
        elif 'Decideur 2' in request.form:
            decideur_name = 'Decideur 2'
        elif 'Decideur 3' in request.form:
            decideur_name = 'Decideur 3'
        elif 'Decideur 4' in request.form:
            decideur_name = 'Decideur 4' 
        else:
            decideur_name=session['decideur']
        
        session['decideur']=decideur_name

        matrix,categories=readJson(decideur_name)
        rank=[]
        if "calculer" in request.form:
            weights=[row[0] for row in matrix]
            
            perfMatrix=session['performanceMatrix']
            
            rank=calculPromtheeII(weights,perfMatrix)[0]
        return render_template("pages/promthee.html",decideur=decideur_name,matrix=matrix,categories=categories,rank=rank)