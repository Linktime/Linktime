<div class="activity-item" >
    <div class="activity-title" >活动名称:<a href="{% url activity_detail pk=activity.id %}" title="详情" >{{activity.name}}</a>
        <div class="activity-action">
            <a class="btn btn-info btn-xs" href="{% url activity_join pk=activity.id %}">参加</a>
            <a class="btn btn-primary btn-xs" href="{% url activity_mark pk=activity.id %}">收藏</a>
            <a class="btn btn-warning btn-xs">赞助</a>
        </div>
    </div>
    <div class="activity-organizer">主办方：
        {% for organizer in activity.organizer.all %}
            {{organizer.get_name}}
        {% endfor %}
    </div>
    <div class="activity-content">简介:{{activity.introduction}}
    </div>

    <div class="activity-bottom">
        <div class="activity-price">价格:{% if activity.price = 0 %}<span class="label label-success">Free</span>{% else %}{{activity.price}}{% endif %}</div>
        <div class="activity-time" >时间:{{activity.date|date:"Y年m月d日"}}</div>
    </div>

</div>