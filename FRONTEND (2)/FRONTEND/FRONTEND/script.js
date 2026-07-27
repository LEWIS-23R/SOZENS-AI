<script>

async function loadAnalysis(){

    try{

        const response = await fetch("http://127.0.0.1:8000/analysis");

        const data = await response.json();

        document.getElementById("result").innerHTML = `

            <div class="card">

                <h2>${data.signal}</h2>

                <p><b>Pair:</b> ${data.pair}</p>

                <p><b>Price:</b> ${data.price}</p>

                <p><b>Trend:</b> ${data.trend}</p>

                <p><b>Confidence:</b> ${data.confidence}</p>

                <p><b>Entry:</b> ${data.entry}</p>

                <p><b>Stop Loss:</b> ${data.stop_loss}</p>

                <p><b>Take Profit:</b> ${data.take_profit}</p>

                <p><b>Risk Reward:</b> ${data.risk_reward}</p>

                <p><b>Reason:</b> ${data.reason}</p>

            </div>

        `;

    }

    catch(error){

        console.error(error);

        alert("Connection to FastAPI failed!");

    }

}

</script>