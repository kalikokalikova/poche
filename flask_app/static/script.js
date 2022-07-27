console.log("poop")

async function translateMe(e) {
    e.preventDefault(); // Stop the page from refreshing and sending the data

    var term = document.getElementById('term-to-translate').value
    console.log(term)

    const res = await fetch("https://libretranslate.com/translate", {
        method: "POST",
        body: JSON.stringify({
            q: term,
            source: "en",
            target: "fr",
            format: "text",
            api_key: "562895d5-7b5a-494a-81ec-5743c8220523"
        }),
        headers: { "Content-Type": "application/json" }

    });
    console.log(await res.json());
};

