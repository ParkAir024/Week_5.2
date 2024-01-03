from app import db

class UsersModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(75), nullable=False, unique=True)

    def __repr__(self):
        return f'<User: {self.username}>'

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, user_dict):
        for k, v in user_dict.items():
            setattr(self, k, v)