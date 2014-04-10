<div class="activity-item" >
    <div class="activity-title" >{% if activity.preparing %}[筹备中]{% endif %}活动名称:<a href="{% url activity_detail pk=activity.id %}" title="详情" >{{activity.name}}</a>
        <div class="activity-action">
            {% comment %}
            <a class="btn btn-info btn-xs" href="{% url activity_join pk=activity.id %}">参加</a>
            <a class="btn btn-warning btn-xs">赞助</a>
            {% endcomment %}
            <a class="btn btn-md" href="{% url activity_mark pk=activity.id %}" title="收藏"><span class="glyphicon glyphicon-star-empty"></span></a>
        </div>
    </div>
    <div class="activity-organizer">主办方：
         {% for organizer in activity.organizer_list_activity.all %}
                        {% for single in organizer.single.all %}
                            <a type="button" class="btn btn-default" href="{% url user_space pk=single.ltuser.id %}">{{ single.username }}</a>
                        {% endfor %}
                        <br>
                        {% for team in organizer.single.all %}
                            {{ team.name }}
                        {% endfor %}
                    {% endfor %}
    </div>
    <div class="activity-content">简介:{{activity.abstract}}
    </div>

    <div class="activity-bottom">
        <!--<div class="activity-price">价格:{% if activity.price = 0 %}<span class="label label-success">Free</span>{% else %}{{activity.price}}元{% endif %}</div>-->
        <div class="activity-price">价格:&nbsp;&nbsp;<span class="label label-success">Free</span></div>
        <div class="activity-date" >时间:{{activity.date|date:"Y年m月d日"}}</div>
    </div>

</div>