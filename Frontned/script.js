const API = "http://127.0.0.1:8000";

async function analyzeHeadline(){

const headline = document.getElementById("headline").value;

const res = await fetch(`${API}/analyze`,{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({headline})
})

const data = await res.json();

document.getElementById("result").innerHTML = `
<h3>Headline:</h3>
<p>${data.headline}</p>

<h3>Classification:</h3>
<p>${data.classification}</p>

<h3>Explanation:</h3>
<p>${data.explanation}</p>
`

loadHistory()

}

async function loadHistory(){

const res = await fetch(`${API}/history`)
const data = await res.json()

const historyDiv = document.getElementById("history")

historyDiv.innerHTML=""

data.forEach(h => {

historyDiv.innerHTML += `
<div class="history-item">
<b>${h.headline}</b><br>
${h.classification}
</div>
`

})

}

loadHistory()