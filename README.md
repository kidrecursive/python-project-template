# Python Project Template

A project template that helps enforce python project best practices.

### Pre-requisites

Docker (or a python virtualenv)

### Resources

Recommended team [git Workflow](https://nvie.com/posts/a-successful-git-branching-model/)

### Testing

Testing is done with [nosetests](https://nose.readthedocs.io/en/latest/). Tests should be placed in the `tests` folder and the testing package structure should mirror the package that is being tested.

Running tests:
```bash
nosetests --rednose -P -v --cover-package=app --with-coverage --cover-erase --nocapture
```

### CI/CD

Integration and delivery is handled using [Github Actions](https://github.com/features/actions). Place worfklows in the `.github/workflows` directory.
