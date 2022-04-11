from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from speechrec import speechrec
from celery_utils import get_celery_app_instance
import time
from os import listdir
from os.path import isfile, join
from celery.result import AsyncResult

# EVENTUALLY HOOK UP TO DB!
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads/'
app.config['MAX_CONTENT_PATH'] = 160000

text_results = ["SPEECH!"]

celery = get_celery_app_instance(app)


@app.route("/")
def hello_world():
    print(text_results)
    return jsonify(text_results)

@app.route('/upload', methods= ['GET', 'POST'])
def upload_file():
   print("WORKING DIRECTORY:", os.getcwd())
   files = [f for f in listdir('./uploads/') if isfile(join('./uploads/', f))]
   return render_template('upload.html', uploadlist = str(files), speeches=str(text_results))
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save('./uploads/' + secure_filename(f.filename))
      #textres = speechrec(f.filename)
      print("FILE TO SEND:", f.filename)
      task = speech_rec_with_celery.delay('./uploads/' +  f.filename)
      return jsonify({"task_id": task.id}), 202
   return f"Long running task triggered with Celery! Check terminal to see the logs..."

@app.route("/tasks", methods=["GET"])
def get_status():
    i = celery.control.inspect()
    print("GETTING TASKS")
    print(i)
    '''task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return jsonify(result), 200'''
    return str(i)

# celery tasks
@celery.task(name='speech_rec')
def speech_rec_with_celery(filename):
    print("Executing Long running task : Sending email with celery...", filename)
    textres = speechrec(filename)
    #text_results.append(textres)
    print("Task complete!")
    return textres
		
if __name__ == '__main__':
   app.run(debug = True)