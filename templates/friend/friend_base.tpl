{% extends 'base.tpl' %}

{% block friend_nav %}class="active"{% endblock %}

{% block container %}
    {% block messages %}
        {% if messages %}
        {% for message in messages %}
        <div class="alert fade in alert-block alert-{% if message.tags = 'error' %}danger{% else %}{{ message.tags }}{% endif %}">
            <button type="button" class="close" data-dismiss="alert">×</button>
            {{ message }}
        </div>
        {% endfor %}
        {% endif %}
    {% endblock %}

    {% block side %}
        {% include 'friend/friend_side.tpl' %}
    {% endblock %}

    <div class="col-md-8">
    {% block content %}
    {% endblock %}
    </div>
{% endblock %}