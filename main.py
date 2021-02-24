from flask import Flask,request, jsonify
import pandas as pd
import pdb

app=Flask(__name__)

@app.route("/")
def index():
    return "Welcome"

@app.route("/<id>/",methods=["GET"])
def get_details(id):
    list_data=()
    payload=request.data
    string_data=""
    col_names = ["col1"]
    df=pd.read_csv("bugreport-bhima_in-RKQ1.200826.002-2021-02-22-20-31-22.txt", names=col_names)
    # df['col1']=df['col1'].apply(lambda x:str(x))
    # pdb.set_trace()
    result = [x for x in df["col1"] if id in str(x)]

    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)