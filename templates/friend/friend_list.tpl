{% extends 'friend/friend_base.tpl' %}
{% block content %}
        <div class="group-list">
            {% for group in groups %}
                <div class="group-item">
                    <div class="group-name">
                        <a href="{% url group_detail pk=group.id %}">{{group.name}}--{{group.owner.username}}</a>
                    </div>
                    <div class="group-friend-list">
                        {% for member in group.member.all %}
                            <div class="group-friend-item">
                                <a href="{% url user_space pk=member.ltuser.id %}" >{{member.username}}</a>
                            </div>
                        {% endfor %}
                    </div>
                </div>
            {% endfor %}
        </div>
{% endblock %}
