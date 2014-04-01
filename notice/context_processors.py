from notice.models import NewFriendNotice, IsAcceptFriendNotice
from django.contrib import auth


def notice(request):
    user = auth.get_user(request)
    if user.is_anonymous():
        return {}
    new_friend_notice = NewFriendNotice.objects.filter(receiver=user,had_read=False)
    notice_count = new_friend_notice.count()

    is_friend_accept = IsAcceptFriendNotice.objects.filter(receiver=user,had_read=False)
    notice_count = is_friend_accept.count() + notice_count
    return {'notice_count':notice_count,
            'new_friend_notice':new_friend_notice,
            'is_friend_accept':is_friend_accept,
            }