from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/bank_app'
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET', 'POST'])
def user_list():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if name and email:
            mongo.db.users.insert_one({'name': name, 'email': email})
            return redirect(url_for('user_list'))
    users = mongo.db.users.find()
    return render_template('user_list.html', users=users)

@app.route('/delete/<string:id>')
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('user_list'))

if __name__ == '__main__':
    app.run(debug=True)
