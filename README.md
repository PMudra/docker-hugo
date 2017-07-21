# Hugo Docker Images

Lightweight [Docker](https://www.docker.com/) images for the static site generator [Hugo](http://gohugo.io/).

## How to use this image

### Scaffold your Hugo bookshelf website

```
$ docker run --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp pmudra/hugo new site bookshelf
```

### Serve content

```
$ docker run -it --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp -p 1313:1313 pmudra/hugo server --bind=0.0.0.0
```
