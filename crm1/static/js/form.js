var n =  new Date();
var y = n.getFullYear();
var m = n.getMonth() + 1;
var d = n.getDate();
document.getElementById("date").innerHTML = d + "/" + m + "/" + y;


window.onload = function() {
    var n =  new Date();
    var y = n.getFullYear();
    var m = n.getMonth() + 1;
    var d = n.getDate();
    document.getElementById("date").innerHTML = d + "/" + m + "/" + y;
    console.log(document.getElementById("ar_id").innerHTML);

    var q = document.getElementById("ar_id").innerHTML;

    document.getElementById("id_Areaname").value = q;
}


