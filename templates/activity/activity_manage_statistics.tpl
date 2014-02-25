{% extends 'activity/activity_manage.tpl' %}

{% block content %}
    <div class="activity-statistics">
        <div class="statistics-item">
            <div class="canvas">
                <canvas id="num-day" width="300" height="300"></canvas>
            </div>
            <div class="content">
                <div class="title"><h3>报名数据</h3></div>
                <div class="body">
                    在这里，你可以看到自报名以来，每一天报名人数情况。根据这份数据，有助于下次活动宣传时间安排。
                </div>
            </div>
        </div>

        <div class="statistics-item">
            <div class="content">
                <div class="title"><h3>性别数据</h3></div>
                <div class="body">
                    这是男女比例图，<font color="#F38630">男为60%</font>，<font color="#69D2E7">女为40%</font>。
                </div>
            </div>
            <div class="canvas">
                <canvas id="num-sex" width="300" height="300"></canvas>
            </div>
        </div>
        
        <div class="statistics-item">
            <div class="canvas">
                <canvas id="num-dep" width="300" height="300"></canvas>
            </div>
            <div class="content">
                <div class="title"><h3>院系数据</h3></div>
                <div class="body">
                    在这里你可以看到参加该活动，不同学院人数所占比例，有助于针对性的组织活动。其中：</br>
                    <font color="#F7464A">机械工程及其自动化学院10人</font></br>
                    <font color="#00CC33">通信信息与工程学院20人</font></br>
                    <font color="#FF9933">计算机工程与科学学院60人</font></br>
                    <font color="#949FB1">文学院5人</font></br>
                    <font color="#4D5360">理学院12人</font></br>
                </div>
            </div>
        </div>
    </div>
{% endblock %}

{% block js_footer %}
    <script src="{{ STATIC_URL }}js/Chart.js"></script>
    <script type="text/javascript">
        var num_day = $("#num-day").get(0).getContext("2d");
        var num_day_chart = new Chart(num_day);
        var data_num_day = {
        labels : ["01-05","06","08","15","02-01","04","09","17"],
        datasets : [
            {
                fillColor : "rgba(151,187,205,0)",
			    strokeColor : "rgba(151,187,205,1)",
			    pointColor : "rgba(151,187,205,1)",
                pointStrokeColor : "#fff",
                data : [0,65,59,90,81,56,55,40]
            },
            ]
        }

        num_day_chart.Line(data_num_day,{});


        var num_sex = $("#num-sex").get(0).getContext("2d");
        var num_sex_chart = new Chart(num_sex);
        var data_num_sex = [
            {
                value: 60,
                color:"#F38630"
            },
            {
                value : 40,
                color : "#69D2E7"
            }
        ]

        num_sex_chart.Pie(data_num_sex,{});

        var num_dep = $("#num-dep").get(0).getContext("2d");
        var num_dep_chart = new Chart(num_dep);

        var data_num_dep = [
            {
                value: 10,
                color:"#F7464A"
            },
            {
                value : 20,
                color : "#00CC33"
            },
            {
                value : 60,
                color : "#FF9933"
            },
            {
                value : 5,
                color : "#949FB1"
            },
            {
                value : 12,
                color : "#4D5360"
            }

        ]

        num_dep_chart.Doughnut(data_num_dep,{});

    </script>
{% endblock %}