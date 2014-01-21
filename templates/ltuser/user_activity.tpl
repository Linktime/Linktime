{% extends 'ltuser/user_base.tpl' %}
{% block content %}

<!-- Nav tabs -->
<ul class="nav nav-tabs">
  <li class="active"><a href="#join" data-toggle="tab" onclick="join();">我参加的</a></li>
  <li><a href="#organize" data-toggle="tab" onclick="organize();">我组织的</a></li>
  <li><a href="#create" data-toggle="tab" onclick="create();">我创建的</a></li>
  <li><a href="#support" data-toggle="tab" onclick="support();">我赞助的</a></li>
    <li><a href="#mark" data-toggle="tab" onclick="mark();" >我收藏的</a></li>
</ul>

<!-- Tab panes -->
<div class="tab-content">
  <div class="tab-pane active" id="join">
      {% include 'ltuser/user_participant_activity.tpl' %}
  </div>
  <div class="tab-pane" id="organize"></div>
  <div class="tab-pane" id="create"></div>
  <div class="tab-pane" id="support"></div>
  <div class="tab-pane" id="mark"></div>
</div>

{% endblock %}

{% block js_footer %}
        <script type="text/javascript">
            function join(page=1){
                $.get("{% url user_activity_participant pk=user.ltuser.id %}" + "?page=" + page,function(data){
                    $("#join").html(data);
                });
            };
            function organize(page=1){
                $.get("{% url user_activity_organizer pk=user.ltuser.id %}" + "?page=" + page,function(data){
                    $("#organize").html(data);
                });
            };
            function create(page=1){
                $.get("{% url user_activity_creator pk=user.ltuser.id %}" + "?page=" + page,function(data){
                    $("#create").html(data);
                });
            };
            function support(page=1){
                $.get("{% url user_activity_sponsor pk=user.ltuser.id %}" + "?page=" + page,function(data){
                    $("#support").html(data);
                });
            };
            function mark(page=1){
                $.get("{% url user_activity_marker pk=user.ltuser.id %}" + "?page=" + page,function(data){
                    $("#mark").html(data);
                });
            };
        </script>
{% endblock %}