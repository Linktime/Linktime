{% extends 'activity/activity_base.tpl' %}

{% block create_nav %}class="active"{% endblock %}
{% block activity_nav %}{% endblock %}

{% block css_head %}
        <link rel="stylesheet" href="{{ STATIC_URL }}css/bootstrap-editable.css" />
        <style type="text/css">
            #
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
                <div class="activity-place">地点:<a href="#" id="address"></a>{{form.address}}</div>
                <div class="activity-map" >Map</div>
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
{% endblock %}