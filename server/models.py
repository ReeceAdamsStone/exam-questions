from __future__ import annotations
from sqlalchemy import Integer, String, ForeignKey, Table, Column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app import db
from typing import List
    # from app import db  

    # db = SQLAlchemy()

class Questions(db.Model):
    __tablename__ = 'Questions'

    QiD: Mapped[int] = mapped_column(primary_key=True)
    Question_String: Mapped[str] = mapped_column()
    Supporting_Material: Mapped[str] = mapped_column()
    Topic_ID: Mapped[int] = mapped_column(ForeignKey('Topic.Topic_ID'))
    Component_ID: Mapped[int] = mapped_column(ForeignKey('Component_of_Paper.Component_of_Paper_ID'))
    Paper_ID: Mapped[int] = mapped_column(ForeignKey('PaperType.PaperType_ID'))

    #New Relationships
    papertype: Mapped["PaperType"] = relationship("PaperType", foreign_keys=[Paper_ID])
    topic: Mapped["Topic"] = relationship("Topic", foreign_keys=[Topic_ID])
    component: Mapped["Component_of_Paper"] = relationship("Component_of_Paper", foreign_keys=[Component_ID])


class PaperType(db.Model):
    __tablename__ = 'PaperType'

    PaperType_ID: Mapped[int] = mapped_column(primary_key=True)
    Paper_Name: Mapped[str] = mapped_column(unique=True)    
    
    # # BiDirectionalRelationships
    # questions: Mapped[List["Questions"]] = relationship(back_populates="papertype")
    

class Topic(db.Model):
    __tablename__ = 'Topic'

    Topic_ID: Mapped[int] = mapped_column(primary_key=True)
    Component_ID: Mapped[int] = mapped_column(ForeignKey('Questions.Component_ID'))
    Topic_Name: Mapped[str] = mapped_column(unique=True)
    Paper_ID: Mapped[int] = mapped_column(ForeignKey('Questions.Paper_ID'))

    # # BiDirectionalRelationships
    # questions: Mapped[List["Questions"]] = relationship(back_populates="topic")

class Component_of_Paper(db.Model):
    __tablename__ = 'Component_of_Paper'

    Component_of_Paper_ID: Mapped[int] = mapped_column(primary_key=True)
    Component_Name: Mapped[str] = mapped_column()
    Marks: Mapped[int] = mapped_column()
    PaperType_ID: Mapped[int] = mapped_column(ForeignKey('Questions.Paper_ID'))  
    
    # # BiDirectionalRelationships
    # questions: Mapped[List["Questions"]] = relationship(back_populates="component")

# class Paper_Name(db.Model):
#     __tablename__ = 'Paper_Name'

#     Paper_ID: Mapped[int] = Column(Integer, primary_key=True)
#     Paper_Name: Mapped[str] = Column(String, unique=True)

#     # Relationships
#     questions = relationship('Questions', back_populates='paper')

# class Assessment_Objectives(db.Model):
#     __tablename__ = 'Assessment_Objectives'

#     AO_ID: Mapped[int] = Column(Integer, primary_key=True)
#     AO_Int_Name: Mapped[str] = Column(String)

#     # Relationships
#     aOquestions = relationship('Questions', secondary='AOs_By_Paper', back_populates='objectives')

# class AOs_By_Paper(db.Model):
#     __tablename__ = 'AOs_By_Paper'

#     QID: Mapped[int] = Column(Integer, ForeignKey('Questions.QiD'), primary_key=True)
#     AO_ID: Mapped[int] = Column(Integer, ForeignKey('Assessment_Objectives.AO_ID'), primary_key=True)