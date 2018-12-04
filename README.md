# iReporter

**A Corruption watchdogs and incidents reporter application.**

iReporter seeks to bring more corruption cases to light by providing a very easily and accesible platform.
This platform will enable any member of the public to report a corruption incidence (red-flag) or even issues that require
government intervention (interventions).
All this while providing some degree of anonimity.

- ## API

  This App exposes endpoints that allows `Users` to report a red-flag or an intervention

- #### Available Resource Endpoints

| Method | Endpoint                                                 | Usage                                          |
| ------ | -------------------------------------------------------- | ---------------------------------------------- |
| POST   | `[hostname]:5000/api/v1/incident`                        | Create a red-flag or an intervention.          |
| GET    | `[hostname]:5000/api/v1/incident`                        | Get all red-flags or interventions.            |
| GET    | `[hostname]:5000/api/v1/incident/<incident_id>`          | Get a red-flad or an intervention.             |
| PATCH  | `[hostname]:5000/api/v1/incident/<incident_id>/location` | Update Location of a red-flag or intervention. |
| PATCH  | `[hostname]:5000/api/v1/incident/<incident_id>/comment`  | Update Comment of a red-flag or intervention.  |
| DELETE | `[hostname]:5000/api/v1/incident/<incident_id>`          | Delete a single red-flag or intervention.      |
| PATCH  | `[hostname]:5000/api/v1/incident/<incident_id>`          | Update a red-flag or intervention.             |

## instuctions [installing iReporter]

- To run on local machine git clone this project :

```
    git clone https://github.com/Ken-Mbugua/KenMbugua.iReporter.git
```

[more-details] https://help.github.com/articles/fork-a-repo/

## prerequisites

install and configure `python 3+` in your machine environment

Navigate to the folder you cloned and run:

- Creating a virtual environment

```
python3 -m venv ireporter-env
```

- Switch to the virtual environment

`source /ireporter-env/bin/activate`

before your terminal script you should see something like this:

`(ireporter-evn) Username@username/.../KenMbugua.iReporter $`

- import enviromental variables

  ```
  export PROJECT_SETTINGS="development"
  export FLASK_APP = "run.py"
  ```

```
$ pip install -r requirements.txt
```

- Configure Environment.

```
$ export APP_SETTINGS="default"
$ export DEV_DATABASE="path to your database"
$ export SECRET="Secret Key Here"
```

- Run App

```
flask run
```

The app should be accessiable via : http://127.0.0.1:5000/

## Running the tests

After all the above installation process is solved `cd` into root then `run`
`python -m pytest ./app`

this automates tests throught the project.

### Break down into end to end tests

Test for tests covereage using pytest coverage

```
python -m pytest --cov=./app
```

### And coding style tests

syle test accordeing to Pep 8 standards

```
pycodestyle app --count
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

- [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used
- [Flask-RestFull](https://flask-restful.readthedocs.io/en/latest/) - Api mini framework

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

- **Ken Mbugua** - _Initial work_ - [Ken-Mbugua](https://github.com/Ken-MbuguaiReporter)

See also the list of [contributors](https://github.com/Ken-MbuguaiReporter/KenMbuguaiReporter/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
