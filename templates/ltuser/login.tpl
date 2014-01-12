{% extends 'base.tpl' %}
{% block container %}
        <div class="row">
            <div class="col-md-4 col-md-offset-4">
                <form class="form" method="POST" action="">
                    {% csrf_token %}
                    <div class="input-group">
                    <span class="input-group-appon">帐号</span>{{form.username}}
                    </div>
                    <div class="input-group">
                    <span>密码</span>{{form.password}}
                    </div>
                    <input type="submit" value="登录" class="btn btn-primary">
                    <a class="btn btn-success" href="{% url register %}">注册</a>
                </form>
            </div>
        </div>
{% endblock %}