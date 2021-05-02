# buggycar_wetpac
automation tester assessment
Automation Website: https://buggy.justtestit.org/

Framework: BDD/pyTest-bdd and POM integrated with pytest test framework & pip & python venv environment

Environments and Tools:

Python: 3.7.7
Visual Code
Google Chrome

Installed by pip
 - Selenium
 - pytest
 - pytest-bdd
 - pytest-html

Prerequisites:
step 1:
Chrome is installed, including the related chromdrivers 
the download link is https://chromedriver.chromium.org/downloads
make sure the chromdriver is in the path
check cmd "chromedriver --version"

step 2:
in the root folder of the project, execute the cmd
python3 -m venv env

step 3:
in the root folder of the project, execute the cmd
source env/bin/activate

step 4:
execute the cmd
pip install -r requirement.txt

Instructions to run:

Mac OS/Linux:

in the root folder of the project, open the terminal:
1. source env/bin/activate
2. python3 -m pytest

Windows:
in the root folder of the project, open the termial:
1. \env\Scripts\activate.bat env\bin\activate
2. python3 -m pytest


Test Reporting:

pytest-html build the report, which is located as report.html

Ps:

Since I cannot delete the registrated user, so some registation case (create new user) may be wrong.
