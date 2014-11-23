$(function(){
    //Need to make a server call to load procedures
    var procedures=["ActionScript","AppleScript","Asp","BASIC","C","C++","Clojure","COBOL","ColdFusion","Erlang","Fortran","Groovy","Haskell","Java","JavaScript","Lisp","Perl","PHP","Python","Ruby","Scala","Scheme"];

<<<<<<< HEAD
    $.ajax({
        url: 

    })

=======
//change this, Shawn
$('#dealerName').autocomplete({
    source: function (request, response) {
        $.getJSON("/example/location/example.json?term=" + request.term, function (data) {
            response($.map(data.dealers, function (value, key) {
                return {
                    label: value,
                    value: key
                };
            }));
        });
    },
    minLength: 2,
    delay: 100
});
>>>>>>> 52c12b3e9d0e741255a19b082b16ade5d080f732

    var $procedure = $('#procedure');
    $procedure.autocomplete({
        source: procedures
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
