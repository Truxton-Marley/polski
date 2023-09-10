document.addEventListener('DOMContentLoaded', () => {
    for (const key in js_slownik) {
        console.log(`${key}: ${js_slownik[key]}`)
        const li = document.createElement('li');
        li.innerHTML = `${key}: ${js_slownik[key]}`;
        document.querySelector("ul#slownik").append(li);
    }
});

// TODO: Servce JSON via own API and use fetch:
// fetch(http://thisip/myapiendpoint_json)
// .then(response => {
//      return response.json()
//  }
// .then(data => { console.log(data) })
// .catch(error => { // do something });
