<script src="{{ STATIC_URL }}js/jquery-2.0.3.min.js"></script>
<script src="{{ STATIC_URL }}js/bootstrap.min.js"></script>
<script src="{{ STATIC_URL }}js/bootstrap-datepicker.js"></script>
<script src="{{ STATIC_URL }}js/locales/bootstrap-datepicker.zh-CN.js"></script>

<script type="text/javascript">
    function friend_add_refuse(id) {
        var $form = $('#notice-form');
        var $input1 = $('#input1');
        $('#input1').attr('name','notice_id').attr('value',id);
        $.post('{% url ajax_friend_add_refuse %}',$form.serialize(),function(data){

        });
    }

    function friend_add_accept(id) {
        var $form = $('#notice-form');
        var $input1 = $('#input1');
        $('#input1').attr('name','notice_id').attr('value',id);
        $.post('{% url ajax_friend_add_accept %}',$form.serialize(),function(data){

        });
    }
</script>
