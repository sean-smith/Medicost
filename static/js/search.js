$(function(){
    $.ajax({
        url: ""
        dataType: "json",


    })

    $("#search").on('submit', function(data){
        $("#procedure").val();
        $.ajax({
            type: "GET"
            url: "/search?procedure="+procedure+""

        });





});
