# Satnogs API Downloader and Parser for CSIM Satellite

`download_and_parse.py` will download and parse telemetry for the CSIM Satellite

[CSIM Satellite on Satnogs](https://db.satnogs.org/satellite/43793/)

The `csim.ksy` file defines how the raw bytes from the satellite should be parsed. It is included in the repo and comes from the above page.

You will need to [install Kaitai](https://kaitai.io/#download) before running this script.

You will also need to signup and get an api key from Satnogs to run the script.

Here are the [docs for the Satnogs API](
https://docs.satnogs.org/projects/satnogs-db/en/stable/api.html). They are a bit sparse :)

I've found it more helpful to just look at the [Satnogs API Source Code](https://gitlab.com/librespacefoundation/satnogs/satnogs-db/-/blob/master/db/api/views.py)

Once you have kaitai installed and your api key, run the script like so:

`SATNOGS_API_KEY=qew923j41n13 download_and_parse.py`
