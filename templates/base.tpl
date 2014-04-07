<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% block description %}<meta name="description" content="Linktime">{% endblock %}
    {% block keywords %}<meta name="keywords" content="Linktime">{% endblock %}
    <meta name="author" content="yang fan">
    {% include 'css.tpl' %}
    {% block css_head %}
    {% endblock %}
    <style type="text/css">
      html,
      body {
        height: 100%;
        background:url('{{ STATIC_URL }}image/ricepaper_v3.png')
        /* The html and body elements cannot have any padding or margin. */
      }

      /* Wrapper for page content to push down footer */
      #wrap {
        min-height: 100%;
        height: auto !important;
        height: 100%;
        /* Negative indent footer by it's height */
        margin: 0 auto -140px;
      }

      /* Set the fixed height of the footer here */
      #container {
        /*padding-top: 50px;*/
        margin-top: -20px;
      }
      #push,
      #footer {
        height:140px;
      }
      #footer {
        font-size: 12px;
        text-align: center;
        color:rgb(255,255,255);
        /*background-color: #f5f5f5;*/
        background-image:url('{{ STATIC_URL }}image/low_contrast_linen.png');
        position: relative;
      }

      /* Lastly, apply responsive CSS fixes as necessary */
      @media (max-width: 767px) {
        #footer {
          margin-left: -20px;
          margin-right: -20px;
          padding-left: 20px;
          padding-right: 20px;
        }
    }
      </style>
    <title>{% block title %}LinkTime{% endblock %}</title>
</head>
<body>
  <div id="wrap">
    <nav class="navbar navbar-inverse " role="navigation">
  <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#linktime-navbar">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="{% url index %}">LinkTime&nbsp;&nbsp;
          <!--<span class="version">Alpha</span>-->
      </a>
    </div>

      <div class="collapse navbar-collapse" id="linktime-navbar">
          <ul class="nav navbar-nav navbar-left">
            {% if user.is_authenticated %}<li {% block user_nav %}{% endblock %}><a href="{% url user_info pk=user.ltuser.id %}">个人空间</a></li>{% endif %}
            <li {% block activity_nav %}{% endblock %}><a href="{% url activity_list %}">活动</a></li>
            <li {% block friend_nav %}{% endblock %}><a href="{% url group_list %}">好友</a></li>
            {% block navbar_left_li %} {% endblock %}
            <li {% block create_nav %}{% endblock %}><a href="{% url activity_create %}">创建活动</a></li>
          </ul>
          <!--
          <form class="navbar-form navbar-left" role="search">
              <div class="input-group">
                  <input type="text" class="form-control" placeholder="活动名称/用户">
                  <span class="input-group-btn">
                      <button type="submit" class="btn btn-default">
                          GO!
                      </button>
                  </span>
              </div>
          </form>
          -->
          <ul class="nav navbar-nav navbar-right">
            <li class="divider-vertical"></li>
              {% if not user.is_authenticated %}
            <li><a href="{% url login %}">登录</a></li>
              {% else %}
              <li class="dropdown">{% include 'notice/notice_base.tpl' %}</li>
              <li><a href="{% url user_info pk=user.ltuser.id %}">{{user.username}}</a></li>
              <li><a href="{% url logout %}">注销</a></li>
              {% endif %}
              {% block navbar_right_li %} {% endblock %}
          </ul>
      </div><!--/.nav-collapse -->
  </nav>

  <div id="container">
    {% block index %}
    {% endblock %}

    <div class="container">
      {% block container %}

      {% endblock %}
    </div>
  </div>
  <div id="push"></div>
</div>

<div id="footer">
    {% include 'js.tpl' %}
    {% block js_footer %}
    {% endblock %}
<br>
    <p>IE内核的浏览器（包括但不限于IE，360浏览器）无法表现本站所有效果，推荐使用Firefox,Chrome或Opera等浏览器的较新版本可得到最佳浏览效果<br>IE8及更老的浏览器本站均不做支持</p><p>©  2013-2014 LinkTime </p><p>Author: <a href="http://www.renren.com/316795990/profile" target="_blank">Yang Fan</a>
</div>

</body>
</html>