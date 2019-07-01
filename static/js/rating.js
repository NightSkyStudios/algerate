function loadImage() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('rating-image').src = this.responseText
        }
    };
    xhttp.open("GET", "/get_image", true);
    xhttp.send();
}

function rateButton(e) {
    console.log(e.value)

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('rating-image').src = this.responseText
        }
    };
    xhttp.open("GET", "/rate_image/" + e.value, true);
    xhttp.send();

    loadImage()

}
