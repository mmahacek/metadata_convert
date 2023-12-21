# Metadata context converter

As of Meridian 2023.1.11 and Horizon 32.0.6, the Nodes REST endpoint was updated to allow modification of metadata, with the caveat that only contexts starting with `X-` can be modified.
All other contexts are considered reserved for internal use.

This is a script to convert custom OpenNMS metadata records to comply with the requirement for custom contexts to start with `X-`.
Any existing metadata records on nodes, IP interfaces, and monitored services with a custom context will be copied over to a new metadata record.
Any pre-existing metadata records will be left intact.

## Running the script

By default the script will attempt to connect to Meridian/Horizon instance running on the localhost with default credentials.
If you would like to customize the server and credentials, you can either modify the script or create a `.env` file and set `onms_host`, `onms_user`, and `onms_pass` environment variables prior to running the script.

```py
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade -r requirements.txt
python3 metadata_convert.py
```
