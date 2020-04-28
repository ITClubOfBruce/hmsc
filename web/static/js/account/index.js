;
var account_index_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        $(".wrap_search .search").click(function(){
            $(".wrap_search").submit()
        })
        $(".remove").click(function(){
            id = $(this).attr("data")
            $.ajax({
                url:common_ops.buildUrl( "/account/removeOrRecover" ),
                type:'POST',
                data:{"id":id,"acts":"remove"},
                dataType:'json',
                success:function( res ){
                    var callback = null;
                    if( res.code == 200 ){
                        callback = function(){
                            window.location.href = common_ops.buildUrl("/account/index");
                        }
                    }
                    common_ops.alert( res.msg,callback );
                }
            });
        })
        $(".recover").click(function(){
            id = $(this).attr("data")
            $.ajax({
                url:common_ops.buildUrl( "/account/removeOrRecover" ),
                type:'POST',
                data:{"id":id,"acts":"recover"},
                dataType:'json',
                success:function( res ){
                    var callback = null;
                    if( res.code == 200 ){
                        callback = function(){
                            window.location.href = common_ops.buildUrl("/account/index");
                        }
                    }
                    common_ops.alert( res.msg,callback );
                }
            });
        })
    }
}

$(document).ready(function(){
    account_index_ops.init()
})