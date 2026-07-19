function escapeHTML(text) {

    if (text === null || text === undefined) {
        return "";
    }

    return String(text)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

// ======================================================
// Risk Badge
// ======================================================

function getRiskBadge(risk) {

    let color = "#757575";

    switch ((risk || "").toLowerCase()) {

        case "high":
            color = "#e53935";
            break;

        case "moderate":
            color = "#fb8c00";
            break;

        case "low":
            color = "#43a047";
            break;

        case "very low":
            color = "#1e88e5";
            break;
    }

    return `
        <span
            style="
                background:${color};
                color:white;
                padding:6px 12px;
                border-radius:20px;
                font-size:13px;
                font-weight:bold;
            "
        >
            ${escapeHTML(risk)}
        </span>
    `;
}

// ======================================================
// Confidence Bar
// ======================================================

function confidenceBar(value) {

    value = Number(value);

    return `

        <div
            style="
                width:100%;
                background:#dfefff;
                border-radius:10px;
                overflow:hidden;
                margin-top:8px;
            "
        >

            <div
                style="
                    width:${value}%;
                    background:#1565c0;
                    color:white;
                    text-align:center;
                    padding:5px;
                    font-size:13px;
                    font-weight:bold;
                "
            >

                ${value.toFixed(1)}%

            </div>

        </div>

    `;
}

// ======================================================
// Loading
// ======================================================

function showLoading() {

    document.getElementById("loading").style.display = "block";

    document.getElementById("result").style.display = "none";

}

function hideLoading() {

    document.getElementById("loading").style.display = "none";

    document.getElementById("result").style.display = "block";

}

// ======================================================
// Main Function
// ======================================================

async function analyzeSymptoms() {

    const message = document
        .getElementById("symptoms")
        .value
        .trim();

    if (!message) {

        alert("Please enter your symptoms.");

        return;

    }

    showLoading();

    const resultDiv = document.getElementById("result");

    try {

        const response = await fetch("/analyze", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                message: message

            })

        });

        const data = await response.json();

        hideLoading();

        if (!data.success) {

            resultDiv.innerHTML = `

            <div class="card">

                <h2>❌ Error</h2>

                <p>${escapeHTML(data.error)}</p>

            </div>

            `;

            return;

        }

        const analysis = data.analysis;

        const predictions = data.predictions;

        const rag = data.rag;
                //--------------------------------------------------
        // Clinical NLP
        //--------------------------------------------------

        let symptomHTML = "";

        if (!analysis.symptoms || analysis.symptoms.length === 0) {

            symptomHTML = `

                <p>No clinical symptoms detected.</p>

            `;

        }

        else {

            analysis.symptoms.forEach(symptom => {

                symptomHTML += `

                <div class="symptom-card">

                    <h3>🩺 ${escapeHTML(symptom.name)}</h3>

                    <table>

                        <tr>

                            <td><b>Present</b></td>

                            <td>${symptom.present ? "✅ Yes" : "❌ No"}</td>

                        </tr>

                        <tr>

                            <td><b>Severity</b></td>

                            <td>${escapeHTML(symptom.severity)}</td>

                        </tr>

                        <tr>

                            <td><b>Confidence</b></td>

                            <td>

                                ${confidenceBar(symptom.confidence * 100)}

                            </td>

                        </tr>

                        <tr>

                            <td><b>SNOMED Code</b></td>

                            <td>${escapeHTML(symptom.ontology.code)}</td>

                        </tr>

                        <tr>

                            <td><b>Clinical Name</b></td>

                            <td>${escapeHTML(symptom.ontology.name)}</td>

                        </tr>

                    </table>

                </div>

                `;

            });

        }

        //--------------------------------------------------
        // Disease Prediction
        //--------------------------------------------------

        let predictionHTML = "";

        predictions.forEach((prediction, index) => {

            predictionHTML += `

            <div class="prediction-card">

                <h3>

                    ${index + 1}. ${escapeHTML(prediction.disease)}

                </h3>

                <table>

                    <tr>

                        <td><b>Confidence</b></td>

                        <td>

                            ${confidenceBar(prediction.confidence)}

                        </td>

                    </tr>

                    <tr>

                        <td><b>Risk Level</b></td>

                        <td>

                            ${getRiskBadge(prediction.risk)}

                        </td>

                    </tr>

                    <tr>

                        <td><b>Recommended Specialist</b></td>

                        <td>

                            👨‍⚕️ ${escapeHTML(prediction.recommended_specialist)}

                        </td>

                    </tr>

                    <tr>

                        <td><b>Description</b></td>

                        <td>

                            ${escapeHTML(prediction.description)}

                        </td>

                    </tr>

                </table>

            </div>

            `;

        });

        //--------------------------------------------------
        // Patient Summary Card
        //--------------------------------------------------

        const patientSummary = `

        <div class="card">

            <h2>👤 Patient Summary</h2>

            <hr><br>

            <table>

                <tr>

                    <td><b>Age</b></td>

                    <td>${analysis.age ?? "Not detected"}</td>

                </tr>

                <tr>

                    <td><b>Duration</b></td>

                    <td>${analysis.duration ?? "Not detected"}</td>

                </tr>

                <tr>

                    <td><b>Symptoms Found</b></td>

                    <td>${analysis.symptoms.length}</td>

                </tr>

            </table>

        </div>

        `;

        //--------------------------------------------------
        // Clinical NLP Card
        //--------------------------------------------------

        const clinicalCard = `

        <div class="card">

            <h2>🩺 Clinical NLP Analysis</h2>

            <hr><br>

            ${symptomHTML}

        </div>

        `;

        //--------------------------------------------------
        // Disease Prediction Card
        //--------------------------------------------------

        const predictionCard = `

        <div class="card">

            <h2>🤖 Disease Risk Prediction</h2>

            <hr><br>

            ${predictionHTML}

        </div>

        `;
                //--------------------------------------------------
        // AI Medical Explanation
        //--------------------------------------------------

        const aiCard = `

        <div class="card">

            <h2>🧠 AI Medical Explanation</h2>

            <hr><br>

            <div class="box">

                ${escapeHTML(rag.answer).replace(/\n/g,"<br>")}

            </div>

        </div>

        `;

        //--------------------------------------------------
        // Retrieved Knowledge
        //--------------------------------------------------

        let sourceHTML = "";

        if (rag.sources && rag.sources.length > 0) {

            rag.sources.forEach(source => {

                sourceHTML += `

                <tr>

                    <td>

                        📖 ${escapeHTML(source.disease)}

                    </td>

                    <td>

                        Chunk ${escapeHTML(source.chunk_id)}

                    </td>

                    <td>

                        ${escapeHTML(source.distance)}

                    </td>

                </tr>

                `;

            });

        }

        else {

            sourceHTML = `

            <tr>

                <td colspan="3">

                    No medical sources retrieved.

                </td>

            </tr>

            `;

        }

        const ragCard = `

        <div class="card">

            <h2>📚 Retrieved Medical Knowledge</h2>

            <hr><br>

            <table>

                <thead>

                    <tr>

                        <th>Disease</th>

                        <th>Chunk</th>

                        <th>Distance</th>

                    </tr>

                </thead>

                <tbody>

                    ${sourceHTML}

                </tbody>

            </table>

        </div>

        `;

        //--------------------------------------------------
        // Final Dashboard
        //--------------------------------------------------

        resultDiv.innerHTML =

            patientSummary +

            clinicalCard +

            predictionCard +

            aiCard +

            ragCard;

    }

    //--------------------------------------------------
    // Unexpected Error
    //--------------------------------------------------

    catch (error) {

        hideLoading();

        resultDiv.innerHTML = `

        <div class="card">

            <h2>❌ Unexpected Error</h2>

            <p>

                ${escapeHTML(error)}

            </p>

        </div>

        `;

        console.error(error);

    }

}

    