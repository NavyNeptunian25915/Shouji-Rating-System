import streamlit as st
import streamlit.components.v1 as components

html_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shouji Rating System V3.2</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400..900&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Orbitron', sans-serif;
            text-align: center;
            background: #000064;
            color: #ffffff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
            gap: 50px;
        }

        .container {
            width: 100%;
            max-width: 900px;
        }

        h1 {
            font-size: 3rem;
            text-shadow: 0 0 20px #ffffff;
            font-weight:1000;
        }

        .chart-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 40px;
            flex-wrap: wrap;
        }

        .chart {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 30px;
            border: 1px solid;
            border-radius: 20px;
            background: rgba(0, 0, 100, 0.5);
            box-shadow: 0 0 20px;
            transition: all 0.3s ease;
            width: 100%;
            max-width: 350px;
        }

        .chart:hover {
            transform: translateY(-5px);
        }

        .Achart {
            border-color: Cyan;
            box-shadow: 0 0 20px Cyan;
            text-shadow: 0 0 20px Cyan;
            color: Cyan;
        }

        .Bchart {
            border-color: #ff0000;
            box-shadow: 0 0 20px Red;
            text-shadow: 0 0 20px #ff0000;
            color: #ff0000;
        }

        .chart h2 {
            font-size: 1.5rem;
            margin-top: 0;
        }

        input[type="number"],
        select {
            font-family: 'Orbitron', sans-serif;
            text-align: center;
            background: #000064;
            color: #ffffff;
            border: 1px solid #ffffff;
            border-radius: 5px;
            box-shadow: 0 0 10px #ffffff;
            padding: 10px;
            margin-top: 10px;
            margin-bottom: 20px;
            width: 100%;
            max-width: 200px;
            box-sizing: border-box;
            transition: box-shadow 0.3s ease;
        }

        input[type="number"]:focus,
        select:focus {
            outline: none;
            box-shadow: 0 0 15px #ffffff;
        }

        .score-select-wrapper {
            margin-top: 40px;
            padding: 20px;
            background: rgba(0, 0, 100, 0.5);
            border-radius: 15px;
            box-shadow: 0 0 15px #ffffff;
        }
        .textA {color: cyan; background-color:#006464;}
        .textDraw {color: white; background-color:#646464;}
        .textB {color: red; background-color:#640000;}

        .results p {
            font-size: 1.4rem;
            word-wrap: break-word;
            padding: 10px;
            border-radius: 5px;
            margin: 15px auto;
            max-width: 400px;
            background: rgba(255, 255, 255, 0.1);
        }

        .results #newA {
            font-size:1rem;
            color: Cyan;
            border: 1px solid Cyan;
            background-color:#006464;
            box-shadow:Cyan 0 0 5vmin;
            text-shadow:Cyan 0 0 5vmin;

        }

        .results #newB {
            font-size:1rem;
            color: #ff0000;
            border: 1px solid #ff0000;
            background-color:#640000;
            box-shadow:#ff0000 0 0 5vmin;
            text-shadow:#ff0000 0 0 5vmin;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Shouji Rating System V3.2</h1>
        <p>Last one was a lie, but that one is still robust.</p>

        <div class="chart-container">
            <div class="chart Achart">
                <h2>Player A</h2>
                <label for="ratingA">Rating</label>
                <input type="number" id="ratingA" value="1500">
                <label for="deviationA">Deviation</label>
                <input type="number" id="deviationA" value="0.64" min="0.01" max="1" step="0.01">
                <label for="volatilityA">Volatility</label>
                <input type="number" id="volatilityA" value="0" min="-1" max="1" step="0.01">
                <p id="newratingA">New Rating for Player A: 1500</p>
                <p id="newdeviationA">New Deviation for Player A: 0.64</p>
            </div>

            <div class="chart Bchart">
                <h2>Player B</h2>
                <label for="ratingB">Rating</label>
                <input type="number" id="ratingB" value="1500">
                <label for="deviationB">Deviation</label>
                <input type="number" id="deviationB" value="0.64" min="0.01" max="1" step="0.01">
                <label for="volatilityB">Volatility</label>
                <input type="number" id="volatilityB" value="0" min="-1" max="1" step="0.01">
                <p id="newratingB">New Rating for Player B: 1500</p>
                <p id="newdeviationB">New Deviation for Player B: 0.64</p>
            </div>
        </div>

        <div class="score-select-wrapper">
            <label for="ratingvariationvalue">Rating Variation:</label>
            <input type="number" id="ratingvariationvalue" value="400">
            <label for="Score">Game Result:</label>
            <select id="Score">
                <option class="textA" value="1">Player A</option>
                <option class="textDraw"value="0.5">Draw</option>
                <option class="textB" value="0">Player B</option>
            </select>
        </div>
    </div>

    <script>
        const scoreSelect = document.getElementById("Score");
        const ratingvariationImput = document.getElementById("ratingvariationvalue");
        const ratingAInput = document.getElementById("ratingA");
        const deviationAInput = document.getElementById("deviationA");
        const volatilityAInput = document.getElementById("volatilityA");
        const ratingBInput = document.getElementById("ratingB");
        const deviationBInput = document.getElementById("deviationB");
        const volatilityBInput = document.getElementById("volatilityB");
        const newratingAParagraph = document.getElementById("newratingA");
        const newratingBParagraph = document.getElementById("newratingB");
        const newdeviationAParagraph = document.getElementById("newdeviationA");
        const newdeviationBParagraph = document.getElementById("newdeviationB");

        function calculateRating() {
            const playerArating = parseFloat(ratingAInput.value) || 1500;
            const playerBrating = parseFloat(ratingBInput.value) || 1500;
            const playerAdeviation = parseFloat(deviationAInput.value) || 0.64;
            const playerBdeviation = parseFloat(deviationBInput.value) || 0.64;
            const playerAvolatility = parseFloat(volatilityAInput.value) || 0;
            const playerBvolatility = parseFloat(volatilityBInput.value) || 0;
            const score = parseFloat(scoreSelect.value);
            const ratingvariation = parseFloat(ratingvariationImput.value) || 400;

            if (playerArating <= 0 || playerBrating <= 0 || playerAdeviation <= 0 || playerBdeviation <= 0 || playerAdeviation > 1 || playerBdeviation > 1 || playerAvolatility < -1 || playerBvolatility < -1 || playerAvolatility > 1 || playerBvolatility > 1) {
                newratingAParagraph.textContent = "Please enter valid ranged ratings, deviations, volatilities.";
                newratingBParagraph.textContent = "Please enter valid ranged ratings, deviations, volatilities.";
                newdeviationAParagraph.textContent = "Please enter valid ranged ratings, deviations, volatilities.";
                newdeviationBParagraph.textContent = "Please enter valid ranged ratings, deviations, volatilities.";
                return;
            }

            // Calculate stability for both players
            const stabilityA = playerArating / ((playerArating ** playerAdeviation) + playerArating);
            const stabilityB = playerBrating / ((playerBrating ** playerBdeviation) + playerBrating);

            // Calculate fluctuations
            const fluctuations = ((playerAdeviation * playerBdeviation * stabilityA * stabilityB) ** 0.25) * ratingvariation;

            // Calculate prediction
            const prediction = 1 / (1 + 10 ** ((playerBrating - playerArating) / fluctuations));

            // Calculate factors for updating ratings
            const factorA = (playerArating ** playerAdeviation) ** stabilityA;
            const factorB = (playerBrating ** playerBdeviation) ** stabilityB;

            // Calculate new ratings
            const newArating = playerArating + factorA * (score - prediction) + factorA * playerAvolatility;
            const newBrating = playerBrating + factorB * ((1 - score) - (1 - prediction)) + factorB * playerBvolatility;

            // Calculate new deviations
            const newAdeviation = (playerAdeviation * stabilityA) ** (1 - Math.abs(playerAvolatility));
            const newBdeviation = (playerBdeviation * stabilityB) ** (1 - Math.abs(playerBvolatility));

            // Update the text content of the result elements
            newratingAParagraph.textContent = `New Rating for Player A: ${newArating.toFixed(0)}`;
            newdeviationAParagraph.textContent = `New Deviation for Player A: ${newAdeviation.toFixed(2)}`;
            newratingBParagraph.textContent = `New Rating for Player B: ${newBrating.toFixed(0)}`;
            newdeviationBParagraph.textContent = `New Deviation for Player B: ${newBdeviation.toFixed(2)}`;
        }

        // Add event listeners to trigger the calculation when inputs change
        ratingvariationImput.addEventListener("change", calculateRating);
        scoreSelect.addEventListener("change", calculateRating);
        ratingAInput.addEventListener("input", calculateRating);
        deviationAInput.addEventListener("input", calculateRating);
        volatilityAInput.addEventListener("input", calculateRating);
        ratingBInput.addEventListener("input", calculateRating);
        deviationBInput.addEventListener("input", calculateRating);
        volatilityBInput.addEventListener("input", calculateRating);
        
        // Initial calculation on page load
        calculateRating();
    </script>
</body>
</html>
"""

components.html(html_string, height=None, scrolling=True) 
