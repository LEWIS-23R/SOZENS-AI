const API_URL = "http://127.0.0.1:8000/analysis";

async function loadAnalysis() {
    try {

        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Could not connect to SOZENS AI Backend.");
        }

        const data = await response.json();

        // Top Cards
        document.getElementById("pair").textContent =
            data.pair ?? "--";

        document.getElementById("price").textContent =
            data.price ?? "--";

        document.getElementById("signal").textContent =
            data.signal ?? "--";

        document.getElementById("confidence").textContent =
            data.confidence ? `${data.confidence}%` : "--";

        // Trade Setup
        document.getElementById("entry").textContent =
            data.entry ?? "--";

        document.getElementById("sl").textContent =
            data.stop_loss ?? "--";

        document.getElementById("tp").textContent =
            data.take_profit ?? "--";

        document.getElementById("rr").textContent =
            data.risk_reward ?? "--";

        // AI Reasoning
        document.getElementById("reason").textContent =
            data.reason ?? "No reasoning available.";

    } catch (error) {

        alert(error.message);
        console.error(error);

    }
}

// Automatically load analysis when the page opens
window.onload = loadAnalysis;