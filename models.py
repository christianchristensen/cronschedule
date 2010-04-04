from google.appengine.ext import db

class Foo(db.Model):
	foofoo = db.StringProperty
	foobar = db.IntegerProperty
	
class Bar(db.Model):
	barfoo = db.StringProperty
	barbar = db.IntegerProperty