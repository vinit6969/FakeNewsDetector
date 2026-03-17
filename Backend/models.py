from sqlalchemy import Column, Integer, String, Text
from database import Base

class Headline(Base):
    __tablename__ = "headlines"

    id = Column(Integer, primary_key=True, index=True)
    headline = Column(String(500))
    classification = Column(String(50))
    explanation = Column(Text)