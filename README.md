# Open-Source Satellite Orbit Visualizations using CZML Generator and Cesium

<img src="https://github.com/lis-aw/CZML-Generator/blob/main/ScreenshotCesium.png" alt="CesiumSandbox Satellite Orbit Visualization" width="70%">

## ✅ What it is:
I created this project when I was looking for an open-source alternative to MatLab and it's SatCom Toolbox for visualizing orbits.
So with the files in this repo you can simulate the orbits of your satellites of choice by generating CZML files to be used within Cesium Sandcastle - (a free alternative to the MatLab SatCom Toolbox).

Cesium is an open-source JavaScript library for creating 3D globes and maps in a web browser. It lets you visualize geospatial data in real time, often used for satellites, terrain, and time-dynamic simulations. Cesium Sandcastle is an online code editor provided by CesiumJS that lets you write, run, and test Cesium code directly in your browser.

🔗 URL:
You can try it here: https://sandcastle.cesium.com/

The Sandcastle is mainly a learning and experimentation environment—perfect for testing CZML and entity styling. In this project it is used to visualize the orbits of custom satellites.

## ✅ How to use this Repo:
- Download the zip of the files in this repository and unpack
- Go to https://sandcastle.cesium.com/
- Paste the contents of the cesiumSandcastle.js file directly into the Sandcastle JavaScript Tab. The included satellites are NOAA 15, 18 and 19 on Jun 10 for 12 hours. This is an example. The contents of `const czml` can be replaced with custom CZML. CZML is a type of JSON file that is used by Sandcastle to draw the orbits of satellites, positions of ground stations etc.
- The czmlGenerator.py file lets you generate your own CZML file for your own preferred satellites. The Python Script will generate the fitting CZML for chosen TLE's you can get from Celestrak [URL: https://celestrak.org/NORAD/elements/gp.php?GROUP=weather&FORMAT=tle (current TLE's of all common weather satellites)]



## 🛰️ Using the czmlGenerator.py for creating CZML of Satellite Orbits

This script generates a CZML file visualizing the orbits of three (ofc you can change how many by changing the code) satellites over a 12-hour period using. You need to manually input the TLE's of the satellites you want the orbits of; you can use Celestrak to get the TLE's: https://celestrak.org/NORAD/elements/gp.php?GROUP=weather&FORMAT=tle 
The script uses multiple special libraries: `poliastro: 0.17.0 | skyfield: 1.53 | astropy: 5.2.2 | czml3: 0.7.0`
Especially poliastro needs a lot of specific dependencies, therefore it's not easily done the regular way. The following section describes the recommended way to get all dependencies right and get the script running, by using conda :)

## ✅ Setup Instructions (for running the czmlGenerator.py)

### 1. Install Miniconda (if you haven't already)
Download Miniconda from:  
🔗 https://docs.conda.io/projects/conda/en/stable/

### 2. Create and activate the environment
Open a terminal and create a new conda environment:

```bash
conda create -n czml-env python=3.10.16
conda activate czml-env
```
It should now say "(czml-env)" to the left of your current path.

### 3. Install required packages

```bash
conda install -c conda-forge poliastro astropy skyfield
pip install czml3==0.7.0
```

> ⚠️ Note: Version `0.7.0` of `czml3` is required for compatibility with `poliastro`. For all others, the newest stable version should be fine, if something breaks, revert to the versions mentioned above.

---

## ▶️ Running the Script

Navigate into the folder containing the script and run it:

```bash
cd path/to/czmlGenerator
python czmlGenerator.py
```

You should see output like:

```
Start CZML generation for three satellites over 12 hours from now...
✅ CZML-File 'three_satellites_12hr.czml' for 12 hours has been created.
📁 Current directory: C:\Users\yourname\someOtherFolder\czmlGenerator
📄 Files in this directory: ['czmlGenerator.py', 'CesiumSanboxFileJS.js' , 'three_satellites_12hr.czml']
```

---

## 💻 Running from VS Code (Optional)
Maybe you are editing this file in VSCode and you don't want to type commands into the terminal to run the file. No problem, but for this to work you also have to create the conda environment first and install the packages. Then you can:

1. Open the folder containing `czmlGenerator.py` in VS Code.
2. Press `Ctrl+Shift+P` and search for **"Python: Select Interpreter"**.
3. Select the environment named **`czml-env`**.
4. To run: Click the dropdown next to the ▶️ **Run** button and choose **"Run Python File"**.
   > ⚠️ Running it with the regular Run button may not work due to environment issues.

---

## 📄 License

MIT License – feel free to use and adapt.
