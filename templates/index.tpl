{% extends 'base.tpl' %}
{% block index %}
<div class="jumbotron">
    <div class="container">
        <div class="row">
            <div class="col-md-6 text-center jumbotron-left">
                <h1>LinkTime<span style="vertical-align:super;font-size:10px">Alpha</span></h1>
                <p>方便、快捷的活动开展、参与和分享平台</p>
                <div class="description">
                    你可以在这里快速的筹备和开展一个活动（讲座、出游、展会、比赛等），并添加文字、图片以及视频描述，还可以方便的管理报名人员，对活动进行分享。也因此，在这里你能找到大量你感兴趣的活动参与，尽情享受吧！
                </div>
                <div class="download">
                    <button class="btn">下载Android客户端</button>
                </div>
            </div>
            <div class="col-md-6 jumbotron-right">


            <div class="carousel-bg">
                <div id="carousel-generic" class="carousel slide" data-ride="carousel">
              <!-- Indicators -->
                  <ol class="carousel-indicators">
                    <li data-target="#carousel-generic" data-slide-to="0" class="active"></li>
                    <li data-target="#carousel-generic" data-slide-to="1"></li>
                    <li data-target="#carousel-generic" data-slide-to="2"></li>
                  </ol>

                  <!-- Wrapper for slides -->
                  <div class="carousel-inner">
                    <div class="item active">
                      <img src="{{ STATIC_URL }}/image/activity-details.png">
                    </div>
                    <div class="item">
                      <img src="{{ STATIC_URL }}/image/friend-group.png">
                    </div>
                    <div class="item">
                      <img src="{{ STATIC_URL }}/image/details.png">
                    </div>
                  </div>

                  <!-- Controls -->
                  <a class="left carousel-control" href="#carousel-generic" data-slide="prev">
                    <span class="glyphicon glyphicon-chevron-left"></span>
                  </a>
                  <a class="right carousel-control" href="#carousel-generic" data-slide="next">
                    <span class="glyphicon glyphicon-chevron-right"></span>
                  </a>
                </div>

                </div>
            </div>
        </div>
  </div>
</div> <!-- jumbotron -->

<!--
<div class="server">
    <div class="title">

    </div>
        <div class="server-item-header">
            <div class="item-box item-box-1">
                <div class="item-border">
                    <div class="server-center">
                        <span class="glyphicon glyphicon-flash icon-4"/>
                    </div>
                </div>
                <div class="server-anima1"><span class="glyphicon glyphicon-picture icon-2"/></div>
                <div class="server-anima2"><span class="glyphicon glyphicon-gift icon-2"/></div>
                <div class="server-anima3"><span class="glyphicon glyphicon-qrcode icon-2"/></div>
                <div class="server-content">快速筹备和创建活动，你无需自己创建一个报名系统，并且我们还会为你提供良好的报名管理功能</div>
            </div>

            <div class="item-box item-box-2">
                <div class="item-border">
                    <div class="server-center">
                        <span class="glyphicon glyphicon-hand-up icon-4"/>
                    </div>
                </div>
                <div class="server-anima1"><span class="glyphicon glyphicon-picture icon-2"/></div>
                <div class="server-anima2"><span class="glyphicon glyphicon-gift icon-2"/></div>
                <div class="server-anima3"><span class="glyphicon glyphicon-qrcode icon-2"/></div>
                <div class="server-content">一键点击即可报名参加，报名记录系统自动为您做好，同时还会该活动生成唯一的二维码票证</div>
            </div>


            <div class="item-box item-box-3">
                <div class="item-border">
                    <div class="server-center">
                        <span class="glyphicon glyphicon-share icon-4"/>
                    </div>
                </div>
                <div class="server-anima1"><span class="glyphicon glyphicon-picture icon-2"/></div>
                <div class="server-anima2"><span class="glyphicon glyphicon-gift icon-2"/></div>
                <div class="server-anima3"><span class="glyphicon glyphicon-qrcode icon-2"/></div>
                <div class="server-content">方便快捷的宣传和分享,你可以一键共享到人人、QQ或者新浪微博</div>
            </div>

        </div>

    <div class="server-body">
    </div>
</div>
-->

<div class="use-data">
    <div class="use-item-1"><h3><font size="18px">48</font>个活动现在正在进行</h3></div>
    <div class="use-item-2"><h3><font size="18px">520</font>个活动曾经在本站上发布</h3></div>
    <div class="use-item-3"><h3>总共<font size="18px">30</font>个广告商在这里提供赞助</h3></div>
    <div class="use-item-4"><h3>超过<font size="18px">5000</font>个用户在这里找到了欢乐和收获</h3></div>
</div>

<div class="enter" ><a class="btn btn-success col-md-4 col-md-offset-4" href="{% url activity_create %}">立即开始创建活动</a></div>
{% endblock %}