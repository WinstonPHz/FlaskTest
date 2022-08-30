This is an example of setting up a Flask Server,
and testing it using python behave,
which follows the cucumber/Gherkin format

Install Instructions.
Download the Zip or clone the git repository.

There is already a venv in the app but if you want to here is how to make a new one.
To create a new vertual environment
`python3 -m venv /{downloaded dir}/Flaskapp/venv`
This line is how you enter the vertual env, we will be using this a lot
`Source /{downloaded dir}/Flaskapp/venv/bin/activate'

There are 3 modules needed to run these scripts:

bahave
requests
Flask
`pip install <module>` sould do the trick if you sourced the activate of the venv

Now you should be ready to run these scripts
Open two terminals
In the first:
In the vertual Environment and in the /Flaskapp dir run the following
`export FLASK_APP=flaskapp.py`
`flask run`
Now the server is running!

In the second terminal, enter the vertual Environment.
Now we just need to run behave as follows:
`behave`

Behave should output the results of the test.

1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
6 steps passed, 0 failed, 0 skipped, 0 undefined

