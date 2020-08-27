console.log("debugger")
$(run)

function run() {
    var code = $("textarea").val();
    code = strToHTML(code)
    var doc = $("#resultContent")[0].contentDocument.getElementsByTagName("html")[0].innerHTML = code.innerHTML
}

function strToHTML(code) {
    parser = new DOMParser()
    var newCode = parser.parseFromString(code, "text/html")
    return newCode.getElementsByTagName("html")[0]
}

$(document).delegate('textarea', 'keydown', function (e) {
    var keyCode = e.keyCode || e.which;

    if (keyCode == 9) {
        e.preventDefault();
        var start = this.selectionStart;
        var end = this.selectionEnd;

        $(this).val($(this).val().substring(0, start) +
            "    " +
            $(this).val().substring(end));

        this.selectionStart =
            this.selectionEnd = start + 4;
    }
});
