from app import db  
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Table1(Base):
    __tablename__ = 'Questions'

    QiD = Column(Integer, primary_key=True)
    Question_String = Column(String)
    Topic_ID = Column(Integer, ForeignKey('table2.Topic_ID'))
    Supporting_Material = Column(String)

class Table2(Base):
    __tablename__ = 'Topics'

    Topic_ID = Column(Integer, primary_key=True)
    Topic_Name = Column(String)
    Component_of_Paper_ID = Column(Integer, ForeignKey('table3.Component_of_Paper_ID'))
    questions = relationship('Table1', backref='topic')

class Table3(Base):
    __tablename__ = 'Component of Paper'

    Component_of_Paper_ID = Column(Integer, primary_key=True)
    Component_Name = Column(String)
    Marks = Column(Integer)
    Paper_ID = Column(Integer, ForeignKey('table4.Paper_ID'))
    components = relationship('Table2', backref='paper')

class Table4(Base):
    __tablename__ = 'Paper Type'

    Paper_ID = Column(Integer, primary_key=True)
    Paper_Name = Column(String)
    components = relationship('Table3', backref='paper')

class Table5(Base):
    __tablename__ = 'Assessment Objectives'

    AO_ID = Column(Integer, primary_key=True)
    AO_Int_Name = Column(String)

class Table6(Base):
    __tablename__ = 'AOs By Paper'

    QID = Column(Integer, ForeignKey('table1.QiD'), primary_key=True)
    AO_ID = Column(Integer, ForeignKey('table5.AO_ID'), primary_key=True)
    question = relationship('Table1', backref='aos')
    ao = relationship('Table5', backref='questions')

    
dbtables = [Table1, Table2, Table3, Table4, Table5, Table6]


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
