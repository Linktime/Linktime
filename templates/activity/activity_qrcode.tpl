{% extends 'activity/activity_detailview.tpl' %}

{% block content %}
    <img src="{% url activity_qrcode_img pk=activity.id %}" width="300" height="300">
{% endblock %}