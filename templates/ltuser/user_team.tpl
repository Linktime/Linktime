{% extends 'ltuser/user_base.tpl' %}
{% block content %}
{% if not teams %}
    <div class="alert alert-warning">你还没有参加任何团队哦，<a href="#">寻找我的团队</a>或者<a href="#">创建一个团队</a></div>
{% endif %}

<div class="team-list">
{% for team in teams %}
<div class="team-item">
    <div class="team-name">{{team.name}}</div>
    <div class="team-leader">Leader：{{team.leader}}</div>
    <div class="team-member">成员：
        {% for member in team.member.all %}
        <a href="{% url user_space pk=member.ltuser.id %}">{{member.username}}  </a>
        {% endfor %}
    </div>
    <div class="team-date">创建日期：{{team.date|date:"Y-m-d"}}</div>
    <div class="team-description">简介：{{team.description}}</div>
</div>
{% endfor %}
</div>
{% endblock %}