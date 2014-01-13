{% extends 'ltuser/user_base.tpl' %}
{% block content %}
{% if not activitys %}
            <div class="alert alert-warning">你还没有参加任何活动哦，<a href="{% url activity_list %}">点击此</a>寻找适合你的活动报名吧</div>
{% endif %}
      <div class="activity-list">
      {% for activity in activitys %}
        <div class="activity-item" >
        <div class="activity-title" >活动名称:<a href="{% url activity_detail pk=activity.id %}" title="详情" >{{activity.name}}</a>
            <div class="activity-action">
                <a class="btn btn-info btn-xs" href="{% url activity_join pk=activity.id %}">参加</a>
                <a class="btn btn-primary btn-xs" href="{% url activity_mark pk=activity.id %}">收藏</a>
                <a class="btn btn-warning btn-xs">赞助</a>
            </div>
        </div>
        <div class="activity-content">简介:{{activity.introduction}}
        </div>

        <div class="activity-bottom">
            <div class="activity-price">价格:{% if activity.price = 0 %}<span class="label label-success">Free</span>{% else %}{{activity.price}}{% endif %}</div>
            <div class="activity-time" >时间:{{activity.date|date:"Y年m月d日"}}</div>
        </div>
    </div>
      {% endfor %}
      </div>

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
    </div><!-- paginate -->
    {% endif %}


{% endblock %}