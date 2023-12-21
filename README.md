# Metadata context converter

This is a script to convert custom OpenNMS metadata records to comply with the requirement for custom contexts to start with `X-`

## Running the script

By default the script will attempt to connect to Meridian/Horizon instance running on the localhost with default credentials.
If you would like to customize the server and credentials, you can either modify the script or create a `.env` file and set `onms_host`, `onms_user`, and `onms_pass` environment variables prior to running the script.

```py
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade -r requirements.txt
python3 metadata_convert.py
```
