{% extends 'ltuser/user_base.tpl' %}
{% block content %}
        <div class="team-list">
        {% for team in teams %}
        <div class="team-item">
            <div class="team-leader">{{team.leader}}</div>
            <div class="team-member">{{team.member}}</div>
            <div class="team-date">{{team.date|date:"Y-m-d"}}</div>
            <div class="team-description">{{team.description}}</div>
        </div>
        {% endfor %}
        </div>
{% endblock %}