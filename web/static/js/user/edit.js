;
var user_edit_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        // 获取到“保存”按钮
        $('.user_edit_wrap .save').click(function(){
            var btn_target = $(this)
            if (btn_target.hasClass("disabled")){
                alert("正在处理，请稍后再试~~~")
                return;
            }
            var nickname_value = $(".user_edit_wrap input[name=nickname]").val();
            var email_value = $(".user_edit_wrap input[name=email]").val();

            if (!nickname_value || nickname_value.length < 2) {
                alert('请输入与规范的昵称')
                return false
            }
            if (!email_value || email_value.length < 2) {
                alert('请输入与规范的邮箱')
                return false
            }
            
            btn_target.addClass("disabled");

            $.ajax({
                url:common_ops.buildUrl("/user/edit"),
                type:"POST",
                data:{'nickname':nickname_value,'email':email_value},
                dataType:'json',
                success:function(resp){
                    console.log(resp)
                    alert(resp.msg)
                    btn_target.removeClass("disabled");
                },
                error:function(error){
                    console.log(error)
                }
            })
        })
    }
}
$(document).ready(function(){
    user_edit_ops.init()
})