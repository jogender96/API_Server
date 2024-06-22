# schema.py
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Bank as BankModel, Branch as BranchModel

class Bank(SQLAlchemyObjectType):
    class Meta:
        model = BankModel

class Branch(SQLAlchemyObjectType):
    class Meta:
        model = BranchModel

class Query(graphene.ObjectType):
    all_branches = graphene.List(Branch)

    def resolve_all_branches(parent, info):
        query = Branch.get_query(info)
        return query.all()

schema = graphene.Schema(query=Query)
