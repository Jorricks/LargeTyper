
function setCookie(name, id) {
    var element = document.getElementById(id);
    var elementValue = escape(element.value);

    document.cookie = name + "=" + elementValue + "; path=/; expires=" + expiry.toGMTString();
    console.log(document.cookie);
}

function storeValues(form) {
    setCookie("email", form.email - field.value);
    return true;
}