from django.core.exceptions import *

import apps.api.modules.city as mod_city
import apps.db.User.models as db_user
from apps.api.modules.exceptions import *


class User(object):
    def __init__(self, email, pswd_hash):
        try:
            user = db_user.User.objects.get(email=email)
            if user.pswd_hash != pswd_hash:
                raise WrongPasswordException('Wrong password.')
        except ObjectDoesNotExist:
            raise UserDoesNotExistException(
                f'User (Email={email}) does not exist.')

        db_user.UserSession.objects.filter(user_id=user.user_id).delete()

        self.user_dbobj = user
        self.user_session_dbobj = db_user.UserSession.objects.create(
            user_id=user)

        self.user_info = UserInfo(user_id=self.get_user_id())

    def get_user_id(self):
        return self.user_dbobj.user_id

    def get_session_id(self):
        return self.user_session_dbobj.session_id

    def get_email(self):
        return self.user_dbobj.email

    def get_user_info(self):
        return self.user_info

    def set_email(self, email):
        self.user_dbobj.email = email
        self.user_dbobj.save()
        return self.user_dbobj.email

    @classmethod
    def new_user(cls, email, pswd_hash, user_name, gender, resident_city_id):
        if db_user.User.objects.filter(email=email).exists():
            raise UserAlreadyExistsException(
                f'User (Email={email}) already exists, try to login.')
        resident_city = mod_city.get_city_instance_by_id(
            city_id=resident_city_id)
        user = db_user.User.objects.create(email=email,
                                           pswd_hash=pswd_hash)
        user_info = db_user.UserInfo.objects.create(
            user_id=user, user_name=user_name, gender=gender, resident_city_id=resident_city)
        return cls(email=email, pswd_hash=pswd_hash)


class UserInfoBase(object):
    def __init__(self, user_id):
        try:
            user_info = db_user.UserInfo.objects.get(user_id=user_id)
        except ObjectDoesNotExist:
            raise UserDoesNotExistException(
                f'User (ID={user_id}) does not exist.')
        self.user_info_dbobj = user_info

    def get_user_id(self):
        return self.user_info_dbobj.user_id

    def get_user_name(self):
        return self.user_info_dbobj.user_name

    def get_gender(self):
        return self.user_info_dbobj.gender

    def get_resident_city_id(self):
        return self.user_info_dbobj.resident_city_id.city_id


class UserInfo(UserInfoBase):
    def set_user_name(self, user_name):
        try:
            self.user_info_dbobj.user_name = user_name
            self.user_info_dbobj.save()
            return 0
        except Exception as e:
            raise e
            return 1

    def set_gender(self, gender):
        if gender not in (db_user.UserInfo.MALE,
                          db_user.UserInfo.FEMALE,
                          db_user.UserInfo.UNKNOWN):
            gender = db_user.UserInfo.OTHER
        try:
            self.user_info_dbobj.gender = gender
            self.user_info_dbobj.save()
            return 0
        except Exception as e:
            raise e
            return 1

    def set_resident_city_id(self, city_id):
        try:
            city = mod_city.get_city_instance_by_id(city_id=city_id)
            self.user_info_dbobj.resident_city_id = city
            self.user_info_dbobj.save()
            return 0
        except Exception as e:
            raise e
            return 1


class FriendInfo(UserInfoBase):
    def __init__(self, user_id, friend_user_id):
        try:
            self.friend_relation_dbobj = db_user.FriendRelation.objects.get(user_id=user_id,
                                                                            friend_user_id=friend_user_id)
        except ObjectDoesNotExist:
            raise FriendDoesNotExistException(f'Friend relation between '
                                              f'user (ID={user_id}) and user (ID={friend_user_id})'
                                              f' does not exist.')
        super().__init__(user_id=friend_user_id)

    def get_user_note(self):
        return self.friend_relation_dbobj.friend_user_note

    def set_user_note(self, user_note):
        try:
            self.friend_relation_dbobj.friend_user_note = user_note
            self.friend_relation_dbobj.save()
            return 0
        except Exception as e:
            raise e
            return 1


def check_user_existance(user_id, existance="Y"):
    '''
        Check the existance of user_id in the database user.User. Raise exceptions when the target user_id exists (or not).
            :param: existance, "Y" checks user_id in the database; "N" checks user_id not in the database.
    '''
    if existance == "Y":
        if not db_user.User.objects.filter(user_id=user_id).exists():
            raise UserDoesNotExistException(
                f'User (ID={user_id}) does not exist.')
    else:
        if db_user.User.objects.filter(user_id=user_id).exists():
            raise UserAlreadyExistsException(
                f'User (ID={user_id}) already exist.')
    return 0


def get_user_instance_by_id(user_id):
    check_user_existance(user_id)
    return db_user.User.objects.get(user_id=user_id)
