{% extends 'activity/activity_base.tpl' %}

{% block navbar_left_li %}
            <li><a href="{% url activity_detail pk=activity.id %}">返回查看</a></li>
{% endblock %}

{% block side %}
        {% include 'activity/activity_manage_side.tpl' %}
{% endblock %}