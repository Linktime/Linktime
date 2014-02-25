{% extends 'ltuser/user_base.tpl' %}
{% block content %}
    <div class="user-info-detail">
        姓名：{{ltuser.user.username}}</br>
        爱好：{{ltuser.hobby}}</br>
        学院：计算机工程与科学学院</br>
        年龄：21</br>
    </div>
{% endblock %}