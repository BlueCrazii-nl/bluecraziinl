const elems = document.getElementsByClassName('stream-status');

function refreshStreams() {
    for (const elem of elems) {
        makeRequest(elem.getAttribute("data-videourl"), function () {
            if (this.readyState == 4) {
                if (this.status == 200) {
                    elem.classList.add('stream-status-online');
                    setViewerCount(elem);
                } else {
                    elem.classList.add('stream-status-offline');
                    elem.innerHTML = 'Offline';
                }
            }
        })
    };
}

function setViewerCount(elem) {
    const url = "https://viewers.bluecrazii.nl/views/" + elem.getAttribute("data-name");
    makeRequest(url, function () {
        if (this.readyState == 4 && this.status == 200) {
            elem.innerHTML = "Online: " + this.responseText;
        }
    });
}

function makeRequest(url, callback) {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = callback;
    xhttp.open("GET", url, true);
    xhttp.send();
}

refreshStreams();
setInterval(() => refreshStreams(), 5000);
