{% extends 'activity/activity_manage.tpl' %}

{% block content %}
    {% if not activity_tickettype %}
        <div class="alert alert-warning">抱歉，还没有人报名，赶紧宣传一下吧！</div>
    {% else %}
        <div class="participant-list">
        {% for tickettype in activity_tickettype %}
        <div><b>票务类型：{{tickettype.type}}</b></div>
        <div class="participant-single"><div class="participant-title">个人报名</div>
            <table class="table table-hover">
            <thead>
            <tr><th>用户名</th><th>报名时间</th><th></th></tr>
            </thead>
            <tbody>
            {% for singleticket in tickettype.single_ticket_type.all %}
                <tr><td><a href="{% url user_space pk=singleticket.owner.ltuser.id %}">{{singleticket.owner.username}}</a></td><td>{{singleticket.datetime|date:"Y-m-d h:i:s"}}</td>
                    <td><a class="btn close" title="移除" data-id="{{single.single.id}}" data-name="{{single.single.username}}">&times;</a></td>
                </tr>
            {% endfor %}
            </tbody>
            </table>
        </div>
        <div class="participant-team"><div class="participant-title">团队报名</div>
            <table class="table table-hover">
            <thead>
            <tr><th>队名</th><th>报名时间</th></tr>
            </thead>
            <tbody>
            {% for team in tickettype.team.all %}
                <tr><td><a href="＃">{{team.team.name}}</a></td><td>{{team.datetime|date:"Y-m-d h:i:s"}}</td></tr>
            {% endfor %}
            </tbody>
            </table>
        </div>
        {% endfor %}
        </div> <!-- participant-list -->
    {% endif %}

<!-- Modal -->
<div class="modal fade" id="confirm" tabindex="-1" role="dialog" aria-labelledby="confirmLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-body">
        <p>你确认要移除下列报名者吗？</p>
          <form>
            <ul></ul>
          </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">返回</button>
        <button type="button" class="btn btn-primary" >确认</button>
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->

{% endblock %}

{% block js_footer %}
        <script type="text/javascript">
                $('.participant-single table').find('a.close').bind('click',function(){
                    $('#confirm').modal();
                    $('#confirm').find('ul').html('<li>'+$(this).data('name')+'</li>');
                });
        </script>
{% endblock %}