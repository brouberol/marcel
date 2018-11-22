# Marcel, the french Docker - Marcel, le docker français
[![Build Status](https://travis-ci.org/brouberol/marcel.svg?branch=master)](https://travis-ci.org/brouberol/marcel) [![Coverage Status](https://coveralls.io/repos/github/brouberol/marcel/badge.svg)](https://coveralls.io/github/brouberol/marcel?branch=master)

![logo](https://brouberol.github.io/marcel/images/logo/marcel-logo-yellow.png)

Marcel is a french wrapper around the docker CLI, intended as a drop-in replacement of docker, for the future french sovereign operating system.

## Examples

* ``docker run`` → ``marcel chauffe``
* ``docker images`` → ``marcel cederoms``
* ``docker login`` → ``marcel vos-papiers``
* ``docker logs`` → ``marcel bûches``
* ``docker pause`` → ``marcel rtt``
* ``docker suspend`` → ``marcel grève``
* ``docker tag`` → ``marcel graffiti``
* ``docker rmi`` → ``marcel rsa``

## Dockerfile

Obviously, the ``Dockerfile`` name is not sovereign enough for us. That's why instead of ``Dockerfile``s, marcel uses ``RecetteÀMarcel`` files.
For now, they use the exact same syntax as ``Dockerfile``, but we'll see about that.

For it to work, you just need to include a ``RecetteÀMarcel`` file in the current directory where you execute your ``marcel construis`` command, are you're good to go.

## Contributing.

First of all, thanks for even considering contributing to the splendor of the French tech industry. You'll need to install the dev dependencies in your virtualenv:

```bash
$ pip install -r requirements/dev.txt
```

Then, create a branch from master and commit your feature (and tests please :). You can test that everything works correctly by running the ``tox`` command.
When all tests are green, push your feature, and create a pull request. Thats it!

## How is marcel related to the french OS ?

This project aims at providing an acceptable technology background on which the Great OS (not firewall) of France could be based on. Take a look at [the official document](http://www.assemblee-nationale.fr/14/amendements/3318/CION_LOIS/CL129.asp) to see how compliant and willingfull to help we are, already developing the technologies for the OS of tomorrow, just like RedStar OS is. Help us make the World better by destroying non-compliant operating systems, e.g. thoses who includes encryption without backdoors.

## Thanks
The [original idea](https://github.com/docker/docker/issues/19396) came of [@ndeloof](https://github.com/ndeloof)'s mind.
The logo was provided by [jkneb](https://github.com/jkneb).
