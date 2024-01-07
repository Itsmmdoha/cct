# CCT

![New Project](https://github.com/Itsmmdoha/cct/assets/70005698/12c4ba97-e666-4cd9-aea4-0236f76026ba)


Cloudflare Cache Tester or CCT in short is a web app that can tell you wheather your website is cacched by Cloudflare Edge server or not.

## How Does It Work?

It sends a HTTP get request to the given URL and checks the `Cf-Cache-Status` header value from the HTTP response. Based on the value, it can determine 
wheather the response was cached or not. Read this official [documentation](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/) by Cloudflare to better understand the comcept.

## Run Locally

clone the repository

```bash
git clone https://github.com/itsmmdoha/cct
```
cd into the repository

```bash
cd cct
```
install requirements

```bash
pip install -r requirements.txt
```
run the app.py file

```bash
python3 app.py
```
## Docker

There is prebuilt image available on dockerhub
Run it using the following command

```bash
docker run -p 8000:8000 houndsec/cct
```

or,

```bash
docker run -d -p 8000:8000 houndsec/cct
```
to run it in detached mode. This commad will automatically pull the image from dockerhub and run it.

### Build The Image Yourself

1. Clone the repo

```bash
  git clone https://github.com/itsmmdoha/cct
```
2. change directory
```bash
cd cct
```
3. Build the image

```bash
docker build -t houndsec/cct .
```
4. Rut it
```bash
docker run -p 8000:8000 houndsec/cct
```
or

```bash
docker run -d -p 8000:8000 houndsec/cct
```
To run in detached mode
Then open [http://localhost:8000](http://localhost:8000)


## About Me

I’m Monazir Muhammad Doha, a 19-year-old on a mission to bring his ideas to life.
Check my website [HoundSec](https://houndsec.net/)
