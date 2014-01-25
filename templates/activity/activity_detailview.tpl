{% extends 'activity/activity_base.tpl' %}
{% block navbar_left_li %}
        {% if organizer %}
        <li><a href="{% url activity_manage pk=activity.id %}">管理</a></li>
        {% endif %}
{% endblock %}

{% block side %}
        {% include 'activity/activity_side.tpl' %}
{% endblock %}
{% block content %}
        <div class="activity-detail" >
            <div class="activity-item">
                <div class="activity-title">
                    {{activity.name}}
                </div>
                <div class="activity-extra">
                    <div class="activity-price">
                        <form id="ticket_form" action="{% url activity_join pk=activity.id %}" method="post">
                            报名方式：<select name="type">
                                {% for ticket_type in ticket_types %}
                                <option value="{{ticket_type.type}}">{{ticket_type.type}}:{{ticket_type.price}}</option>
                                {% endfor %}
                            </select>
                            <a class="btn btn-success btn-sm" href="#" id="buy_ticket">报名</a>
                        </form>
                    </div>
                    <div class="activity-date" >时间:{{activity.date|date:"Y年m月d日"}}</div>
                </div>
                <div class="activity-image-box">在此处添加图片（未开放）</div>
                <div class="activity-content">
                    <p>简介：</p>
                    <div class="activity-abstract">{{activity.abstract}}</div>
                    <p>详情：</p>
                    <div class="activity-introduction">
                        {{activity.introduction|safe}}
                    </div>
                </div>
                <div class="activity-video-box">在此处添加视频（未开放）</div>
                <div class="activity-place">地点:{{activity.address}}</div>
                <div class="activity-map" >Map</div>
            </div>
        </div>
        <!--<embed src="http://player.youku.com/player.php/sid/XNjUzNTEzMzQw/v.swf" allowFullScreen="true" quality="high" width="480" height="400" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash"></embed>-->
{% endblock %}

{% block js_footer %}
        <script type="text/javascript">
            $('#buy_ticket').click(function(){
                $('#ticket_form').submit();
            });
        </script>
{% endblock %}