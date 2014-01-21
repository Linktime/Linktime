{% if groups %}
        <div>
            <h5>共为您找到{{count}}个分组，请选择要添加到的分组</h5>
            <form id="group_form" class="form" action="{% url friend_add_pre %}" method="post">
                {% csrf_token %}
                <input id="user_id" type="text" class="hide" name="user_id">
                <select class="form-control" name="group_name">
                    {% for group in groups %}
                    <option>{{group.name}}</option>
                    {% endfor %}
                </select>
            </form>
        </div>
{% else %}
        <p>..</p>
{% endif %}