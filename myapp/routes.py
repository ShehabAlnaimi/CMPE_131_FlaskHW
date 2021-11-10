from myapp import myapp_obj
from myapp.forms import TopCitiesForm
from flask import render_template, flash, redirect, request

from myapp import db
from myapp.models import  TopCities
#from flask_login import current_user, login_user, logout_user, login_required


@myapp_obj.route("/", methods = ['GET', 'POST'])
def home():

	title = 'Top Cities'
	name = 'Shehab'
	top_cities = TopCities.query.all()
	form = TopCitiesForm()
	if request.method == 'GET':
		return render_template ('home.html', form = form, name = name, title = title, top_cities = top_cities)
	if request.method == 'POST':
		if not request.form ['city_name'] or not request.form ['city_rank']:
			flash ('Enter city name  and city ranke')
		else:
			ct = TopCities (city_name = form.city_name.data, city_rank = form.city_rank.data)
			db.session.add(ct)
			db.session.commit()
			flash ('city added')
			return redirect ('/')
	return render_template('home.html', title=title, name=name, top_cities = top_cities, form = form)
