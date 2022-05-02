import hashlib
from django.utils.crypto import get_random_string

class passcode():
  @staticmethod
  def get_hashed_password(passwordText):
    pass_salt = get_random_string(length=10, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    salted_pass = pass_salt+passwordText
    hashed_pass = hashlib.sha256(salted_pass.encode('utf-8')).hexdigest()
    return pass_salt, hashed_pass
  
  def check_password(hashedPwd, pwd, salt):
    pwd_salt = salt+pwd
    cal_hashed_pwd = hashlib.sha256(pwd_salt.encode('utf-8')).hexdigest()
    return cal_hashed_pwd == hashedPwd
