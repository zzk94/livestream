
$('#post-form').on('submit', function(event){
        event.preventDefault();
//        console.log($("#post-form").serialize());
        //get the action-url of the form
        var actionurl = event.currentTarget.action;
        //do your own request an handle the results
        var posting = $.post( actionurl, $("#post-form").serialize());
        posting.done(function( data )
        {
            $('#id_content').val('');
            $("#talk").prepend("<li>" + data.username+" : "+data.content+" <sub><i>posted at "+data.time+"</i></sub></li>");
        });
    });

(function(){
    poll = function(){
        $.ajax({
            url: "/livestream/update/",
            dataType: "json",
            type: "get",
            success:function(data){
//                console.log(data.valid);
                if(data.valid == true){
                    $("#number_content").text(data.length_mess);
                    for(i = 0 ; i < data.length_mess ; i++){
//                        $("#talk").text("")
                        $("#talk").prepend("<li>"+data[i].username+" : "+data[i].content+" <sub><i>posted at "+data[i].time+"</i></sub></li>");
                    }
                }
            }
        })

    },

    pollInterval = setInterval(function(){
        poll();
    },2000);

    poll();
})();
