const elems = document.getElementsByClassName('stream-status');

for (const elem of elems) {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4) {
            if (this.status == 200) {
                elem.classList.add('stream-status-online');
                elem.innerHTML = 'Online';
            } else {
                elem.classList.add('stream-status-offline');
                elem.innerHTML = 'Offline';
            }
        }
    };
    xhttp.open("GET", elem.getAttribute("data-videourl"), true);
    xhttp.send();
};
