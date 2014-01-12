{% extends 'activity/activity_base.tpl' %}
{% block content %}
    <form class="form" action="{% url activity_create %}" method="POST">
    {% csrf_token %}
    {{ form.as_bf }}
    <input type="submit" class="btn btn-primary" value="提交">
    </form>
{% endblock %}

{% block js_footer %}
<script type="text/javascript">
    $(function() {$("#id_date").datepicker({ format: 'yyyy-mm-dd' }); });
</script>
{% endblock %}