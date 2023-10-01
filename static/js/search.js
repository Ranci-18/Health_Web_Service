/* eslint-disable linebreak-style */
/* eslint-disable no-undef */
const searchButton = document.getElementById('searchButton');
const searchInput = document.getElementById('searchInput');
const searchResults = document.getElementById('searchResults');

searchButton.addEventListener('click', async () => {
  const symptom = searchInput.value;
  const response = await fetch('/search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ symptom }),
  });
  const data = await response.json();
  // Process and display data in searchResults
  // Example: display titles of articles
  searchResults.innerHTML = data.map((article) => `<p>${article.title}</p>`).join('');
});
