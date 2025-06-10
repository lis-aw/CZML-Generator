# cesium-satellite-simulation
Simulate the orbits of your satellites of choice within Cesium Sandcastle - a free alternative to MatLab SatCom Toolbox.

Cesium is an open-source JavaScript library for creating 3D globes and maps in a web browser. It lets you visualize geospatial data in real time with high precision, often used for satellites, terrain, and time-dynamic simulations. It runs on WebGL and requires no plugins.

Cesium Sandcastle is an online code editor provided by CesiumJS that lets you write, run, and test Cesium code directly in your browser.

🔹 Key Features:
- Live editing and preview of 3D scenes

- Dozens of example templates to learn from

- Instant feedback with console output

- Great for prototyping with CesiumJS

🔗 URL:
You can try it here: https://sandcastle.cesium.com/

It's mainly a learning and experimentation environment—perfect for testing CZML, entity styling, time-dynamic visualizations, or CesiumJS API features.

In this project it is used to visualize the orbits of custom satellites. The cesiumSandcastle.js file can be pasted directly into the Sandcastle JavaScript Tab. The included satellites are NOAA 15, 18 and 19 on Jun 10 for 12 hours.

The czmlGenerator.py file lets you generate your own czml file for your own preferred satellites. CZML is a type of JSON file that is used by the Sandcastle to draw the orbits of satellites, positions of ground stations etc.
The Python Script will generate the fitting CZML for chosen TLE's you can get from Celestrak. 

For the script to work you need poliastro, skyfield, astropy
