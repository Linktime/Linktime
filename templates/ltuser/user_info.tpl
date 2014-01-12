{% extends 'ltuser/user_base.tpl' %}
{% block content %}
        <div class="row">
            <div class="col-md-8 ">
                {{ltuser.hobby}}
                {{ltuser.user.username}}
            </div>
        </div>
{% endblock %}