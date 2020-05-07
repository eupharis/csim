# Satnogs API Downloader and Parser for CSIM Satellite

`download_and_parse.py` will download and parse telemetry for the CSIM Satellite

[CSIM Satellite on Satnogs](https://db.satnogs.org/satellite/43793/)

The `.ksy` file defines how the raw bytes from the satellite should be parsed. It comes from the above page.

You will need to [install Kaitai](https://kaitai.io/#download) before running this script.

You will also need to signup and get an api key from Satnogs to run the script.

Once you have kaitai installed and your api key, run the script like so:

`SATNOGS_API_KEY=qew923j41n13 download_and_parse.py`
