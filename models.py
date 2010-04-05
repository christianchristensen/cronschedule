from google.appengine.ext import db

class CronObject(db.Model):
  url = db.StringProperty(required=True)
  type = db.StringProperty(choices=set(["cat", "dog", "bird"]))
  data = db.BlobProperty()
  created = db.DateTimeProperty(auto_now_add=True)
  updated = db.DateTimeProperty()
  owner = db.UserProperty(required=True)

# class Bar(db.Model):
#   barfoo = db.StringProperty
#   barbar = db.IntegerProperty