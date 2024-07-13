from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

def userExist(username):
    return User.objects.filter(username=username).count() < 1

def oldPasswordCorrect(old, user):
    password = User.objects.filter(username=user).first().password
    print(password)
    return check_password(old, password)