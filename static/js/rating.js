function loadImage() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let res = this.responseText.split('\n')
            let href = res[0]
            let avg = res[1]
            document.getElementById('rating-image').src = href;
            document.getElementById('average-number').innerHTML = avg;

            if (avg === 'N/A') {
                document.querySelectorAll('.number-button').forEach(elem => {
                    elem.disabled = true;
                });
            } else {
                document.querySelectorAll('.number-button').forEach(elem => {
                    elem.disabled = false;
                });
            }
        }
    };

    mode = document.getElementById('both').checked ? 0 : document.getElementById('male').checked ? 1 : 2;

    xhttp.open("GET", "/get_image/mode=" + mode, true);
    xhttp.send();
}

function rateButton(e) {

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            if (this.responseText == 'redirect') {
                window.location.href = "/no_images/";
            } else
                loadImage()
        }
    };
    xhttp.open("GET", "/rate_image/" + e.value, true);
    xhttp.send();

}

function ready() {
    loadImage()
}

document.addEventListener("DOMContentLoaded", ready);
