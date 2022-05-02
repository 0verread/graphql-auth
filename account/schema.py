import graphene
from graphene_django import DjangoObjectType
from .auth.mutations import AccountRegister
from .models import Users, Salts

from .auth.generators import passcode
class user(DjangoObjectType):
  class Meta:
    model = Users
    exclude_fields = ('id', 'password',)

class AccountQueries(graphene.ObjectType):
  user = graphene.List(user)
  user_name_pass = graphene.Field(user, email=graphene.String(), password = graphene.String())

  def resolve_user(self, info, **kargs):
    return Users.objects.all()

  def resolve_user_name_pass(self, info, email, password):
    user = Users.objects.get(email=email)
    if user:
      pwd = user.password
      pwd_salt = Salts.objects.get(user_id=user.id).pass_salt
      is_pwd_correct = passcode.check_password(pwd, password, pwd_salt)
      if is_pwd_correct:
        return [user]
    # Return an Error stating "Invalid username or password"
    return None

class AccountMutations(graphene.ObjectType):
  account_register = AccountRegister.Field()
  