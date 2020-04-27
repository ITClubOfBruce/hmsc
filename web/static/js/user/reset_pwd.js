;
var mod_pwd_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        $("#save").click(function(){
            var btn_target = $(this)
            if (btn_target.hasClass("disabled")) {
                alert("重置正在进行中，请稍后再试")
                return;
            }

            var old_password = $("#old_password").val()
            var new_password = $("#new_password").val()

            if (!old_password){
                alert("请输入原密码")
                return false;
            }
            if (!new_password || new_password.length < 6) {
                alert("请输入不少于6位的新密码")
                return false
            }

            btn_target.addClass("disabled")

            $.ajax({
                url:common_ops.buildUrl("/user/reset-pwd"),
                type:"POST",
                data:{'old_password':old_password,'new_password':new_password},
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
    mod_pwd_ops.init()
})