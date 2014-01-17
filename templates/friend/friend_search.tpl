{% extends "friend/friend_base.tpl" %}
{% block content %}
        <div>
            <form >
                <div class="input-group">
                    {% csrf_token %}
                  <input type="text" placeholder="在此输入要搜索的好友名字" class="form-control" name="username">
                    <span class="input-group-btn">
                        <button id="search_btn" class="btn btn-default" type="button">搜索</button>
                  </span>
                </div><!-- /input-group -->
            </form>
        </div>
        <div>
            <div id="friend_list">
            </div>
        </div>


         <!-- Button trigger modal -->

<!-- Modal -->
<div class="modal fade" id="select_group" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title" id="myModalLabel">请选择一个好友分组</h4>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">返回</button>
        <button type="button" class="btn btn-primary">确认</button>
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->
{% endblock %}

{% block js_footer %}
    <script type="text/javascript">
    $("#search_btn").click(function(){
        var $form = $("form")
        $.post("{% url ajax_friend_search %}",$form.serialize(),function(data){
            $("#friend_list").html(data);
        });
    });

    // FIXME
    $(function(){
    $(".friend-action a").click(function(){
        var id = $(this).data("id");
        $("#select_group").modal("show");
        });
    });
    </script>
{% endblock %}