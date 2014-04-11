{% extends 'activity/activity_base.tpl' %}

{% block side %}
        <div class="col-md-2"></div>
{% endblock %}

{% block content %}

<form class="form" method="get" action=".">

    <div class="row">
        <div class="col-md-6">
            <div class="input-group">
                <input id="suggestId" class="form-control" placeholder="活动地点" name="place">
                <span class="input-group-btn">
                    <a id="search" class="btn btn-default">查询</a>
                </span>
            </div>
            <input class="form-control hidden" name="lat">
            <input class="form-control hidden" name="lng">
        </div>
        <div class="col-md-5 col-md-offset-1">
            <a href="{% url activity_search %}" class="btn btn-default col-md-6">按活动名查询</a>
        </div>
    </div>
</form>

{% if not activitys %}
    <div class="alert alert-warning">没有搜索到您要查询的活动</div>
{% endif %}
    <div class="activity-list">
        <div class="map">
            <div id="map"></div>
        </div>
    </div>

<div class="activity-list">
{% for activity in activitys %}
    {% include 'activity/activity_list_item.tpl' %}
{% endfor %}
    {% if is_paginated %}
    <div>
        <ul class="pagination pagination-centered">
            {% if page_obj.has_previous %}
            <li><a href="?page={{ page_obj.previous_page_number }}">«</a></li>
            {% endif %}
            {% for page in page_obj.paginator.page_range %}
            <li><a href="?page={{page}}">{{page}}</a></li>
            {% endfor %}
            {% if page_obj.has_next %}
            <li><a href="?page={{ page_obj.next_page_number }}">»</a></li>
            {% endif %}
            <li><a>第{{ page_obj.number }} 页/ 共{{ page_obj.paginator.num_pages }}页</a></li>
        </ul>
    </div>
    {% endif %}
            </div>
{% endblock %}

{% block js_footer %}
    <script type="text/javascript" src="http://api.map.baidu.com/api?v=2.0&ak=tWoFM89fYumwstH3RLwVbYme"></script>
        <script type="text/javascript">
            // 百度地图API功能
            var map = new BMap.Map("map");            // 创建Map实例
            {% if search_point %}
                var point = new BMap.Point({{search_point.lng}},{{search_point.lat}});
                map.centerAndZoom(point,16);
                var marker = new BMap.Marker(point);
                map.addOverlay(marker);
                marker.setAnimation(BMAP_ANIMATION_BOUNCE); //跳动的动画
                var circle = new BMap.Circle(point,500);
                map.addOverlay(circle);

                {% for point in points  %}
                map.addOverlay(new BMap.Marker(new BMap.Point({{point.lng}},{{point.lat}})));
                {% endfor %}
            {% else %}
                map.centerAndZoom('上海',12);
            {% endif %}
            map.addControl(new BMap.NavigationControl());  //添加默认缩放平移控件
            map.enableScrollWheelZoom();


        </script>

    <script type="text/javascript">
        var gc = new BMap.Geocoder(); // 工具
        var ac = new BMap.Autocomplete(    //建立一个自动完成的对象
        {"input" : "suggestId"
         ,"location" : map
        });
        $('#search').click(function(){
            var $form = $('form');
            gc.getPoint($('input[name="place"]').val(), function(point){
            if (point) {
                $('input[name="lat"]').attr("value",point.lat);
                $('input[name="lng"]').attr("value",point.lng);
                $form.submit();
                }
            }, "上海市");
        });
    </script>
{% endblock %}