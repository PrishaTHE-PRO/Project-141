import csv 
from flask import Flask,jsonify,request

with open('articles.csv') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_article=data[1:]
liked_article=[]
not_liked_article=[]

app=Flask(__name__)

@app.route('/get-article')
def get_article():
    return jsonify({
        'data':all_article[0],
        'status':'success'
    })

@app.route('/liked-article',methods=['POST'])
def liked_article():
    article=all_article[0]
    liked_article.append(article)
    all_article.pop(0)
    return jsonify({
        'status':'success'
    })

@app.route('/not-liked-article',methods=['POST'])
def not_liked_article():
    article=all_article[0]
    not_liked_article.append(article)
    all_article.pop(0)
    return jsonify({
        'status':'success'
    })

if __name__=='__main__':
    app.run()