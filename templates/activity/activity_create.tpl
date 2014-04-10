{% extends 'activity/activity_base.tpl' %}

{% block create_nav %}class="active"{% endblock %}
{% block activity_nav %}{% endblock %}

{% block css_head %}
        <link rel="stylesheet" href="{{ STATIC_URL }}css/bootstrap-editable.css" />
        <style type="text/css">
            html,body {
                width:100%;
                height:100%;
            }
        </style>
{% endblock %}

{% block side %}
        <div class="col-md-2"></div>
{% endblock %}

{% block content %}

<div class="create-step">
    <table class="table" align="center">
        <tbody>
            <tr><td><div class="step-bg">I.</div>创建</td><td><div class="step-bg">II.</div>筹备</td><td><div class="step-bg">III.</div>发布</td></tr>
        </tbody>
    </table>
    <div class="progress progress-striped active">
      <div class="progress-bar progress-bar-success" style="width: 33.3%">

      </div>
      <!--<div class="progress-bar progress-bar-warning" style="width: 33.3%">-->

      <!--</div>-->
      <!--<div class="progress-bar progress-bar-danger" style="width: 33.3%">-->

      <!--</div>-->
    </div>
</div>



    <form class="form" action="{% url activity_create %}" method="POST">
    {% csrf_token %}

    <div class="activity-detail" >
            <div class="activity-item">
                <div class="activity-title">
                    <a href="#" id="name"></a>
                    {{form.name}}
                </div>
                <div class="activity-content">
                    <p>简介（<font color="red">200字以内</font>）：</p>
                    <div class="activity-abstract">
                        {{form.abstract}}
                    </div>
                </div>
                <div class="activity-extra">
                    <div class="activity-price">价格:<a href="#" id="price" title="暂时支持免费活动"></a>{{form.price}}元</div>
                    <div class="activity-date" >日期:<a href="#" id="date"></a>{{form.date}}</div>
                </div>
                <div class="activity-image-box">在此处添加图片（未开放）</div>
                <div class="activity-content">
                    <p>详情：</p>
                    {% include 'activity/activity_wysiwyg_toolbar.tpl' %}
                    <div class="form-control activity-introduction" id="introduction"></div>
                    {{ form.introduction }}
                </div>
                <div class="activity-video-box">在此处添加视频（未开放）</div>
                <div class="activity-place">地点:<a href="#" id="address"></a>
                    {{form.address}}
                    <input name="lat" class="hidden">
                    <input name="lng" class="hidden">
                    <br>
                    <div class="row">
                        <div class="col-md-6 col-md-offset-3">
                            <div class="input-group">
                                 <span class="input-group-addon">快速搜索:</span>
                                <input class="form-control" type="text" id="suggestId">
                                <span class="input-group-btn" ><a class="btn btn-default" id="search">定位</a></span>
                            </div>
                            <div id="searchResultPanel" style="border:1px solid #C0C0C0;width:150px;height:auto;">
                            </div>
                        </div>
                    </div>
                </div>
                <div class="activity-map" ><div id="map"></div></div>
            </div>
        </div>
    </form>
    <input id="submit" type="submit" class="btn btn-primary pull-right" value="筹备">
{% endblock %}

{% block js_footer %}
<script src="{{ STATIC_URL }}js/bootstrap-editable.min.js"></script>
<script src="{{ STATIC_URL }}js/jquery.hotkeys.js"></script>
<script src="{{ STATIC_URL }}js/bootstrap-wysiwyg.js"></script>
<script type="text/javascript">
    $("#name").editable({
        mode:'inline',
        emptytext:'在此输入活动名称',
        type:'text',
    });

    $("#address").editable({
        mode:'inline',
        emptytext:'在此输入活动地点',
        type:'text',
    });

    $("#price").editable({
        type:'select',
        mode:'inline',
        prepend:'0',
        source:{"1":"0"},
    });

    $("#date").editable({
        mode:'popup',
        placement:'bottom',
        emptytext:'例如2014-01-01',
        type:'date',
        clear:false,
        tpl:'<input class="form-control" type="text"/>',
        format: 'yyyy-mm-dd',
        viewformat: 'yyyy-mm-dd',
        datepicker: {
            weekStart: 1,
        },
    });

    $("#submit").click(function(){
        var $form = $("form");
        var $introduction = $("#introduction");
        $("#id_introduction").html($introduction.html());
        var $name = $("#name");
        $("#id_name").attr("value",$name.html());
        var $date = $("#date");
        $("#id_date").attr("value",$date.html());
        var $price = $("#price");
        $("#id_price").attr("value",$price.html());
        var $address = $("#address");
        $("#id_address").attr("value",$address.html());
        $form.submit();
    });

    $(function() {
        $("#id_date").datepicker({
            format: 'yyyy-mm-dd',
            language:'zh-CN',
            });
        //$("#id_introduction").wysiwyg();
        $("#introduction").wysiwyg();
     });
</script>
<!-- 以下是百度地图API -->
<script type="text/javascript" src="http://api.map.baidu.com/api?v=2.0&ak=tWoFM89fYumwstH3RLwVbYme"></script>
<script type="text/javascript">
// 百度地图API功能
function G(id) {
    return document.getElementById(id);
}

var map = new BMap.Map("map");
map.centerAndZoom("上海市",12);                   // 初始化地图,设置城市和地图级别。
map.addControl(new BMap.NavigationControl());  //添加默认缩放平移控件
map.enableScrollWheelZoom();                            //启用滚轮放大缩小

var gc = new BMap.Geocoder(); // 工具

var ac = new BMap.Autocomplete(    //建立一个自动完成的对象
    {"input" : "suggestId"
    ,"location" : map
});

map.addEventListener("click",function(e){
    $("input[name='lat']").attr("value",e.point.lat);
    $("input[name='lng']").attr("value",e.point.lng);
    gc.getLocation(e.point, function(rs){
        var addComp = rs.addressComponents;
        var str = addComp.province + ", " + addComp.city + ", " + addComp.district + ", " + addComp.street + ", " + addComp.streetNumber;
        $("#address").html(str);
        $("#id_address").attr("value",str);
        $("#address").editable({
            mode:'inline',
            emptytext:'在此输入活动地点',
            type:'text',
        });
    });
    var marker = new BMap.Marker(e.point);  // 创建标注
    map.clearOverlays();
    map.addOverlay(marker);              // 将标注添加到地图中
    marker.setAnimation(BMAP_ANIMATION_BOUNCE); //跳动的动画
});

$("#search").click(function(){
    gc.getPoint($("#suggestId").val(), function(point){
  if (point) {
    map.centerAndZoom(point, 16);
    map.addOverlay(new BMap.Marker(point));
  }
}, "上海市");
});

</script>
{% endblock %}