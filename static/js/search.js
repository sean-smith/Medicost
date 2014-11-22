$(function(){
    //Need to make a server call to load procedures
    var availableTags=["ActionScript","AppleScript","Asp","BASIC","C","C++","Clojure","COBOL","ColdFusion","Erlang","Fortran","Groovy","Haskell","Java","JavaScript","Lisp","Perl","PHP","Python","Ruby","Scala","Scheme"];

    $("#procedure").autocomplete({
        source: availableTags
    });

    var error = function(data){
        var error_bar = "<div class='alert alert-danger' role='alert'><button type='button' class='close' data-dismiss='alert'><span aria-hidden='true'>&times;</span><span class='sr-only'>Close</span></button>"+data+"</div>";
        $("#error").html(error_bar);

    }



    $("#search").on('submit', function(event){
        event.preventDefault();
        var procedure = $("#procedure").val();
        var zip = $("#zip").val();
        if( procedure ==""){
            error("Please Enter a procedure");
            return false
        }
        if( zip ==""){
            error("Please Enter a zip code");
            return false
        }
        $.ajax({
            type: "POST",
            data: {
                "procedure": procedure,
                "zip": zip
            },
            url: "/search?procedure="+procedure+"&zip="+zip,
            success: function(data){
                console.log("success");
            }
        });
        return false;




    });

});
