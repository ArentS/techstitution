from flask import Blueprint, render_template, request, redirect, url_for
from bson import json_util, ObjectId
from app import mongo


mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET','POST'])
def index():
    ''' Renders the App index page.
    :return:
    '''
    db = mongo.db.arkep
    
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data = request.form.to_dict()
        db.insert(data)
        return render_template('success.html')
        #return json_util.dumps(data)
    else:
        return 'Bad request'

@mod_main.route('/<string:id>', methods=['GET'])
def get_doc(id):
    
    #Return a mongo document with the specified id.
    #return MongoDb Cursor
    
    db = mongo.db.arkep
    
    if request.method == 'GET':
    
        doc = db.find_one({"_id":ObjectId(id)})
        #doc_json = json_util.dumps(doc)
        #return render_template('doc.html' , doc = doc_json )
        return render_template('doc.html' , doc = doc )
        #return "<p>You requested a document with ID" + id +'<p>/n ' + json_util.dumps(doc)
    else:
        return 'Bad request'
    
@mod_main.route('/lista', methods=['GET'])
def lista():
    dokumentat = mongo.db.arkep.find()
    return render_template('lista.html', dokumentat = dokumentat)

@mod_main.route('/remove/<string:id>', methods=['GET'])
def remove_doc(id):
    
    #Return a mongo document with the specified id.
    #return MongoDb Cursor
    
    db = mongo.db.arkep
    
    if request.method == 'GET':
    
        
        doc =db.remove({"_id":ObjectId(id)})
        #doc_json = json_util.dumps(doc)
        #return render_template('doc.html' , doc = doc_json )
        return redirect(url_for('main.lista'))
        #return "<p>You requested a document with ID" + id +'<p>/n ' + json_util.dumps(doc)
    else:
        return 'Bad request'
    
@mod_main.route('/update/<string:id>', methods=['GET'])
def get_doc_to_update(id):
    
    #Return a mongo document with the specified id.
    #return MongoDb Cursor
    
    db = mongo.db.arkep
    
    if request.method == 'GET':
    
        doc = db.find_one({"_id":ObjectId(id)})
        #doc_json = json_util.dumps(doc)
        #return render_template('doc.html' , doc = doc_json )
        return render_template('update.html' , doc = doc )
        #return "<p>You requested a document with ID" + id +'<p>/n ' + json_util.dumps(doc)
    else:
        return 'Bad request'
    
    
@mod_main.route('/update', methods=["GET",'POST'])
def update_doc():
    
        db = mongo.db.arkep
        data = request.form.to_dict()
        id = data['_id']
        del data['_id']
        
        db.update(
           {'_id':ObjectId(id)},
          data,True
        )
        if (data):
            result = "Te dhenat u ruajtun me sukses"
            return redirect(url_for('main.lista'))

        else:
            result = "Gabim ne ruajten e te dhenave"
            return render_template('lista.html', result=result, json=json_util.dumps(data))