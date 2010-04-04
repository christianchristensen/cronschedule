import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class BaseController(webapp.RequestHandler):
	def render_template(self, view, values):
		self.response.out.write(template.render(self.path_for_template(view), values))

	def path_for_template( self, view):
		path = os.path.join(os.path.dirname(__file__), 'views/' + view)
		return(path)

	def param(self, param):
		return cgi.escape(self.request.get(param))