<div class="col-md-3">
    {% include 'ltuser/user_info_panel.tpl' %}
    <ul class="nav nav-stacked linktime-side">
        <li><a href="{% url group_list %}">好友列表</a></li>
        <li><a href="{% url friend_search %}">添加好友</a></li>
    </ul>
</div>