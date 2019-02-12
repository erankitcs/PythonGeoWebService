from flask import Flask,render_template,request,send_file
from get_geocode import getgeocode
from map_formation import create_addressmap
import pandas
from read_uploaded_csv import read_csvfile
import csv
import json
import numpy as np
app=Flask(__name__)

@app.route('/home/')
def home():

    return render_template("home.html")

@app.route("/index/" , methods=['POST'])
def proceed():
    uname=request.form["username"]
    return render_template("index.html",username=uname)
@app.route("/coordinate/",methods=['POST'])
def address():
    adr=request.form["address"]
    #lat=30
    #long=30
    gloc=getgeocode(adr)
    if gloc !=None :
        lat=gloc.latitude
        long=gloc.longitude
    else:
        lat=None
        long=None
    df_adr=pandas.DataFrame([{'Address':adr, 'Latitude':lat,'Longitude':long}])
    map_html=create_addressmap(df_adr)
    return render_template("result_search.html",lat=lat,long=long,adr=adr,map_html=map_html)

@app.route("/coordinates/",methods=['POST'])
def addresses():
    global file
    global newfilename
    if request.method=='POST':
        file=request.files["fileinput"]
        newfilename=str(np.random.randint(0,1000))+file.filename
        status, data , adrcol = read_csvfile(file)
        data.to_csv("Downloads/"+newfilename)
        df_adr=data.loc[:,['Latitude','Longitude',adrcol]]
        df_adr.rename(columns={adrcol: 'Address'}, inplace=True)
        #print(df_adr)
        map_html=create_addressmap(df_adr)
        return render_template("result_file.html",map_html=map_html,data=df_adr)

@app.route("/download")
def download():
     return send_file("Downloads/"+newfilename, attachment_filename="yourfile.csv", as_attachment=True)


@app.route("/storeUser",methods=['POST'])
def storeUser():
    uname=request.form["username"]
    myData = [[uname]]
    myFile = open('UserData/UserName.csv', 'a')
    with myFile:
         writer = csv.writer(myFile)
         writer.writerows(myData)
    return json.dumps({'status':'OK','user':uname})

if __name__=="__main__":
    app.run(debug=True)
