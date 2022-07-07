deleteItem = async () => {
    const response = await fetch(window.location, {method: "DELETE"})
    if (response.status === 200) {
        const data = await response.json()
        window.location = data.url || "/"
    }
}