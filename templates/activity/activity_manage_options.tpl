{% extends 'activity/activity_manage.tpl' %}

{% block css_head %}
        <link rel="stylesheet" href="{{ STATIC_URL }}css/bootstrap-editable.css" />
{% endblock %}

{% block content %}
        <div class="activity-options">
            <div class="activity-title">Options</div>
            <div class="activity-team-select" >报名方式：<a id="activity-team-select" pk="{{activity.id}}">{{activity.activityoptions.team_flag}}</a></div>
            <div class="activity-during" >持续时间：<a id="activity-during" pk="{{activity.id}}">{{activity.activityoptions.during}}</a></div>
        </div>
{% endblock %}

{% block js_footer %}
    <script src="{{ STATIC_URL }}js/bootstrap-editable.min.js"></script>
    <script type="text/javascript">
        var update_url = "";
        $('#activity-team-select').editable({
            mode:'inline',
            type:'select',
            emptytext:'组队与个人',
            source:{'1':'组队与个人','2':'个人','3':'组队'},
        });
        $('#activity-during').editable({
            mode:'inline',
            type:'text',
            emptytext:'全天',
        })
    </script>
{% endblock %}