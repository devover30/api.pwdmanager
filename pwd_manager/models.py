from datetime import date
from pwd_manager.extensions import db


class user_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website_app_name = db.Column(db.String(50))
    user_name = db.Column(db.String(20))
    login_pwd = db.Column(db.String(20))
    created_at = db.Column(db.Date, default=date.today)

    @property
    def serialized(self):
        return {
            'id': self.id,
            'website_name': self.website_app_name,
            'login_id': self.user_name,
            'login_pwd': self.login_pwd,
            'created_date': self.created_at
        }

