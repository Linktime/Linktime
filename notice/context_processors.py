from notice.models import NewFriendNotice
from django.contrib import auth


def notice(request):
    user = auth.get_user(request)
    if user.is_anonymous():
        return {}
    new_friend_notice = NewFriendNotice.objects.filter(receiver=user,had_read=False)
    notice_count = new_friend_notice.count()
    return {'new_friend_notice':new_friend_notice,'notice_count':notice_count}