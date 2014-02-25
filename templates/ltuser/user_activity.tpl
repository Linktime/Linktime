{% extends 'ltuser/user_base.tpl' %}
{% block content %}

<!-- Nav tabs -->
<ul class="nav nav-tabs">
  <li class="active"><a href="#join_tab" data-toggle="tab" onclick="join(1);">我参加的</a></li>
  <li><a href="#organize_tab" data-toggle="tab" onclick="organize(1);">我组织的</a></li>
  <li><a href="#create_tab" data-toggle="tab" onclick="create(1);">我创建的</a></li>
  <li><a href="#support_tab" data-toggle="tab" onclick="support(1);">我赞助的</a></li>
    <li><a href="#mark_tab" data-toggle="tab" onclick="mark(1);" >我收藏的</a></li>
</ul>

<!-- Tab panes -->
<div class="tab-content">
  <div class="tab-pane active" id="join_tab">
      {% include 'ltuser/user_participant_activity.tpl' %}
  </div>
  <div class="tab-pane" id="organize_tab"></div>
  <div class="tab-pane" id="create_tab"></div>
  <div class="tab-pane" id="support_tab"></div>
  <div class="tab-pane" id="mark_tab"></div>
</div>

{% endblock %}

{% block js_footer %}
        <script type="text/javascript">
            function join(page){
                $.get("{% url user_activity_participant pk=user.ltuser.id %}" + "?page=" + page,function(data){
                    $("#join_tab").html(data);
                });
            };
            function organize(page){
                $.get("{% url user_activity_organizer pk=user.ltuser.id %}" + "?page=" + page,function(data){
                    $("#organize_tab").html(data);
                });
            };
            function create(page){
                $.get("{% url user_activity_creator pk=user.ltuser.id %}" + "?page=" + page,function(data){
                    $("#create_tab").html(data);
                });
            };
            function support(page){
                $.get("{% url user_activity_sponsor pk=user.ltuser.id %}" + "?page=" + page,function(data){
                    $("#support_tab").html(data);
                });
            };
            function mark(page){
                $.get("{% url user_activity_marker pk=user.ltuser.id %}" + "?page=" + page,function(data){
                    $("#mark_tab").html(data);
                });
            };


        </script>
{% endblock %}