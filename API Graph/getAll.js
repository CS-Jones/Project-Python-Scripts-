function getData() {
    var resp;
    $.ajax({
        url: "http://localhost:8081/helloworld",
        type: "POST",
        crossDomain: true,
        data: "getAll",
        async: false,
        dataType: "json",
        success: function (response) {
            resp = response;
            //$("#getAll").html(JSON.stringify(resp));
        },
        error: function (xhr, status) {
            alert("error");
        }
    });
    return resp;
};

function getData2() {
    var resp2;
    $.ajax({
        url: "http://localhost:8081/helloworld",
        type: "POST",
        crossDomain: true,
        data: "getAll2",
        async: false,
        dataType: "json",
        success: function (response) {
            resp2 = response;
            //$("#getAll").html(JSON.stringify(resp));
        },
        error: function (xhr, status) {
            alert("error");
        }
    });
    return resp2;
};


/*
$(document).ready(function(){
$.post( "http://localhost:8081/helloworld", function( data ) {
  $( ".getAll" ).html( data );
});
console.log("anything")
});*/