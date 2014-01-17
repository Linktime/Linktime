{% extends 'ltuser/user_base.tpl' %}
{% block content %}
        <h2>TODO</h2>
        <div class="row">
            <div class="col-md-8 ">
                {{ltuser.hobby}}
                {{ltuser.user.username}}
            </div>
        </div>
{% endblock %}