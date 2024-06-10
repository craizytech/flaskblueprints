from flask import render_template

from home import bp


@bp.before_app_request
def before_request():
    print("Before Request")
    
@bp.after_app_request
def after_request(response):
    print("After Request")
    return response



@bp.route('/')
def home():
    return render_template('index.html')
