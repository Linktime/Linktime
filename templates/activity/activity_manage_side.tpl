<div class="col-md-3">
    {% include 'ltuser/user_info_panel.tpl' %}
    <ul class="nav nav-stacked linktime-side">
        <li><a href="{% url activity_manage pk=activity.id %}">活动介绍</a></li>
        <li><a href="{% url activity_manage_options pk=activity.id %}">活动选项</a></li>
        <li><a href="{% url activity_manage_participant pk=activity.id %}">报名管理</a></li>
        <li><a href="#">信息统计</a></li>
        <li><a href="{% url activity_manage_task pk=activity.id %}">事物管理</a></li>
        <li><a href="#">电子票</a></li>
    </ul>
</div>