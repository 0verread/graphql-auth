from django.utils.crypto import get_random_string

"""
This is a custom util to create customized random
user id and many more.
"""

"""
user id will be starting with with char 'u'
"""
def get_user_id():
  user_id = get_random_string(length=11)
  return 'u' + user_id