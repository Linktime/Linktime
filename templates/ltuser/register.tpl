{% extends 'base.tpl' %}
{% block container %}
    <div class="login-bg"></div>
    <form class="form-group" method="POST" action="{% url register %}">
        <div class="login-box">
            <div class="login-header">Linktime
                <span style="vertical-align:super;font-size:10px">Alpha</span>
            </div>
            <div class="login-body">
                {% csrf_token %}
                <div class="input-group input-username">
                    <span class="input-group-appon">帐号：</span>{{form.username}}
                </div>
                <div class="input-group input-username">
                    <span class="input-group-appon">密码：</span>{{form.password}}
                </div>
                <div class="input-group input-username">
                    <span class="input-group-appon">重复：</span>{{form.repassword}}
                </div>
                <div class="input-group input-username">
                    <span class="input-group-appon">邮箱：</span>{{form.email}}
                </div>
            </div>
            <div class="btn-group login-footer">
                <button class="btn btn-success btn-register" type="submit" >注册</button>
                <a class="btn btn-primary btn-login" href="{% url login %}">返回登录</a>
            </div>

        </div>
    </form>
{% endblock %}