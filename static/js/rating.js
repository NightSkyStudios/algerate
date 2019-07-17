function loadImage() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('rating-image').src = this.responseText.split('\n')[0];
            document.getElementById('average-number').innerHTML = this.responseText.split('\n')[1];
        }
    };

    mode = document.getElementById('both').checked?0:document.getElementById('male').checked?1:2;

    xhttp.open("GET", "/get_image/mode=" + mode, true);
    xhttp.send();
}

function rateButton(e) {
    console.log(e.value)

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            loadImage()
        }
    };
    xhttp.open("GET", "/rate_image/" + e.value, true);
    xhttp.send();

}

function ready(){
    loadImage()
}

document.addEventListener("DOMContentLoaded", ready);
