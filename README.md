# Continuous Integration for a Production-Ready Dockerized Django App with CircleCI and CodeCov

[![CircleCI](https://circleci.com/gh/CIRCLECI-GWP/dockerized-django-demo.svg?style=svg)](https://github.com/CIRCLECI-GWP/dockerized-django-demo)

<p align="center"><img src="https://avatars3.githubusercontent.com/u/59034516"></p>

End-to-end tutorial of CI for production-ready Dockerized Django 3.2 on CircleCI 2.1

## Clone the repository:

run the following command on your terminal to clone the repository:

```bash
git clone git@github.com:CIRCLECI-GWP/dockerized-django-demo.git

cd dockerized-django-demo
```

## Running the test locally

Go into the bash of your Docker container for the Django and run tests.

```bash
$ cd dockerized-django-demo-circleci
$ docker-compose -f local.yml run web_django bash
```

Now, run the tests.

```bash
root@abc77c0122b3:/code# python3 manage.py test --keepdb
```

### About CircleCI Guest Writer Program

Reviewers: [Ron Powell][ron], [Stanley Ndagi][stan], [Amos Omondi][amos]

[ron]: https://github.com/ronpowelljr
[stan]: https://github.com/NdagiStanley
[amos]: https://github.com/amos-o
