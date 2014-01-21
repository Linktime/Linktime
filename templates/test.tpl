{% extends 'base.tpl' %}

{% block container %}
<!-- Nav tabs -->
<ul class="nav nav-tabs">
  <li><a href="#home" data-toggle="tab">Home</a></li>
  <li><a href="#profile" data-toggle="tab">Profile</a></li>
  <li><a href="#messages" data-toggle="tab">Messages</a></li>
  <li><a href="#settings" data-toggle="tab">Settings</a></li>
</ul>

<!-- Tab panes -->
<div class="tab-content">
  <div class="tab-pane active" id="home">1</div>
  <div class="tab-pane" id="profile">2</div>
  <div class="tab-pane" id="messages">3</div>
  <div class="tab-pane" id="settings">4</div>
</div>

{% endblock %}

{% block js_footer %}
{% endblock %}