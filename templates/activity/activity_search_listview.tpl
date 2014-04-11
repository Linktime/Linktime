{% extends 'activity/activity_base.tpl' %}

{% block side %}
        <div class="col-md-2"></div>
{% endblock %}

{% block content %}

<form class="form" method="get" action=".">
    <div class="row">
        <div class="col-md-6">
            <div class="input-group">
                <input class="form-control" placeholder="活动名称" name="activity_name">
                <span class="input-group-btn">
                    <button class="btn btn-default">查询</button>
                </span>
            </div>
        </div>
        <div class="col-md-5 col-md-offset-1">
            <a href="{% url activity_search_map %}" class="btn btn-default col-md-6">按地理位置查询</a>
        </div>
    </div>
</form>

<div class="activity-list">
{% if not activitys %}
    <div class="alert alert-warning">没有搜索到您要查询的活动</div>
{% endif %}
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