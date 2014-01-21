{% extends 'activity/activity_manage.tpl' %}

{% block content %}
        <div class="activity-detail" >
            <div class="activity-item">
                <div class="activity-title">
                    {{activity.name}}
                </div>
                <div class="activity-extra">
                    <div class="activity-price">价格:{% if activity.price = 0 %}<span class="label label-success">Free</span>{% else %}{{activity.price}}{% endif %}</div>
                    <div class="activity-time" >时间:{{activity.date|date:"Y年m月d日"}}</div>
                </div>
                <div class="activity-image-box">Images are Missing</div>
                <div class="activity-content">
                    简介:{{activity.introduction}}
                </div>
                <div class="activity-video-box">Videos are Escape</div>
                <div class="activity-map" >Map</div>
            </div>
        </div>
        <!--<embed src="http://player.youku.com/player.php/sid/XNjUzNTEzMzQw/v.swf" allowFullScreen="true" quality="high" width="480" height="400" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash"></embed>-->
{% endblock %}
