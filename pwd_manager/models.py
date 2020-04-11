from pwd_manager.extensions import db
from datetime import date


class user_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    logo = db.Column(db.String(100))
    website_app_name = db.Column(db.String(50))
    user_name = db.Column(db.String(20))
    login_pwd = db.Column(db.String(20))
    created_at = db.Column(db.Date, default=date.today)

    @property
    def serialized(self):
        return {
            'id': self.id,
            'title': self.title,
            'webLoginName': self.website_app_name,
            'logo_url': self.logo,
            'loginID': self.user_name,
            'loginPwd': self.login_pwd,
            'createdDate': self.__parseDate(self.created_at)
        }

    def __parseDate(self,data):
        return data.strftime('%a, %d-%b-%Y')


