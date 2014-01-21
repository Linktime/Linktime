{% extends 'activity/activity_manage.tpl' %}

{% block content %}
        {% if participants %}
        <div>
            {% for participant in participants %}
                <div>{{participant.get_name}}</div>
            {% endfor %}
        </div>
        {% else %}
            <div class="alert alert-warning">抱歉，还没有人报名，赶紧宣传一下吧！</div>
        {% endif %}
{% endblock %}