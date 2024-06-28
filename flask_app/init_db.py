from company_blog import db
from company_blog.models import User
#db作成
#新たにテーブル作成の際にはdb.drop_all()

#db.drop_all()
db.create_all()

user1 = User(email="toshiki.ito3@persol.co.jp", username="Ito Toshiki", password="123", administrator="1")
db.session.add(user1)
db.session.commit()