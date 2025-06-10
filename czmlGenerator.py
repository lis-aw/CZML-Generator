from datetime import datetime, timedelta, timezone
from skyfield.api import EarthSatellite, load
from poliastro.bodies import Earth
from poliastro.twobody import Orbit
from astropy import units as u
from astropy.time import Time
from poliastro.czml.extract_czml import CZMLExtractor
import json
import os

def load_orbit_from_tle(name, tle1, tle2, ts, target_time):
    sat = EarthSatellite(tle1, tle2, name, ts)
    geocentric = sat.at(target_time)
    r = geocentric.position.km
    v = geocentric.velocity.km_per_s
    epoch = Time(target_time.utc_datetime())
    return Orbit.from_vectors(Earth, r * u.km, v * u.km / u.s, epoch=epoch)

def main():
    try:
        print("Start CZML generation for three satellites over 12 hours from now...")

        # Set timescale
        ts = load.timescale()

        # Get current UTC time and +12 hours
        now = datetime.now(timezone.utc)
        now_ts = ts.utc(now)
        twelve_hours_later_ts = ts.utc(now + timedelta(hours=12))

        # Satellite 1 - NOAA18
        name1 = "NOAA18"
        tle1_line1 = "1 28654U 05018A   25139.17554799  .00000232  00000+0  14650-3 0  9991"
        tle1_line2 = "2 28654  98.8420 218.8920 0014228 185.7099 174.3913 14.13599782 30723"
        orbit1 = load_orbit_from_tle(name1, tle1_line1, tle1_line2, ts, now_ts)

        # Satellite 2 - NOAA19
        name2 = "NOAA19"
        tle2_line1 = "1 33591U 09005A   25139.17854087  .00000215  00000+0  13832-3 0  9992"
        tle2_line2 = "2 33591  98.9980 203.7618 0014712  66.9650 293.3072 14.13363506839086"
        orbit2 = load_orbit_from_tle(name2, tle2_line1, tle2_line2, ts, now_ts)

        # Satellite 3 - NOAA15
        name3 = "NOAA15"
        tle3_line1 = "1 25338U 98030A   25139.49551384  .00000209  00000+0  10343-3 0  9994"
        tle3_line2 = "2 25338  98.5363 165.1330 0011359  64.8959 295.3400 14.26967244405395"
        orbit3 = load_orbit_from_tle(name3, tle3_line1, tle3_line2, ts, now_ts)

        # Set start and end epoch for 12-hour period
        start_epoch = Time(now)
        end_epoch = Time(now + timedelta(hours=12))
        N = 300  # Increase for better resolution

        extractor = CZMLExtractor(start_epoch, end_epoch, N)

        # Add orbits
        extractor.add_orbit(
            orbit1,
            id_name="NOAA18",
            id_description="NOAA 18",
            path_width=2,
            path_color=[255, 100, 50, 255],
            label_text="NOAA18",
            label_fill_color=[200, 80, 120, 255],
            groundtrack_show=True
        )

        extractor.add_orbit(
            orbit2,
            id_name="NOAA19",
            id_description="NOAA 19",
            path_width=2,
            path_color=[50, 200, 255, 255],
            label_text="NOAA19",
            label_fill_color=[60, 200, 150, 255],
            groundtrack_show=True
        )

        extractor.add_orbit(
            orbit3,
            id_name="NOAA15",
            id_description="NOAA 15",
            path_width=2,
            path_color=[50, 200, 255, 255],
            label_text="NOAA15",
            label_fill_color=[60, 200, 150, 255],
            groundtrack_show=True
        )

        # Serialize and save
        packets = extractor.packets
        serial = [json.loads(p.dumps()) for p in packets]

        filename = "three_satellites_12hr.czml"
        with open(filename, "w") as f:
            json.dump(serial, f, indent=2)

        print(f"✅ CZML-File '{filename}' for 12 hours has been created.")
        print("📁 Current directory:", os.getcwd())
        print("📄 Files in this directory:", os.listdir())

    except Exception as e:
        print("❌ ERROR:", e)

if __name__ == "__main__":
    main()
