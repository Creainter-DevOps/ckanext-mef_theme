# ckanext-mef_theme

Custom CKAN extension for a theme of MEF

## How to Install Locally for Development

1. Install CKAN from source.

2. Install ckanext-mef_theme. Activate your CKAN virtual environment and:

        git clone git@github.com:Creainter-DevOps/ckanext-mef_theme.git
        cd ckanext-mef_theme
        python setup.py develop

3. Edit the following settings to the `[app:main]` section of your CKAN config
   file (e.g. `development.ini` or `ckan.ini`):

        ckan.plugins = mef_theme

4. Run CKAN, e.g. `paster serve mef_theme.ini`

Note on CKAN versions: at the time of writing the `master` branch of
ckanext-mef_theme is intended to work with CKAN 2.0 (currently the `master`
branch of ckan).

5. Comands:
/usr/lib/ckan/default/src/ckanext-mef_theme
git pull
supervisorctl restart ckan-uwsgi:*
