<div class="col-md-3">
    <ul class="nav nav-stacked linktime-side">
        <li><a href="{% url user_info pk=user.ltuser.id %}">个人信息</a></li>
        <li><a href="#">好友动态</a></li>
        <li><a href="{% url user_activity pk=user.ltuser.id %}">个人活动</a></li>
        <li><a href="{% url user_team pk=user.ltuser.id %}">团队管理</a></li>
        <li><a href="#">留言板</a></li>
        <li><a href="#">私信</a></li>
    </ul>
</div>