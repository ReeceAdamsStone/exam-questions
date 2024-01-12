from sqlalchemy import Integer, String, ForeignKey, Table, Column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.schema import PrimaryKeyConstraint
# from app import db  

db = SQLAlchemy()

class Questions(db.Model):
    
    QiD: Mapped[int] = mapped_column(Integer, ForeignKey('AOs_By_Paper.QID'), primary_key=True)
    Question_String: Mapped[str] = mapped_column(String)
    Topic_ID: Mapped[int] = mapped_column(Integer, ForeignKey('Topics.Topic_ID'))
    Supporting_Material: Mapped[str] = mapped_column(String)
    # objectives = relationship('AOs_By_Paper', backref='aos_by_Q')

    objectives: Mapped[List[Assessment_Objectives]] = relationship(secondary=AOs_By_Paper)

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

class AOs_By_Paper(db.Model):
    __tablename__ = 'AOs_By_Paper'

    QID: Mapped[int] = mapped_column(Integer, ForeignKey('Questions.QiD'), primary_key=True)
    AO_ID: Mapped[int] = mapped_column(Integer, ForeignKey('Assessment_Objectives.AO_ID'), primary_key=True)
    question = relationship('Questions', backref='aos')
    ao = relationship('Assessment_Objectives', backref='questions')

    __table_args__ = (
        PrimaryKeyConstraint('QID','AO_ID'),
    )

AOs_By_Paper = Table(
    "AOs_By_Paper", Column("QID", ForeignKey("QiD"))
    "AOs_By_Paper", Column("AO_ID", ForeignKey("QiD")),
)
    
# dbtables = [Table1, Table2, Table3, Table4, Table5, Table6]


# Table1

# QiD	Question String		Topic ID	Supporting Material


# Table2

# Topic ID	Topic Name	Foreign Key to Component of paper ID 


# Table 3

# Component of Paper ID	Component Name	Marks	Foreign Key to Paper

# Table 4

# Paper ID 	Paper Name	

# Table 5

# AO ID		AO Int/Name

# Table 6 

# QID 		AO ID
