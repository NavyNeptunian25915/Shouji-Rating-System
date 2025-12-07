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
        html, body {
            height: 100%;
            margin: 0;
            padding: 0;
            overflow: hidden; /* Prevent scroll inside iframe */
        }

        body {
            font-family: 'Orbitron', sans-serif;
            text-align: center;
            background: #000064;
            color: #ffffff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
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
            width: 100%;
            max-width: 350px;
        }

        .Achart {
            border-color: Cyan;
            box-shadow: 0 0 20px Cyan;
            color: Cyan;
        }

        .Bchart {
            border-color: #ff0000;
            box-shadow: 0 0 20px Red;
            color: #ff0000;
        }

        input[type="number"], select {
            font-family: 'Orbitron', sans-serif;
            text-align: center;
            background: #000064;
            color: #ffffff;
            border: 1px solid #ffffff;
            border-radius: 5px;
            padding: 10px;
            margin: 10px auto 20px;
            width: 100%;
            max-width: 200px;
        }

        .score-select-wrapper {
            margin-top: 40px;
            padding: 20px;
            background: rgba(0, 0, 100, 0.5);
            border-radius: 15px;
        }
    </style>
</head>
<body>
    <!-- Your full HTML stays the same -->
    REPLACE_THIS_WITH_YOUR_ORIGINAL_HTML_CONTENT
</body>
</html>
"""

components.html(html_string, height=None, scrolling=False)
