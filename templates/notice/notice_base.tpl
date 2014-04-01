<a href="#" class="dropdown-toggle" data-toggle="dropdown">
    {% if notice_count == 0 %}
    {% else %}
    <span class="badge" style="background-color:red;margin-right:2px">{{notice_count}}</span>
    {% endif %}
    <span class="glyphicon glyphicon-bell"></span><b class="caret"></b></a>
<ul class="dropdown-menu">
    {% if notice_count == 0 %}
        <li><a href="#">没有任何新消息</a></li>
    {% else %}
        {% for new_friend in new_friend_notice %}
        <li><div class="notice-item"><a href="{% url user_space pk=new_friend.sender.ltuser.id %}">{{new_friend.sender}}</a>
            向您发出好友申请请求，
            <a href="#" onclick="friend_add_accept({{new_friend.id}})">接收</a>或者<a href="#" onclick="friend_add_refuse({{new_friend.id}});">忽略</a></div></li>
        {% endfor %}
        {% for is_accept in is_friend_accept %}
        <li><div class="notice-item"><a href="{% url user_space pk=is_accept.sender.ltuser.id %}">{{is_accept.sender}}</a>
            {% if is_accept.event == 'friend_accept' %}接受{% else %}拒绝{% endif %}了您的好友请求，<a href="#">已读</a>
        {% endfor %}
    <li class="divider"></li>
    {% endif %}
    <form id="notice-form">
        <input id="input1" class="hide">
        <input id="input2" class="hide">
    </form>
</ul>