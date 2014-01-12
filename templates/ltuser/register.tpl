{% extends 'base.tpl' %}
{% block container %}
<div class="row">
    <div class="col-md-4 col-md-offset-4">
        <form class="form-group" method="POST" action="{% url register %}">
        {% csrf_token %}
        <div class="input-group">
            <span class="input-group-appon">帐号</span>{{form.username}}
        </div>
        <div class="input-group">
            <span class="input-group-appon">密码</span>{{form.password}}
        </div>
        <div class="input-group">
            <span class="input-group-appon">重复密码</span>{{form.repassword}}
        </div>
        <div class="input-group">
            <span class="input-group-appon">邮箱</span>{{form.email}}
        </div>
        <input class="btn btn-success" type="submit" value="注册">
        </form>
    </div>
</div>
{% endblock %}