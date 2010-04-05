from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
# from google.appengine.api import users

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
    cronObj = CronObject(url="http://minenet.org", type="cat", owner=users.get_current_user())
#    cronObj.put()
 		t_args = { 
			'page_title': 'Manage cron callbacks',
			'page_content': 'PUT HTML elem here...'
 		}
		self.render_template('managecron.html', t_args) 

# Initialization Code
application = webapp.WSGIApplication([ 
  ('/', MainPage),
  ('/managecron', ManageCronPage),
  ('/tasks/croncallback', MainPage),
	],debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
  main()