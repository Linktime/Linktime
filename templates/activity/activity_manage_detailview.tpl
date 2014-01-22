{% extends 'activity/activity_manage.tpl' %}

{% block css_head %}
        <link rel="stylesheet" href="{{ STATIC_URL }}css/bootstrap-editable.css" />
{% endblock %}

{% block content %}
        <div class="activity-detail" >
            <div class="activity-item">
                <div class="activity-title">
                    <a href="#" id="activity_name" data-type="text" data-pk="{{activity.id}}" data-title="修改用户名">{{activity.name}}</a>
                </div>
                <div class="activity-extra">
                    <div class="activity-price">
                        价格:<a href="#" id="activity_price" data-type="text" data-pk="{{activity.id}}" data-title="修改价格">{% if activity.price = 0 %}<span class="label label-success">Free</span>{% else %}{{activity.price}}{% endif %}</a></div>
                    <div class="activity-time" >时间:<a href="#" id="activity_date" data-pk="{{activity.id}}" data-title="修改时间">{{activity.date|date:"Y-m-d"}}</a></div>
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

{% block js_footer %}
        <!--tpl:'<div class="input-group"><input class="form-control" type="text"/><span class="input-group-btn"><button id="search_btn" class="btn btn-default" type="button"><span class="glyphicon glyphicon-th"></span></button></span></div>',-->
<script src="{{ STATIC_URL }}js/bootstrap-editable.min.js"></script>
<script type="text/javascript">
    var update_url="{% url ajax_activity_update pk=activity.id %}";
    $(document).ready(function() {
        $('#activity_name').editable({
            name:'name',
            mode:'inline',
            url:update_url,
        });

        $('#activity_price').editable({
            name:'price',
            placement:'right',
            url:update_url,
            {% if activity.price = 0 %}value:"0",{% endif %}
            validate: function(value) {
                if($.trim(value) == '') {
                    $.attr('value','0');
                    return '值不能为空';
                }
            },
        });

        $('#activity_date').editable({
            name:'date',
            mode:'popup',
            url:update_url,
            type:'date',
            placement:'bottom',
            clear:false,
            tpl:'<input class="form-control" type="text"/>',
            format: 'yyyy-mm-dd',
            viewformat: 'yyyy-mm-dd',
            datepicker: {
                weekStart: 1
            }
        });
    });
</script>
{% endblock %}