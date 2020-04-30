;

var goods_set_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        var that = this
        $(".wrap_goods_set .save").click(function(){
            var btn_target = $(this)
            if (btn_target.hasClass("disabled")) {
                alert("请求正在进行，请稍后再试")
                return
            }
            var cat_id_target_value = $(".wrap_goods_set input[name=cat_id]").val()
            var name_target_value = $(".wrap_goods_set input[name=name]").val()
            var price_target_value = $(".wrap_goods_set input[name=price]").val()
            var summary = $.trim("dddddddddddddd")
            var stock_target_value = $(".wrap_goods_set input[name=stock]").val()
            var tags_target_value = $.trim($(".wrap_goods_set input[name=tags]").val())
            if ( parseInt(cat_id_target_value) < 1 ) {
                alert("请选择分类")
                return
            }
            if (name_target_value.length < 1) {
                alert("请输入符合规范的名称")
                return false;
            }
            if ( parseInt(price_target_value) < 1 ) {
                alert("请输入符合规范的售价")
                return
            }
            if ($(".wrap_goods_set .pic-each").length < 1) {
                alert("请上传封面")
                return
            }
            if (summary.length < 10) {
                alert("请输入描述，不少于10个字符")
                return false;
            }
            if ( parseInt(stock_target_value) < 1 ) {
                alert("请输入符合规范的库存")
                return
            }
            if (tags_target_value.length < 1) {
                alert("请输入标签，便于搜索")
                return
            }

            btn_target.addClass("disabled")
            

            var data = {
                cat_id:cat_id_target_value,
                name:name_target_value,
                price:price_target_value,
                main_image:$(".wrap_goods_set .pic-each .del_image").attr("data"),
                summary:summary,
                stock:stock_target_value,
                tags:tags_target_value,
                id:$(".wrap_goods_set input[name=id]").val()
            }
            $.ajax({
                url:common_ops.buildUrl("/goods/set"),
                type:"POST",
                data:data,
                dataType:"json",
                success:function(resp){
                    console.log(resp.msg)
                    btn_target.removeClass("disabled")
                    if(resp.code == 200){
                        window.location.href = common_ops.buildUrl("/goods/index")
                    }
                },
                error:function(error){
                    console.log(error)
                }
            })
        })
    },
    initEditor:function(){

    },
    delete_img:function(){

    }
}


$(document).ready(function(){
    goods_set_ops.init()
})