document.addEventListener("DOMContentLoaded", function () {
    console.log("DOM content loaded"); // Debugging statement

    const randomArtistButton = document.getElementById("randomArtistButton");

    randomArtistButton.addEventListener("click", function () {
        console.log("Button clicked!"); // Debugging statement

        // Fetch the maximum artist ID from your data source or API
        // For demonstration purposes, let's assume maxArtistId is fetched asynchronously
        fetchMaxArtistId().then((maxArtistId) => {
            // Generate a random artist_id within the range of available IDs
            const randomArtistId = Math.floor(Math.random() * maxArtistId) + 1;

            // Redirect to the artist_page with the random artist_id
            window.location.href = `/artist/${randomArtistId}`;
        }).catch((error) => {
            console.error("Error fetching max artist ID:", error); // Handle errors
        });
    });
});

// Function to fetch the maximum artist ID asynchronously (replace with your actual fetch logic)
function fetchMaxArtistId() {
    return new Promise((resolve, reject) => {
        // Simulate fetching the maximum artist ID (replace with your fetch logic)
        setTimeout(() => {
            const maxId = 9; // Replace 10 with the actual maximum artist ID
            resolve(maxId);
        }, 10); // Simulate 1 second delay for fetching
    });
}
