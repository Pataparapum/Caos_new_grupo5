from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import ReadUser, WriteUser

def userExist(username):
    return User.objects.filter(username=username).count() > 0

def ReadUserExist(username):
    return ReadUser.objects.filter(userName=username).count() > 0

def WriteUserExist(username):
    return WriteUser.objects.filtert(userName=username).count() > 0

def oldPasswordCorrect(old, user):
    password = User.objects.filter(username=user).first().password
    print(password)
    return check_password(old, password)