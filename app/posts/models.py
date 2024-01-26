from app.databese import BaseModel
from app.extensions import db
from sqlalchemy import Column, String, Text, Integer, ForeignKey

class Post(BaseModel):
    __tabename__ = 'post'

    title = Column(String(30), nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
	    return f'{self.__class__.__name__}({self.id}, {self.title[:30]}, {self.created_at})'

