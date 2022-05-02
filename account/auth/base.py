from .generators import passcode
from ..models import Users, Salts

class SetPassword:
  def __init__(self, email, password, username=None, id=None):
      self.email = email
      self.password = password
      self.username = username
      self.id = id

  def set_new_password(self):
    salt, hashed_pass = passcode.get_hashed_password(self.password)
    user = Users.objects.get(email=self.email)
    user.password = hashed_pass
    user.save(update_fields=["password"])
    salt_instance = Salts(
      user_id = user.id,
      pass_salt = salt
    )
    salt_instance.save()
    return None