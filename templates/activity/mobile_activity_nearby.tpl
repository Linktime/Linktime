<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />

<title>附近的活动</title>
<style type="text/css">
    html,body {
        width:100%;
        height: 100%;
    }
    #map {width: 100%;height: 100%;overflow: hidden;margin:0;}
</style>
</head>
<body>
<div id="map"></div>
<script type="text/javascript" src="http://api.map.baidu.com/api?v=2.0&ak=tWoFM89fYumwstH3RLwVbYme"></script>
<script type="text/javascript">

// 百度地图API功能
var map = new BMap.Map("map");            // 创建Map实例
var point = new BMap.Point(121.400117,31.322826);
map.centerAndZoom(point,16);
map.addControl(new BMap.NavigationControl());  //添加默认缩放平移控件
map.enableScrollWheelZoom();                            //启用滚轮放大缩小

var circle = new BMap.Circle(point,500);
var markerMe = new BMap.Marker(point);
map.addOverlay(markerMe);
markerMe.setAnimation(BMAP_ANIMATION_BOUNCE); //跳动的动画
map.addOverlay(circle);

map.addOverlay(new BMap.Marker(new BMap.Point(121.398716,31.322856)));
map.addOverlay(new BMap.Marker(new BMap.Point(121.401554,31.322178)));
map.addOverlay(new BMap.Marker(new BMap.Point(121.40071,31.320188)));
</script>
</body>
</html>