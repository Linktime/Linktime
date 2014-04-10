<div class="col-md-3">
    {% include 'ltuser/user_info_panel.tpl' %}
    <ul class="nav nav-stacked linktime-side">
        <li><a href="{% url activity_detail pk=activity.id %}">活动介绍</a></li>
        <li><a href="{% url activity_qrcode pk=activity.id %}">电子票</a></li>
    </ul>
</div>