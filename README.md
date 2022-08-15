# README #

This README would normally document whatever steps are necessary to get your application up and running.

**This is a ready-to-use graphql authentication authorization API. This is under development phase**

### What is this repository for? ###

* The whole api architech
* 1.0
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up

Beginning of the backend server. This is a django application exposing GraphQL APIs.
Mutaions -> Write operations.
Queries -> Read operations.

* Database configuration

1. Install postgresql in local machine. 
```
brew install libpq
```
for [ref](https://stackoverflow.com/questions/44654216/correct-way-to-install-psql-without-full-postgres-on-macos)

start services using `brew service start postgres` command.

2. Craate a user ( or exisiting user can be used)
3. create local db
4. run all sql scripts from core/assets folder.

__Note: Do not run migration on DB. we don't create tables using migrations, we create manually by running scripts. This is give us more freedom on manipulation db tables and views.__

* Running Server
1. Create a virtual env on the root folder.
```
virtualenv venv
```
If you're naming it different than `venv` then please put it in `.gitignore` file. `venv` is already there.

2. Activate virtual env
```
source venv/bin/activate
```

3. Install all dependencies
```
pip3 install -r requirements.txt
```
Don't forget to put new dependencies in the `requirements.txt` file using `freeze` command. If you don't know about it, Google it. 

4. run the server
```
python manage.py runserver
``` 
### Development guidelines ###

1. Use virtual env to install all the dependencies
2. Make sure to add new dependency in `requirements.txt` file
3. DO NOT run migrations. We don't do that here. running server might give you warning stating that you have unapplied migrations. you can ignore that. You have to run manually sql scrips in the database. You can do that by using 
```
\i <path-of-the-sql-script>
```
4. We use tab of 2 spaces indentation.
5. Rest of the things can be reviewed in PR.

### Who do I talk to? ###

* Subhajit and Ritwik
