# GeoLocation
# NOTE: 
# 1) HTML/CSS and Leaflet Integration not developed


# Install the below Library for GDAL
sudo apt-get install binutils libproj-dev gdal-bin



## Setup
- First installed python3.9 dev tools.
    - <i>For debian based distros</i>
    1) <code>sudo apt-get install python3.9 python3.9-dev python3.9-venv</code>
        <br>
    <b>These all steps are same on every *nix based systems.</b>
    2) clone the repository.
    3) change to project dir.
    4) create virtual environment. <br>
        i) <code>python3 -m venv venv</code> <br> 
        ii) <code>source venv/bin/activate</code>
    5) create a file .env and put all system secrets there. <br>
    6) Install all requirements. <br>
        i) <code>pip install -r requirements.txt</code>
    7) Run Development server <br>
        i) <code>python manage.py runserver</code>
