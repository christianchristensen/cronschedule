from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

import controller

from models import *

class MainPage(controller.BaseController):
	def get(self):
 		t_args = { 
			'page_title': 'Untitled',
			'page_content': 'Hello, World!'
 		}

		self.render_template('index.html', t_args) 

# Initialization Code
application = webapp.WSGIApplication([ 
  ('/', MainPage),
  ('/managecron', MainPage),
  ('/tasks/croncallback', MainPage),
	],debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
  main()