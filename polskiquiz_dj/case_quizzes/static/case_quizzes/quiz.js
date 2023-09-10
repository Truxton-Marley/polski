//var adjectives = JSON.parse('{{ adjectives|safe }}');
console.log(adjectives);


let counter = 0;

function count() {
    counter++;
    const p_counter = document.querySelector("p.counter");
    p_counter.innerHTML = `The count is now ${counter}`;
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button.counter').onclick = count;
});

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function () {
        // do something
        const name = document.querySelector('#name').value;
        alert(`Hello, ${name}!`);
    };
});

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('button#color').forEach(function(button) {
        button.onclick = function() {
            document.querySelector('#frajda').style.color = button.dataset.color;
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('form#vocab').onsubmit = () => {
        const slowo = document.querySelector('input#vocab').value;
        console.log(slowo);
        const li = document.createElement('li');
        li.innerHTML = slowo;
        document.querySelector("ul#vocab").append(li);
        // Stop the form from submitting
        return false;
    }
});

function hello() {
    const h2 = document.querySelector("h2");
    if (h2.innerHTML === "Hello") {
        h2.innerHTML = "Good Bye";
    } else {
        h2.innerHTML = "Hello";
    }        
}
