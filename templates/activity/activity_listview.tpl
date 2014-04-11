{% extends 'activity/activity_base.tpl' %}

{% block side %}
        <div class="col-md-2"></div>
{% endblock %}

{% block content %}
        <div class="activity-list">
        <div class="row">
            <div class="btn-group col-md-6 col-md-offset-3">
                <a href="{% url activity_search %}" class="btn btn-default col-md-6">按活动名查询</a>
                <a href="{% url activity_search_map %}" class="btn btn-default col-md-6">按地理位置查询</a>
            </div>
        </div>

{% for activity in activitys %}
    {% include 'activity/activity_list_item.tpl' %}
{% endfor %}
    {% if is_paginated %}
    <div>
        <ul class="pagination pagination-centered">
            {% if page_obj.has_previous %}
            <li><a href="?page={{ page_obj.previous_page_number }}">«</a></li>
            {% endif %}
            {% for page in page_obj.paginator.page_range %}
            <li><a href="?page={{page}}">{{page}}</a></li>
            {% endfor %}
            {% if page_obj.has_next %}
            <li><a href="?page={{ page_obj.next_page_number }}">»</a></li>
            {% endif %}
            <li><a>第{{ page_obj.number }} 页/ 共{{ page_obj.paginator.num_pages }}页</a></li>
        </ul>
    </div>
    {% endif %}
            </div>
{% endblock %}

{% block js_footer %}

{% endblock %}