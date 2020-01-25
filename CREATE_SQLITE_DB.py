# CREATING SQLITE DATABASE WITH CRICKET BATTERS

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy import create_engine, MetaData, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Text, Float


csvfiles = "ICC Test Batting Figures.csv"
engine = create_engine("sqlite:///cricket.sqlite")
conn = engine.connect()

###
# Use SQLAlchemy to model table schema
###
Base = declarative_base()


class Batters(Base):
    __tablename__ = 'Batters'

    id = Column(Integer, primary_key=True)
    player_name = Column(Text)
    span = Column(Text)
    matches = Column(Integer)
    innings = Column(Integer)
    no = Column(Integer)
    runs = Column(Float)
    hs = Column(Integer)
    avg = Column(Float) 
    hundred = Column(Integer)
    fifty = Column(Integer)
    zero = Column(Integer)
    PlayerProfile = Column(Text)



#     def __repr__(self):
#         return f"id={self.id}, name={self.title}"


Base.metadata.create_all(engine)
metadata = MetaData(bind=engine)
metadata.reflect()

###
# Use Pandas to read csv into a list of row objects
###

df = pd.read_csv(csvfiles, dtype=object, encoding="ISO-8859-1")
cricket_data = df.to_dict(orient='records')

###
# Insert data into table using SQLAlchemy
###

batter_table = sqlalchemy.Table('Batters', metadata, PrimaryKeyConstraint('id'),
                            autoload=True, extend_existing=True)

conn.execute(batter_table.delete())
conn.execute(batter_table.insert(), cricket_data)
