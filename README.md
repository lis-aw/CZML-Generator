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

F# 🚀 CZML Generator for Satellite Orbits

This script generates a CZML file visualizing the orbits of three satellites over a 12-hour period using [poliastro](https://www.poliastro.space/), [Skyfield](https://rhodesmill.org/skyfield/), and [czml3](https://github.com/poliastro/czml3). It outputs a file compatible with [CesiumJS](https://cesium.com/platform/cesiumjs/), useful for satellite orbit visualizations in 3D.

---
poliastro: 0.17.0
skyfield: 1.53
astropy: 5.2.2
czml3: 0.7.0

## ✅ Setup Instructions

### 1. Install Miniconda (if you haven't already)
Download Miniconda from:  
🔗 https://docs.conda.io/projects/conda/en/stable/

### 2. Create and activate the environment

```bash
conda create -n czml-env python=3.10.16
conda activate czml-env
```

### 3. Install required packages

```bash
conda install -c conda-forge poliastro astropy skyfield
pip install czml3==0.5.7
```

> ⚠️ Note: Version `0.5.7` of `czml3` is required for compatibility with `poliastro`.

---

## ▶️ Running the Script

Navigate into the folder containing the script:

```bash
cd path/to/czmlGenerator
python czmlGenerator.py
```

You should see output like:

```
Start CZML generation for three satellites over 12 hours from now...
✅ CZML-File 'three_satellites_12hr.czml' for 12 hours has been created.
📁 Current directory: C:\Users\lisam\IP-HRPT\czmlGenerator
📄 Files in this directory: ['czmlGenerator.py', 'requirements.txt', 'three_satellites_12hr.czml']
```

---

## 💻 Running from VS Code (Optional)

1. Open the folder containing `czmlGenerator.py` in VS Code.
2. Press `Ctrl+Shift+P` and search for **"Python: Select Interpreter"**.
3. Select the environment named **`czml-env`**.
4. Click the dropdown next to the ▶️ **Run** button and choose **"Run Python File"**.
   > ⚠️ Running it with the regular Run button may not work due to environment issues.

---

## 📦 Files in This Project

- `czmlGenerator.py` – Main script
- `three_satellites_12hr.czml` – Example output file
- `requirements.txt` – (Optional, for pip-based setup)

---

## 🛰️ Output

The output CZML file can be loaded into CesiumJS for a 3D orbit visualization of satellites over time.

---

## 📄 License

MIT License – feel free to use and adapt.
