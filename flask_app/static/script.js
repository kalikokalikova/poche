console.log("poop")

async function translateMe(e) {
    e.preventDefault(); // Stop the page from refreshing and sending the data

    var term = document.getElementById('term-to-translate').value
    console.log(term)
    // TODO validations on the search term, non-empty, string, ect.

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
    result = await res.json();
    // TODO put in some kind of waiting messaging, perhaps a party cat?

    // ??? Will it ever be the case that this object tries to populate with results that haven't arrived yet?
    translationData = {
        en: term,
        fr: result.translatedText
    };
    populateForm(translationData);
};

function populateForm(translationData) {
    // TODO this div will be hidden by default and be shown when form is populated
    document.getElementById("result-div").style.display = "block";
    document.getElementById("term-to-translate").value = "";
    document.getElementById("english").value = translationData.en;
    document.getElementById("french").value = translationData.fr;
};

function activateSave() {
    button = document.getElementsByClassName("save-term")[0];
    console.log(button);
};