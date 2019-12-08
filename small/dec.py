# Decorators are no longer covered in the course, but I decided
# to retain the example anyway.
def decorate(f):
  def wrapper():
    return f().upper()
  return wrapper
@decorate
def get_name():
    return "nick russo"
print(get_name())
