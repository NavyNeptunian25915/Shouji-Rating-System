import streamlit as st
import streamlit.components.v1 as components

html_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shouji Rating System V4</title>
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
            border-color: #ff00ff;
            box-shadow: 0 0 20px #ff00ff;
            text-shadow: 0 0 20px #ff00ff;
            color: #ff00ff;
        }
                
        .Cchart {
            border-color: #ffff00;
            box-shadow: 0 0 20px #ffff00;
            text-shadow: 0 0 20px #ffff00;
            color: #ffff00;
        }

        .chart h2 {
            font-size: 1.5rem;
            margin-top: 0;
        }
        input[type="range"],
        #alphaValue[type="range"] {
            -webkit-appearance: none;
            width: 100%;
            max-width: 200px;
            height: 8px;
            background: #000064;
            border-radius: 5px;
            box-shadow: 0 0 10px #ffffff;
            outline: none;
            margin: 10px 0 20px 0;
            cursor: pointer;
        }
        input[type="range"]::-webkit-slider-thumb,
        #alphaValue[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 20px;
            height: 20px;
            background-color: #ffffff;
            border: 2px solid #000064;
            border-radius: 50%;
            box-shadow: 0 0 8px #ffffff;
            cursor: pointer;
            margin-top: -6px;
            transition: box-shadow 0.3s ease;
            position: relative;
            z-index: 1;
        }
        input[type="range"]:hover::-webkit-slider-thumb,
        #alphaValue[type="range"]:hover::-webkit-slider-thumb {
            box-shadow: 0 0 12px #ffffff;
        }
        input[type="range"]::-moz-range-thumb,
        #alphaValue[type="range"]::-moz-range-thumb {
            width: 20px;
            height: 20px;
            background-color: #ffffff;
            border: 2px solid #000064;
            border-radius: 50%;
            box-shadow: 0 0 8px #ffffff;
            cursor: pointer;
            transition: box-shadow 0.3s ease;
            position: relative;
            z-index: 1;
        }
        input[type="range"]:hover::-moz-range-thumb,
        #alphaValue[type="range"]:hover::-moz-range-thumb {
            box-shadow: 0 0 12px #ffffff;
        }
        /* For Firefox track styling */
        input[type="range"]::-moz-range-track,
        #alphaValue[type="range"]::-moz-range-track {
            background: #000064;
            border-radius: 5px;
            box-shadow: 0 0 10px #ffffff;
            height: 8px;
        }
        /* For IE */
        input[type="range"]::-ms-fill-lower,
        input[type="range"]::-ms-fill-upper,
        #alphaValue[type="range"]::-ms-fill-lower,
        #alphaValue[type="range"]::-ms-fill-upper {
            background: #000064;
            border-radius: 5px;
            box-shadow: 0 0 10px #ffffff;
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
        .textB {color: magenta; background-color:#640064;}
        .textC {color: yellow; background-color:#646400;}

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
            color: #ff00ff;
            border: 1px solid #ff00ff;
            background-color:#640064;
            box-shadow:#ff00ff 0 0 5vmin;
            text-shadow:#ff00ff 0 0 5vmin;
        }

        .results #newC {
            font-size:1rem;
            color: #ffff00;
            border: 1px solid #ffff00;
            background-color:#646400;
            box-shadow:#ffff00 0 0 5vmin;
            text-shadow:#ffff00 0 0 5vmin;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Shouji Rating System V4</h1>
        <p>A multiplayer version, really!?</p>

        <div class="chart-container">
            <div class="chart Achart">
                <h2>Player A</h2>
                <label for="ratingA">Rating</label>
                <input type="number" id="ratingA" value="1500">
                <label for="deviationA">Deviation</label>
                <input type="range" id="deviationA" value="0.64" min="0" max="1" step="0.01">
                <label for="volatilityA">Volatility</label>
                <input type="range" id="volatilityA" value="0" min="-1" max="1" step="0.01">
                <p id="newratingA">New Rating for Player A: 1500</p>
                <p id="newdeviationA">New Deviation for Player A: 0.64</p>
            </div>

            <div class="chart Bchart">
                <h2>Player B</h2>
                <label for="ratingB">Rating</label>
                <input type="number" id="ratingB" value="1500">
                <label for="deviationB">Deviation</label>
                <input type="range" id="deviationB" value="0.64" min="0" max="1" step="0.01">
                <label for="volatilityB">Volatility</label>
                <input type="range" id="volatilityB" value="0" min="-1" max="1" step="0.01">
                <p id="newratingB">New Rating for Player B: 1500</p>
                <p id="newdeviationB">New Deviation for Player B: 0.64</p>
            </div>

            <div class="chart Cchart">
                <h2>Player C</h2>
                <label for="ratingC">Rating</label>
                <input type="number" id="ratingC" value="1500">
                <label for="deviationC">Deviation</label>
                <input type="range" id="deviationC" value="0.64" min="0" max="1" step="0.01">
                <label for="volatilityC">Volatility</label>
                <input type="range" id="volatilityC" value="0" min="-1" max="1" step="0.01">
                <p id="newratingC">New Rating for Player C: 1500</p>
                <p id="newdeviationC">New Deviation for Player C: 0.64</p>
            </div>
        </div>

        <div class="score-select-wrapper">
            <label for="ratingvariationvalue">Variation:</label>
            <input type="number" id="ratingvariationvalue" value="400">
            <label for="alphaValue">Scale:</label>
            <input type="range" id="alphaValue" value="0.5" min="0" max="1" step="0.01">
            <label for="rhoValue">Decay:</label>
            <input type="range" id="rhoValue" value="0.5" min="0" max="1" step="0.01">
            <label for="winnerSelect">Winner:</label>
            <select id="winnerSelect">
                <option class="textA" value="0">Player A</option>
                <option class="textB" value="1">Player B</option>
                <option class="textC" value="2">Player C</option>
            </select>
        </div>
    </div>

    <script>
        const ratingvariationInput = document.getElementById("ratingvariationvalue");
        const alphaInput = document.getElementById("alphaValue");
        const rhoInput = document.getElementById("rhoValue");
        const winnerSelect = document.getElementById("winnerSelect");
        
        // Player A inputs
        const ratingAInput = document.getElementById("ratingA");
        const deviationAInput = document.getElementById("deviationA");
        const volatilityAInput = document.getElementById("volatilityA");
        const newratingAParagraph = document.getElementById("newratingA");
        const newdeviationAParagraph = document.getElementById("newdeviationA");
        
        // Player B inputs
        const ratingBInput = document.getElementById("ratingB");
        const deviationBInput = document.getElementById("deviationB");
        const volatilityBInput = document.getElementById("volatilityB");
        const newratingBParagraph = document.getElementById("newratingB");
        const newdeviationBParagraph = document.getElementById("newdeviationB");
        
        // Player C inputs
        const ratingCInput = document.getElementById("ratingC");
        const deviationCInput = document.getElementById("deviationC");
        const volatilityCInput = document.getElementById("volatilityC");
        const newratingCParagraph = document.getElementById("newratingC");
        const newdeviationCParagraph = document.getElementById("newdeviationC");

        function calculateRating() {
            const muA = parseFloat(ratingAInput.value) || 1500;
            const muB = parseFloat(ratingBInput.value) || 1500;
            const muC = parseFloat(ratingCInput.value) || 1500;
            
            const phiA = parseFloat(deviationAInput.value) || 0.64;
            const phiB = parseFloat(deviationBInput.value) || 0.64;
            const phiC = parseFloat(deviationCInput.value) || 0.64;
            
            const sigmaA = parseFloat(volatilityAInput.value) || 0;
            const sigmaB = parseFloat(volatilityBInput.value) || 0;
            const sigmaC = parseFloat(volatilityCInput.value) || 0;
            
            const winner = parseInt(winnerSelect.value);
            const resultA = winner === 0 ? 1 : 0;
            const resultB = winner === 1 ? 1 : 0;
            const resultC = winner === 2 ? 1 : 0;
            
            const beta = parseFloat(ratingvariationInput.value) || 400;
            const alpha = parseFloat(alphaInput.value) || 0.5;
            const rho = parseFloat(rhoInput.value) || 0.5;

            // Input validation
            if (muA < 1 || muB < 1 || muC < 1 || beta < 1) {
                newratingAParagraph.textContent = "Please enter valid values.";
                newratingBParagraph.textContent = "Please enter valid values.";
                newratingCParagraph.textContent = "Please enter valid values.";
                newdeviationAParagraph.textContent = "Please enter valid values.";
                newdeviationBParagraph.textContent = "Please enter valid values.";
                newdeviationCParagraph.textContent = "Please enter valid values.";
                return;
            }

            // Calculate T (Τ) for each player
            const TA = muA / (muA * phiA + muA);
            const TB = muB / (muB * phiB + muB);
            const TC = muC / (muC * phiC + muC);

            // Calculate C (ℂ) - mean of all deviations and T values * beta
            const C = ((phiA + phiB + phiC + TA + TB + TC) / 6) * beta;

            // Calculate adjusted ratings (ʃ) for each player
            const As = Math.pow(muA, (phiA + TA) / 2);
            const Bs = Math.pow(muB, (phiB + TB) / 2);
            const Cs = Math.pow(muC, (phiC + TC) / 2);

            // Calculate expected scores (ᐤ) for each player
            // Aᐤ = (2/3)/(1 + exp((mean(B, C) - A)/C))
            const meanOthersA = (muB + muC) / 2;
            const Ap = (2 / 3) / (1 + Math.exp((meanOthersA - muA) / C));

            const meanOthersB = (muA + muC) / 2;
            const Bp = (2 / 3) / (1 + Math.exp((meanOthersB - muB) / C));

            const meanOthersC = (muA + muB) / 2;
            const Cp = (2 / 3) / (1 + Math.exp((meanOthersC - muC) / C));

            // Calculate new ratings
            const newMuA = muA + Math.pow(As, alpha) * (resultA - Ap) + Math.pow(As, alpha) * sigmaA;
            const newMuB = muB + Math.pow(Bs, alpha) * (resultB - Bp) + Math.pow(Bs, alpha) * sigmaB;
            const newMuC = muC + Math.pow(Cs, alpha) * (resultC - Cp) + Math.pow(Cs, alpha) * sigmaC;

            // Calculate new deviations
            const newPhiA = Math.pow(phiA * rho, 1 - Math.abs(sigmaA));
            const newPhiB = Math.pow(phiB * rho, 1 - Math.abs(sigmaB));
            const newPhiC = Math.pow(phiC * rho, 1 - Math.abs(sigmaC));

            // Update the text content of the result elements
            newratingAParagraph.textContent = `New Rating for Player A: ${newMuA.toFixed(15)}`;
            newdeviationAParagraph.textContent = `New Deviation for Player A: ${newPhiA.toFixed(15)}`;
            newratingBParagraph.textContent = `New Rating for Player B: ${newMuB.toFixed(15)}`;
            newdeviationBParagraph.textContent = `New Deviation for Player B: ${newPhiB.toFixed(15)}`;
            newratingCParagraph.textContent = `New Rating for Player C: ${newMuC.toFixed(15)}`;
            newdeviationCParagraph.textContent = `New Deviation for Player C: ${newPhiC.toFixed(15)}`;
        }

        // Add event listeners to trigger the calculation when inputs change
        ratingvariationInput.addEventListener("change", calculateRating);
        alphaInput.addEventListener("change", calculateRating);
        rhoInput.addEventListener("change", calculateRating);
        winnerSelect.addEventListener("change", calculateRating);
        
        // Player A listeners
        ratingAInput.addEventListener("input", calculateRating);
        deviationAInput.addEventListener("input", calculateRating);
        volatilityAInput.addEventListener("input", calculateRating);
        
        // Player B listeners
        ratingBInput.addEventListener("input", calculateRating);
        deviationBInput.addEventListener("input", calculateRating);
        volatilityBInput.addEventListener("input", calculateRating);
        
        // Player C listeners
        ratingCInput.addEventListener("input", calculateRating);
        deviationCInput.addEventListener("input", calculateRating);
        volatilityCInput.addEventListener("input", calculateRating);
        
        // Initial calculation on page load
        calculateRating();
    </script>
</body>
</html>
"""

components.html(html_string, height=1664, width=2560, scrolling=True)
