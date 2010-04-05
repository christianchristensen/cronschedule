from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import users

import urllib2

import controller

from models import *

class MainPage(controller.BaseController):
	def get(self):
 		t_args = { 
			'page_title': 'Untitled',
			'page_content': 'Hello, World!'
 		}

		self.render_template('index.html', t_args) 

class ManageCronPage(controller.BaseController):
	def get(self):
		meh = "meh: " + str(self.request) + "<br /><br />"
		if(str(self.request).find("/add") != -1):  
				pageoutput = "page add req"
		elif(str(self.request).find("/add") != -1):
				pageoutput = "delete req"
		else:
			query = db.GqlQuery("SELECT * FROM CronObject WHERE owner = :owner", owner=users.get_current_user())
			results = query.fetch(10) # use the auto-pager to deal with this...
			cronObjOutput = ""
			# This needs to be templated!
			# even moreso - django can scaffold the UI for this right?!?! bahhh - use the django framework for this!!
			for result in results:
				cronObjOutput = cronObjOutput + "<li><a href=\"managecron/id/"+str(result.key())+"\">" + result.url + "</a> - <a href=\"managecron/delete/"+str(result.key())+"\">delete</a></li>"
			pageoutput = cronObjOutput

		t_args = { 
			'page_title': 'Manage cron callbacks',
			'page_content': meh + pageoutput
 		}
		self.render_template('managecron.html', t_args)
	def post(self):
		cronObj = CronObject(url="http://minenet.org", owner=users.get_current_user())
		cronObj.put()
		self.redirect('/managecron')

class CronCallback(controller.BaseController):
	def get(self):
		query = db.GqlQuery("SELECT * FROM CronObject")
		results = query.fetch(100) # how to go over a set?
		cronObjOutput = ""
		for result in results:
		  try:
		    outputres = urllib2.urlopen(result.url)
		  except:
		    outputres = 'fail: ' + result.url
		  cronObjOutput = cronObjOutput + "<li>"+outputres+"</li>"
		t_args = { 
			'page_title': 'Cron Callback',
			'page_content': "<h1>Results</h1><br/>"+cronObjOutput
 		}
		self.render_template('index.html', t_args)


# Initialization Code
application = webapp.WSGIApplication([ 
  ('/', MainPage),
  ('/managecron', ManageCronPage),
  ('/managecron/add', ManageCronPage),
  ('/managecron/delete', ManageCronPage),
  ('/tasks/croncallback', CronCallback),
	],debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
  main()