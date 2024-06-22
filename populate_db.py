# populate_db.py
from models import Base, Bank, Branch
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///banks.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add some sample data
bank1 = Bank(name="Bank A")
bank2 = Bank(name="Bank B")
session.add(bank1)
session.add(bank2)
session.commit()

branch1 = Branch(branch="Branch A1", ifsc="IFSC0001", bank=bank1)
branch2 = Branch(branch="Branch A2", ifsc="IFSC0002", bank=bank1)
branch3 = Branch(branch="Branch B1", ifsc="IFSC0003", bank=bank2)
session.add(branch1)
session.add(branch2)
session.add(branch3)
session.commit()

session.close()
