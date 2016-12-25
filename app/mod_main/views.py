import os
from flask import Flask, Blueprint, render_template, request, redirect, url_for, send_from_directory
from bson import json_util, ObjectId
from app import mongo
from werkzeug.utils import secure_filename


mod_main = Blueprint('main', __name__)

UPLOAD_FOLDER = '/home/arent/Desktop/dev/techstitution/app/static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@mod_main.route('/', methods=['GET','POST'])
def index():
    ''' Renders the App index page.
    :return:
    '''
    db = mongo.db.arkep
    
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        
        #metoda per me i ruajt file-at edhe njekohesisht validim
        # check if the post request has the file part
        if 'cer_biznesit' and 'cert_fiskal' and 'info_biz' not in request.files:
            #flash('No file part')
            return 'Bad request'
        file = request.files['cer_biznesit']
        file1 = request.files['cert_fiskal']
        file2 = request.files['info_biz']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '' and file1.filename == '' and file2.filename == '':
            #flash('No selected file')
            return 'Bad request'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
        if file1 and allowed_file(file1.filename):
            filename = secure_filename(file1.filename)
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
        if file2 and allowed_file(file2.filename):
            filename = secure_filename(file2.filename)
            file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            
            
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

#shfaqe file-in,  psh. http://0.0.0.0:5000/uploads/imazhi.png, po duhet vet me ia shtu /imazhi.png, perndryshe nuk e gjen emrin(se nuk po ruhet ne databaze) dhe po mbet url  http://0.0.0.0:5000/uploads/ .
#To do --- Permes nje linku(icone) ne doc.html duhet me e shfaq dokumentin.
@mod_main.route('/uploads/<filename>')
def uploaded_file(filename):
    filename = secure_filename(filename)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER