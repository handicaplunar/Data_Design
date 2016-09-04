from mycircle import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64),index=True,unique=True)
	email = db.Column(db.String(120), index=True,unique=True)
	library = db.relationship('Library',backref='owner',lazy='dynamic')

	@property
	def is_authenticated(self):
		return False

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id)  # python 2
		except NameError:
			return str(self.id)  #python 3
	

	def __repr__(self):
		return '<User %r>' % (self.nickname)

class Library(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Library %r>' % (self.body)
