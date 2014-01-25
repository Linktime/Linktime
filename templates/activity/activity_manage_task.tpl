{% extends 'activity/activity_manage.tpl' %}
{% block content %}
        <div class="task-list">
            <table class="table table-hover table-striped">
                <thead>
                    <tr><th>任务内容</th><th>指派人</th><th>截止日期</th><th>完成状态</th></tr>
                </thead>
                <tbody>
                    {% for task in tasks %}
                    <tr>
                        <td>{{task.task}}</td>
                        <td>{% for user in task.assign.all %}<label>{{user.username}}</label>{% endfor %}</td>
                        <td>{{task.deadline|date:"Y-m-d h:i:s"}}</td>
                        <td>{% if task.done %}<span class="label label-success">完成</span>{% else %}<span class="label label-danger">未完成</span>{% endif %}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
{% endblock %}