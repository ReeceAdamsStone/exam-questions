from __future__ import annotations
from sqlalchemy import Integer, String, ForeignKey, Table, Column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app import db
from typing import List
# from app import db  

# db = SQLAlchemy()

AOs_By_Paper = Table(
    "AOs_By_Paper",
    db.Model.metadata,
    Column("QID", ForeignKey('Questions.QiD'), primary_key=True),
    Column("AO_ID", ForeignKey('Assessment_Objectives.AO_ID'), primary_key=True),
)

class Questions(db.Model):
    __tablename__ = 'Questions'
    
    # QiD: Mapped[int] = mapped_column(Integer, ForeignKey('AOs_By_Paper.QID'), primary_key=True)
    QiD: Mapped[int] = mapped_column(Integer, primary_key=True)
    Question_String: Mapped[str] = mapped_column(String)
    Topic_ID: Mapped[int] = mapped_column(Integer, ForeignKey('Topics.Topic_ID'))
    Supporting_Material: Mapped[str] = mapped_column(String)
    # objectives = relationship('AOs_By_Paper', backref='aos_by_Q')

    objectives: Mapped[List[Assessment_Objectives]] = relationship(secondary=AOs_By_Paper, back_populates="aOquestions")

class Topics(db.Model):
    __tablename__ = 'Topics'

    Topic_ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Topic_Name: Mapped[str] = mapped_column(String)
    Component_of_Paper_ID: Mapped[int] = mapped_column(Integer, ForeignKey('Component_of_Paper.Component_of_Paper_ID'))
    questions = relationship('Questions', backref='topic')

class Component_of_Paper(db.Model):
    __tablename__ = 'Component_of_Paper'

    Component_of_Paper_ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Component_Name: Mapped[str] = mapped_column(String)
    Marks: Mapped[int] = mapped_column(Integer)
    Paper_ID: Mapped[int] = mapped_column(Integer, ForeignKey('Paper_Name.Paper_ID'))
    components = relationship('Topics', backref='paper')

class Paper_Name(db.Model):
    __tablename__ = 'Paper_Name'

    Paper_ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Paper_Name: Mapped[str] = mapped_column(String)
    components = relationship('Component_of_Paper', backref='paper')

class Assessment_Objectives(db.Model):
    __tablename__ = 'Assessment_Objectives'

    AO_ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    AO_Int_Name: Mapped[str] = mapped_column(String)
    aOquestions: Mapped[List[Questions]] = relationship(secondary=AOs_By_Paper, back_populates="objectives")