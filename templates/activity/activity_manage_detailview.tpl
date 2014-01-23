{% extends 'activity/activity_manage.tpl' %}

{% block css_head %}
        <link rel="stylesheet" href="{{ STATIC_URL }}css/bootstrap-editable.css" />
        <style type="text/css">
            #introduction {
                overflow-y:scroll;word-break:normal; min-height:300px;width:100%;
            }
        </style>
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
                    <div class="activity-date" >日期:<a href="#" id="activity_date" data-pk="{{activity.id}}" data-title="修改时间">{{activity.date|date:"Y-m-d"}}</a></div>
                </div>
                <div class="activity-image-box">在此处添加图片（未开放）</div>
                <div class="activity-content">
                    简介:</br>
                    <div class="activity-abstract">{{activity.abstract}}</div>
                    <div class="hide" id="introduction_toolbar">{% include 'activity/activity_wysiwyg_toolbar.tpl' %}</div>
                    <div id="activity_introduction" data-pk="{{activity.id}}">{{activity.introduction|safe}}</div>
                    <form id="introduction_form">
                    <input name="name" class="hide" value="introduction">
                    <input name="pk" class="hide" value="{{activity.id}}">
                    <textarea name="value" class="hide"></textarea>
                    <div id="introduction" class="form-control hide"></div>
                    </form>
                    <div id="editable-buttons" class="editable-buttons hide">
                            <button type="submit" class="btn btn-primary btn-sm editable-submit"><i class="glyphicon glyphicon-ok"></i></button>
                            <button type="button" class="btn btn-default btm-sm editable-cancel"><i class="glyphicon glyphicon-remove"></i></button>
                    </div>
                </div>
                <div class="activity-video-box">在此处添加视频（未开放）</div>
                <div class="activity-place">地点:<a href="#" id="activity_address" data-pk="{{activity.id}}" data-title="修改地点">{{activity.address}}</a></div>
                <div class="activity-map" >Map</div>
            </div>
        </div>
        <!--<embed src="http://player.youku.com/player.php/sid/XNjUzNTEzMzQw/v.swf" allowFullScreen="true" quality="high" width="480" height="400" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash"></embed>-->
{% endblock %}

{% block js_footer %}
        <!--tpl:'<div class="input-group"><input class="form-control" type="text"/><span class="input-group-btn"><button id="search_btn" class="btn btn-default" type="button"><span class="glyphicon glyphicon-th"></span></button></span></div>',-->
<script src="{{ STATIC_URL }}js/bootstrap-editable.min.js"></script>
<script src="{{ STATIC_URL }}js/jquery.hotkeys.js"></script>
<script src="{{ STATIC_URL }}js/bootstrap-wysiwyg.js"></script>
<script type="text/javascript">
    var update_url="{% url ajax_activity_update pk=activity.id %}";
    var introduction_width = $("#activity_introduction").width();
    $(document).ready(function() {

        $('#activity_name').editable({
            name:'name',
            mode:'inline',
            url:update_url,
        });

        $("#activity_address").editable({
            name:'address',
            mode:'inline',
            type:'text',
            url:update_url,
        });

        //DIY Introduction-editable
        //It seems ok, but I don't sure >_<
        $('#introduction').wysiwyg();
        $('#activity_introduction').click(function(){
            $("#introduction_toolbar").removeClass("hide");
            $(this).addClass('hide');
            $('#editable-buttons').removeClass('hide');
            $('#introduction').removeClass("hide").html($(this).html()).focus();
        });

        function introduction_close(){
            $("#introduction_toolbar").addClass("hide");
            $('#introduction').addClass('hide');
            $('#editable-buttons').addClass('hide');
            $('#activity_introduction').removeClass("hide");
        };

        //$('#introduction').on('blur',introduction_close);

        $('#editable-buttons button:eq(1)').click(introduction_close);
        $('#editable-buttons button:eq(0)').click(function(){
            var $form = $('#introduction_form');
            $form.children("textarea").html($('#introduction').html());
            $.post(update_url,$form.serialize(),function(data){
                $('#activity_introduction').html($('#introduction').html());
                introduction_close();
            })
        })


        //FIXME
        //-------------------------------------------------------------------
        /*
        $('#activity_introduction').editable({
            url:update_url,
            tpl:'<div id="introduction"></div><textarea id="introduction_area" class="hide"></textarea>',
            mode:'inline',
            onblur:'ignore',
            type:'wysihtml5',
            clear:false,
            showbuttons:'bottom',
        });

        $('#activity_introduction').on('shown',function(e,editable){
            $introduction = $("#introduction");
            $("#introduction_toolbar").removeClass("hide");
            $introduction.wysiwyg();
            $introduction.width(introduction_width*0.95);
            $introduction.html($('#activity_introduction').html());
        });

        $('#activity_introduction').on('hidden',function(e,editable){
            $("#introduction_toolbar").addClass("hide");
        });
        */
        //-------------------------------------------------------------------


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
                weekStart: 1,
            },
        });
    });
</script>
{% endblock %}