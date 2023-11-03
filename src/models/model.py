# src/models/model.py

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

class Episode(Base):
    __tablename__ = 'episodes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="episodes")

class Insight(Base):
    __tablename__ = 'insights'
    id = Column(Integer, primary_key=True, autoincrement=True)
    insight_text = Column(Text, nullable=False)
    episode_id = Column(Integer, ForeignKey('episodes.id'), nullable=False)
    episode = relationship("Episode", back_populates="insights")

User.episodes = relationship("Episode", order_by=Episode.id, back_populates="user")
Episode.insights = relationship("Insight", order_by=Insight.id, back_populates="episode")

# Setting up the database connection and metadata creation
engine = create_engine('sqlite:///autogen_assisted_reflection.db')
Base.metadata.create_all(engine)
