{% extends 'base.tpl' %}
{% block container %}
        <div class="login-bg"></div>
        <!--<div class="row">-->
        <form class="form" method="POST" action="">

            <div class="login-box">
                <div class="login-header">Linktime
                    <span class="version">Alpha</span>
                </div>
                <div class="login-body">
                    {% csrf_token %}
                    <div class="input-group input-username">
                    <span class="input-group-appon">帐号：</span>{{form.username}}
                    </div>
                    <div class="input-group input-password">
                    <span>密码：</span>{{form.password}}
                    </div>
                </div>
                <div class="btn-group login-footer">
                        <button type="submit" class="btn btn-primary btn-login">登录</button>
                        <a class="btn btn-success btn-register" href="{% url register %}">注册</a>
                    </div>
                </div>
            </form>
        <!--</div>-->
{% endblock %}