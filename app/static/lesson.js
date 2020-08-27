function goToEditor(text) {
    $.ajax({
        url: "/exampleEditor",
        method: "PUT",
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({
            html: text
        }),
        complete: function () {
            open("/exampleEditor")
        }
    })
}
