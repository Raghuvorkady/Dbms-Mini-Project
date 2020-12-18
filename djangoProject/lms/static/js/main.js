function search() {
    input = document.getElementById("searchInput");
    value = input.value;
    var searchUrl = "{% url 'search' " + value + " %}";
    alert(value);
    var id = $(this).attr('id');

    document.location.href=searchUrl + "/" + id;
}
