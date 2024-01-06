# CCT

![preview](https://github.com/Itsmmdoha/cct/assets/70005698/2a6e09d5-e220-4a35-aadd-d0770321eae1)

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

## About Me

I’m Monazir Muhammad Doha, a 19-year-old on a mission to bring his ideas to life.
Check my website [HoundSec](https://houndsec.net/)

