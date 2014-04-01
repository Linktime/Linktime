<section style="min-height:100px;"> <!-- FIX bug on chrome -->
    <ul id="gallery">
        <li id="fullPreview"></li>

        <li>
            <a href="{{ STATIC_URL }}img/full/1.jpg"></a>
            <img data-original="{{ STATIC_URL }}img/thumb/1.jpg" src="{{ STATIC_URL }}img/effects/white.gif" width="240" height="150" alt="Ocean" />

            <div class="overLayer"></div>
            <div class="infoLayer">
                <ul>
                    <li><h2>海报1</h2></li>
                    <li><p>查看全图</p></li>
                </ul>
            </div>

            <!--<div class="projectInfo">-->
                <!--<strong>-->
                    <!--Day, Month, Year:-->
                <!--</strong> sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.-->
            <!--</div>-->
        </li>
        <li>
            <a href="{{ STATIC_URL }}img/full/2.jpg"></a>
            <img data-original="{{ STATIC_URL }}img/thumb/2.jpg" src="{{ STATIC_URL }}img/effects/white.gif" width="240" height="150" alt="Ocean" />

            <div class="overLayer"></div>
            <div class="infoLayer">
                <ul>
                    <li><h2>海报2</h2></li>
                    <li><p>查看全图</p></li>
                </ul>
            </div>
    </li>
    </ul>
</section>
