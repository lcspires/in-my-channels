document.addEventListener("DOMContentLoaded", () => {
  const channelListEl = document.getElementById("channel-list");
  const videoListEl = document.getElementById("video-list");
  const searchForm = document.getElementById("search-form");
  const searchInput = document.getElementById("search-input");

  // Carregar lista de canais
  fetch("/subscriptions")
    .then(res => res.json())
    .then(data => {
      channelListEl.innerHTML = "";
      data.subscriptions.forEach(channel => {
        const li = document.createElement("li");
        li.textContent = channel.title;
        channelListEl.appendChild(li);
      });
    })
    .catch(err => {
      channelListEl.innerHTML = "<li>Erro ao carregar canais</li>";
      console.error(err);
    });

  // Buscar vídeos
  searchForm.addEventListener("submit", e => {
    e.preventDefault();
    const query = searchInput.value.trim();
    if (!query) return;

    fetch(`/search?q=${encodeURIComponent(query)}`)
      .then(res => res.json())
      .then(data => {
        videoListEl.innerHTML = "";
        if (data.results.length === 0) {
          videoListEl.innerHTML = "<li>Nenhum vídeo encontrado</li>";
          return;
        }

        data.results.forEach(video => {
          const li = document.createElement("li");
          li.innerHTML = `<strong>${video.title}</strong> <em>(${video.channel})</em>`;
          videoListEl.appendChild(li);
        });
      })
      .catch(err => {
        videoListEl.innerHTML = "<li>Erro na busca</li>";
        console.error(err);
      });
  });
});
