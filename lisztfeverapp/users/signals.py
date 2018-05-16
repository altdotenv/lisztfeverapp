from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from urllib.request import urlopen
from django.core.files import File


@receiver(user_signed_up)
def user_signed_up(request, user, **kwargs):
    if len(user.socialaccount_set.all()) > 0:
        social_account = user.socialaccount_set.all()[0]
        uid = social_account.uid
        gender = social_account.extra_data.get('gender', None)
        user.gender = gender
        avatar = social_account.get_avatar_url()
        user.profile_pic.save(avatar)
        user.name = user.get_full_name()
    user.save()
