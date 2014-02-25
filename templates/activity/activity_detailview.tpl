{% extends 'activity/activity_base.tpl' %}
{% block navbar_left_li %}
        {% if organizer %}
        <li><a href="{% url activity_manage pk=activity.id %}">管理</a></li>
        {% endif %}
{% endblock %}

{% block css_head %}
        <link href="{{ STATIC_URL }}css/least.min.css" rel="stylesheet" />
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
                <div class="activity-content">
                    <p>简介：</p>
                    <div class="activity-abstract">{{activity.abstract}}</div>
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
                <div class="activity-image-box">
                    {% include 'activity/activity_image.tpl' %}
                </div>
                <div class="activity-content">
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
        </br>
        <div class="bshare-custom"><a title="分享到QQ空间" class="bshare-qzone"></a><a title="分享到新浪微博" class="bshare-sinaminiblog"></a><a title="分享到人人网" class="bshare-renren"></a><a title="分享到腾讯微博" class="bshare-qqmb"></a><a title="分享到网易微博" class="bshare-neteasemb"></a><a title="更多平台" class="bshare-more bshare-more-icon more-style-addthis"></a><span class="BSHARE_COUNT bshare-share-count">0</span></div><script type="text/javascript" charset="utf-8" src="http://static.bshare.cn/b/buttonLite.js#style=-1&amp;uuid=&amp;pophcol=2&amp;lang=zh"></script><script type="text/javascript" charset="utf-8" src="http://static.bshare.cn/b/bshareC0.js"></script>
        <!-- least.js JS-file -->
        <script src="{{ STATIC_URL }}js/least.min.js" defer="defer"></script>
        <!-- Lazyload JS-file -->
        <script src="{{ STATIC_URL }}js/jquery.lazyload.min.js" defer="defer"></script>
        <script type="text/javascript">
            $('#buy_ticket').click(function(){
                $('#ticket_form').submit();
            });

            $(document).ready(function(){
                $('#gallery').least();
            });
        </script>


{% endblock %}