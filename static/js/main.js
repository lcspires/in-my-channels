// Seleciona elementos da página
const form = document.getElementById("search-form");
const input = document.getElementById("search-input");
const resultsDiv = document.getElementById("results");

// Função para limpar resultados anteriores
function limparResultados() {
    resultsDiv.innerHTML = "";
}

// Função para exibir resultados
function exibirResultados(videos) {
    limparResultados();

    if (!videos || videos.length === 0) {
        const msg = document.createElement("p");
        msg.textContent = "No videos found";
        resultsDiv.appendChild(msg);
        return;
    }

    const ul = document.createElement("ul");
    videos.forEach(video => {
        const li = document.createElement("li");
        li.textContent = `${video.canal} - ${video.titulo}`;
        ul.appendChild(li);
    });

    resultsDiv.appendChild(ul);
}

// Função para buscar vídeos via fetch
async function buscarVideos(termo) {
    if (!termo) {
        limparResultados();
        return;
    }

    resultsDiv.textContent = "Loading...";

    try {
        const response = await fetch(`/search?q=${encodeURIComponent(termo)}`);
        const data = await response.json();
        exibirResultados(data.results);
    } catch (err) {
        resultsDiv.textContent = "Error searching for videos.";
        console.error(err);
    }
}

// Evento de submissão do formulário
form.addEventListener("submit", (e) => {
    e.preventDefault();
    const termo = input.value.trim();
    buscarVideos(termo);
});
