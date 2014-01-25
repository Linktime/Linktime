{% extends 'base.tpl' %}

{% block user_nav %}class="active"{% endblock %}

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
        {% include 'ltuser/user_side.tpl' %}
    {% endblock %}

    <div class="col-md-8">
    {% block content %}
    {% endblock %}
    </div>
{% endblock %}