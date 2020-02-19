# CKAN Google Analytics

This exntension to connect the open data portal with google analytics

## Create an Analytics Account

Go to google analytics website https://analytics.google.com , Login with your google account.

Go to admin -> create account -> then fill the required information (ex: the website url).

Once you are done you will have an account ID similar to `UA-158767768-1`

## Installation

Activate your CKAN virtual environment

```bash
. /usr/lib/ckan/default/bin/activate
```

Install the ckanext-harvest Python package into your virtual environment:

```bash
cd /usr/lib/ckan/default/src/
pip install -e git+https://github.com/Abdelrahman146/ckanext-google_analytics#egg=ckanext-google_analytics
```

add the plugin in the ckan config file

```bash
sudo nano /etc/ckan/default/production.ini
```

```python
ckan.plugins = officedocs_view
ckan.views.default_views = ... officedocs_view
```

bellow `[app:main]` add your analytics account ID:

```
## Google Analytics
ckanext-google_analytics.id = [ANALYTICS ID] # ex: UA-158767768-1
```
restart CKAN to have the changes take effect:

```
sudo service apache2 restart
```

Wait for few hours and check the google analytics dashboard.
