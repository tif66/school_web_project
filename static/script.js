function loadRandomJoke() {
    const box = document.getElementById("randomJoke");
    if (!box) return;

    fetch("/api/jokes/random")
        .then(r => r.json())
        .then(d => {
            box.innerText = d.joke;
        });
}

function loadAllJokes() {
    const list = document.getElementById("jokesList");
    if (!list) return;

    fetch("/api/jokes")
        .then(r => r.json())
        .then(jokes => {
            list.innerHTML = "";
            jokes.forEach(j => {
                const li = document.createElement("li");
                li.innerText = j;
                list.appendChild(li);
            });
        });
}

function addJoke() {
    const text = document.getElementById("jokeInput").value;
    const msg = document.getElementById("msg");

    fetch("/api/jokes", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text})
    })
    .then(r => r.json())
    .then(d => {
        msg.innerText = d.message;
    });
}

window.onload = () => {
    loadRandomJoke();
    loadAllJokes();
};