const API = "http://127.0.0.1:5000";

const image = document.getElementById("image");
const prediction = document.getElementById("prediction");
const actual = document.getElementById("actual");
const status = document.getElementById("status");

const button = document.getElementById("generateBtn");

async function generatePrediction() {

    try {

        const response = await fetch(`${API}/predict`);

        if (!response.ok) {
            throw new Error("Failed to fetch prediction.");
        }

        const data = await response.json();

        image.src = data.image_url;

        prediction.textContent = data.prediction;

        actual.textContent = data.actual;

        status.textContent = data.correct
            ? "✅ Correct Prediction"
            : "❌ Incorrect Prediction";

    }

    catch (error) {

        console.error(error);

        alert("Cannot connect to Flask Backend.");

    }

}

button.addEventListener("click", generatePrediction);

// Load one image automatically when page opens
generatePrediction();