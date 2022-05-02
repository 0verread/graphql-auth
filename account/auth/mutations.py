import graphene
from graphene_django import DjangoObjectType
from ..models import Users
from .id_generator import get_user_id
from .base import SetPassword

class UserType(DjangoObjectType):
  class Meta:
    model = Users

class AccountRegistrationInput(graphene.InputObjectType):
  full_name = graphene.String(required=True)
  email = graphene.String(required=True)
  password = graphene.String(required=True)
  username = graphene.String(required=True)

class AccountRegister(graphene.Mutation):
  class Arguments:
    input =  AccountRegistrationInput(required=True)
  data = graphene.Field(UserType)

  @staticmethod
  def set_password(email, password):
    set_password = SetPassword(email, password)
    set_password.set_new_password()
    return None

  @staticmethod
  def mutate(self, info, input):
    id  = get_user_id() 
    acc_instance = Users(
      id = id,
      full_name = input.full_name,
      email = input.email,
      username = input.username
    )
    acc_instance.save()
    AccountRegister.set_password(input.email,input.password)
    # Exclude 'id' and 'password' field from return obj
    return AccountRegister(data=acc_instance)