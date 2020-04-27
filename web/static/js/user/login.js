;
var user_login_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $(".login_wrap .do-login").click(function(){
            var btn_target = $(this)
            if (btn_target.hasClass("disabled")) {
                alert("请求正在处理，请稍后再试~~~")
                return;
            }
            var login_name = $(".login_wrap input[name=login_name]").val()
            var login_pwd = $(".login_wrap input[name=login_pwd]").val()

            // 前端校检
            if (login_name == undefined || login_name.length < 1){
                alert('请输入正确的用户名')
                return
            }
            if (login_pwd == undefined || login_pwd.length < 1){
                alert('请输入正确的密码')
                return
            }

            btn_target.addClass("disabled");

            $.ajax({
                url:common_ops.buildUrl("/user/login"),
                type:"POST",
                data:{'login_name':login_name,'login_pwd':login_pwd},
                dataType:'json',
                success:function(resp){
                    btn_target.removeClass("disabled");
                    console.log(resp)
                    alert(resp.msg)
                    window.location.reload()
                },
                error:function(error){
                    console.log(error)
                }
            })
        })
    }
}


$(document).ready(function(){
    user_login_ops.init();
})