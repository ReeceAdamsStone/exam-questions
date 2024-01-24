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

    QiD: Mapped[int] = Column(Integer, primary_key=True)
    Question_String: Mapped[str] = Column(String)
    Supporting_Material: Mapped[str] = Column(String)
    Topic_ID: Mapped[int] = Column(Integer, ForeignKey('Topics.Topic_ID'))
    Component_of_Paper_ID: Mapped[int] = Column(Integer, ForeignKey('Component_of_Paper.Component_of_Paper_ID'))
    Paper_ID: Mapped[int] = Column(Integer, ForeignKey('Paper_Name.Paper_ID'))

    # Relationships
    topic = relationship('Topics', back_populates='questions')
    component_of_paper = relationship('Component_of_Paper', back_populates='questions')
    paper = relationship('Paper_Name', back_populates='questions')
    objectives = relationship('Assessment_Objectives', secondary='AOs_By_Paper', back_populates='aOquestions')

class Topics(db.Model):
    __tablename__ = 'Topics'

    Topic_ID: Mapped[int] = Column(Integer, primary_key=True)
    Topic_Name: Mapped[str] = Column(String, unique=True)

    # Relationships
    questions = relationship('Questions', back_populates='topic')

class Component_of_Paper(db.Model):
    __tablename__ = 'Component_of_Paper'

    Component_of_Paper_ID: Mapped[int] = Column(Integer, primary_key=True)
    Component_Name: Mapped[str] = Column(String)
    Marks: Mapped[int] = Column(Integer)

    # Relationships
    questions = relationship('Questions', back_populates='component_of_paper')

class Paper_Name(db.Model):
    __tablename__ = 'Paper_Name'

    Paper_ID: Mapped[int] = Column(Integer, primary_key=True)
    Paper_Name: Mapped[str] = Column(String, unique=True)

    # Relationships
    questions = relationship('Questions', back_populates='paper')

class Assessment_Objectives(db.Model):
    __tablename__ = 'Assessment_Objectives'

    AO_ID: Mapped[int] = Column(Integer, primary_key=True)
    AO_Int_Name: Mapped[str] = Column(String)

    # Relationships
    aOquestions = relationship('Questions', secondary='AOs_By_Paper', back_populates='objectives')

class AOs_By_Paper(db.Model):
    __tablename__ = 'AOs_By_Paper'

    QID: Mapped[int] = Column(Integer, ForeignKey('Questions.QiD'), primary_key=True)
    AO_ID: Mapped[int] = Column(Integer, ForeignKey('Assessment_Objectives.AO_ID'), primary_key=True)