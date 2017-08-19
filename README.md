# Hugo Docker Images

[![Docker Build Statu](https://img.shields.io/docker/build/pmudra/hugo.svg)](https://hub.docker.com/r/pmudra/hugo/)

Lightweight [Docker](https://www.docker.com/) images for the static site generator [Hugo](https://gohugo.io/).

## How to use this image

Basically, the Hugo Docker image is used the same way as the Hugo CLI itself.
See the official [basic usage](https://gohugo.io/getting-started/usage/) page for a more detailed explanation.

### Get help and version

```
$ docker run --rm pmudra/hugo help
$ docker run --rm pmudra/hugo version
```

Command/Option   | Description
-----------------|------------
`docker run`     | Run a command in a new container
`--rm`           | Automatically remove the container when it exits
`pmudra/hugo`    | Name of the Hugo Docker image
`help`/`version` | Hugo CLI commands (i.e. same as running `hugo help`/`hugo version`)

### Create a new site

```
$ docker run --rm --mount type=bind,source="$(pwd)",target=/usr/src/myapp -w /usr/src/myapp pmudra/hugo new site quickstart
```

Command/Option          | Description
------------------------|------------
`--mount type=bind,`    | Attach a filesystem mount to the container
`source="$(pwd)",`      | Path to the directory on the host i.e. the path of the current working directory
`target=/usr/src/myapp` | Path where the directory will be mounted in the container
`-w /usr/src/myapp`     | Working directory inside the container
`new site quickstart`   | Create a new Hugo site named *quickstart*

The above will create a new Hugo site in a folder named *quickstart*. 

### Serve content

```
$ cd quickstart
$ docker run -it --rm --mount type=bind,source="$(pwd)",target=/usr/src/myapp -w /usr/src/myapp -p 1313:1313 pmudra/hugo server --bind=0.0.0.0
```

Command/Option   | Description
-----------------|------------
`-it`            | Keep STDIN open even if not attached and allocate a pseudo-TTY
`-p 1313:1313`   | Publish the container's port to the host
`--bind=0.0.0.0` | Bind to all interfaces (this enables the docker host to access the site)

The above builds and serves the site.
Web Server is available at [http://localhost:1313/](http://localhost:1313/).

Remember to [add a theme](https://gohugo.io/getting-started/quick-start/#step-3-add-a-theme) before expecting to see anything else than a blank page.
