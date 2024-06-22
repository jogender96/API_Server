# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Bank(Base):
    __tablename__ = 'banks'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    branches = relationship("Branch", back_populates="bank")

class Branch(Base):
    __tablename__ = 'branches'
    id = Column(Integer, primary_key=True)
    branch = Column(String, nullable=False)
    ifsc = Column(String, nullable=False)
    bank_id = Column(Integer, ForeignKey('banks.id'))

    bank = relationship("Bank", back_populates="branches")
