# SendGrid

SendGrid is an email sending service used to send email through softwares.

This application uses SendGrid to send emails.

## Prerequisites:

You will need the following programmes properly installed on your computer.

* [Python](https://www.python.org/) 3.6+
* [Virtual Environment](https://pypi.org/project/virtualenv/)

To install virtual environment on your system use:

```bash
pip install virtualenv

or

pip3 install virtualenv #if using linux(for python 3 and above)
```
* [SendGrid](https://sendgrid.com/) API key

To get the email application to work you would need to [create](https://sendgrid.com/docs/ui/account-and-settings/api-keys/#creating-an-api-key) and [use](https://sendgrid.com/docs/for-developers/sending-email/django/) an API key for Sendgrid.
## Installation:

```bash
git clone https://github.com/ongraphpythondev/SendgridEmail.git

cd SendgridEmail

virtualenv venv
      or
virtualenv venv -p python3 #if using linux(for python 3 and above)

venv\Scripts\activate # for windows
      or
source venv/bin/activate # for linux

# install required packages for the project to run
pip install -r requirements.txt
```
In Project directory's SendgridEmail/settings.py file you would need to either change
```python
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
```
to
```python
SENDGRID_API_KEY = '<The API key provided by SendGrid>'
```
or define SENDGRID_API_KEY in environment variables as the key provided by sendgrid.

## Running:

To run the development server after installation:
```bash
# activate the virtual environment
venv\Scripts\activate # for windows
      or
source venv/bin/activate # for linux

# run server
python manage.py runserver
```
