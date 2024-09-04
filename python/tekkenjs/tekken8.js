
axios.get("https://github.com/BanAaron/tekken-backend.git").then(response => {
    console.log(response);
    console.log(response.status);
});