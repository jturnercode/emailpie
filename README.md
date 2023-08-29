# emailpie
Functions using python standard library to easily send emails within python code. 

## Dependencies
- python 3.11+
- pipenv (kinda for now)

## Usage

### Typical Project
Code as written today is meant to use environmental variables to setup default configuartion for email settings. If using pipenv, it will auto import configuration variables from .env file.

Default variables needed:
- MAIL_USER
- MAIL_ADDR_DEFAULT
- MAIL_SMTP
- MAIL_PASS

### Projects with Multiple Folders
If project has a larger code base, copy emailpie.py into project directory folder maybe named mylibs (as example).
Then add "PYTHONPATH = ./mylibs" to .env file. This allows interpreter to see emailpie.py. The default variables would still need to be added to .env file. 


### Send Email

Add code

## TODO
- [ ] Add readme and publish?
- [ ] Add/modify code to disable required pipenv dependancy for default os.environ[] arguments if desired(use)
- [ ] Pass list to toaddr vs string (not intuative); if os.environ[] convert to list, else pass list
- [ ] Multiple attachmets?
- [ ] Add error handling
- [ ] Test different email services


## Contact
[_jturnercode_](https://github.com/jturnercode)
