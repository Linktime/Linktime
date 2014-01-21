{% if not activitys %}
            <div class="alert alert-warning">你还没有创建任何活动哦，<a href="{% url activity_create %}">点击此</a>创建属于你的活动吧</div>
{% endif %}
      <div class="activity-list">
      {% for activity in activitys %}
        {% include 'activity/activity_list_item.tpl' %}
      {% endfor %}
      </div>

    {% if is_paginated %}
    <div>
        <ul class="pagination pagination-centered">
            {% if page_obj.has_previous %}
            <li><a href="#" onclick="create({{ page_obj.previous_page_number }})">«</a></li>
            {% endif %}
            {% for page in page_obj.paginator.page_range %}
            <li><a href="#" onclick="create({{page}});">{{page}}</a></li>
            {% endfor %}
            {% if page_obj.has_next %}
            <li><a href="#" onclick="create({{ page_obj.next_page_number }});">»</a></li>
            {% endif %}
            <li><a>第{{ page_obj.number }} 页/ 共{{ page_obj.paginator.num_pages }}页</a></li>
        </ul>
    </div><!-- paginate -->
{% endif %}