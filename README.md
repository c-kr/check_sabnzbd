# check_sabnzbd

check_sabnzbd is a Python 3 Monitoring Plugin that checks the SABnzbd log for warnings &amp; errors via API

## Installation

Install python requests, move check_sabnzbd.py and MonitoringPlugin to your monitoring libexec directory and make it executable:

```bash
pip install requests
mv check_sabnzbd.py /usr/local/nagios/libexec/
mv MonitoringPlugin /usr/local/nagios/libexec/
chmod 755 /usr/local/nagios/libexec/check_sabnzbd.py
```

check_sabnzbd depends on MonitoringPlugin. If you use git to clone the repo, make sure you clone the submodule:

```bash
git clone --recursive https://github.com/c-kr/check_sabnzbd.git
```
## Usage

```bash
check_sabnzbd.py --hostname [HOST/IP] --api [APIKEY]
```

## Example

```bash
check_sabnzbd.py --hostname 192.168.178.123 --api 17b8e4ffbfa2f99fb1c899414580e386
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

