from django.contrib.auth.models import User
from mongoengine import Document, fields
import mongoengine

class User(Document):
    username = fields.StringField(required=True, unique=True)
    email = fields.EmailField(required=True, unique=True)
    password = fields.StringField(required=True)

class Account(Document):
    user = fields.ReferenceField(User, required=True, reverse_delete_rule=mongoengine.CASCADE)
    balance = fields.IntField()

class Transaction(Document):
    account = fields.ReferenceField(Account, required=True)
    amount = fields.IntField(required=True, default=0)
    type = fields.StringField(choices=['deposit', 'withdraw'], required=True)

 

