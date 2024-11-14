document.addEventListener("DOMContentLoaded", () => {
  fetch("szablon.html")
    .then((response) => response.text())
    .then((templateData) => {
      document.documentElement.innerHTML = templateData;

      fetch("artykul.html")
        .then((response) => response.text())
        .then((articleData) => {
          const contentDiv = document.getElementById("content");
          if (contentDiv) {
            contentDiv.innerHTML = articleData;
          } else {
            console.error("Nie znaleziono elementu #content w szablonie.");
          }
        })
        .catch((error) =>
          console.error("Błąd podczas wczytywania artykułu:", error)
        );
    })
    .catch((error) =>
      console.error("Błąd podczas wczytywania szablonu:", error)
    );
});
