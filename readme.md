# Docker GPU test

Simple repo to test nvidia-docker using a pytorch image

## Build

```
$ docker build -t gpu-test .
```

## Run

```
$ docker run --gpus all gpu-test .
```