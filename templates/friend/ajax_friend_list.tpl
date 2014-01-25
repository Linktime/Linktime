<div class="friend-search-list">
{% if users %}
<div>搜索到{{count}}个相关用户</div>
{% for single_user in users %}
        <div class="friend-item">
            <div class="friend-name"><a href="{% url user_space pk=single_user.ltuser.id %}">{{single_user.username}}</a></div>
            <div class="friend-action">
                <a href="#" onclick="addfriend({{single_user.id}})" class="btn btn-info btn-sm" data-id="{{single_user.id}}" >＋好友</a>
            </div>
        </div>
{% endfor %}
{% else %}
        <div class="alert alert-warning">Sorry，没有找到任何用户！</div>
{% endif %}
</div>