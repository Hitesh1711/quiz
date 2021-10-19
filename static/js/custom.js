$(document).ready(function () {
    $('.summernote').summernote({
        height: 250
    });
});

function addDiv(divclassname, layout_added) {
    var itm = document.getElementsByClassName(divclassname);
    var cln = itm[0].cloneNode(true);
    document.getElementsByClassName(layout_added)[0].appendChild(cln);
}

function removeDiv(divclassname, layout_added) {
    if (document.getElementsByClassName(divclassname).length > 1) {
        document.getElementsByClassName(layout_added)[0].lastElementChild.remove();
    }

}

$("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("active");
});