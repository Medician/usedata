__author__ = 'manya'
from app import app
from flask import request, render_template
import repository as repo




@app.route('/')
def index_route():
    return render_template('welcome_b.html')


@app.route('/customer', methods=['POST'])
def user_post_route():

    email = request.form.get('email')
    phone = request.form.get('phone')
    address = request.form.get('address')

    repo.create_cust(email, phone, address)



@app.route('/customer/<email>', methods=['GET'])
def all_users_get_route(email):
    # = request.form.get('email')
   	repo.get_cust(email)
   	


