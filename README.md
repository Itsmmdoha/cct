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

### How it works

cct sends a HTTP head request to the link you submit. If a website is configured with cloudflare cache, cloudflare includes `Cf-Cache-Status` header 
in every HTTP response. Based on the value of this header in the response, CCT decides wheather the response was cached on not. j

The following is a list of values and their meaning cloudflare can send in the `cf-cache-status` header. It was collected from cloudflare
official [documentation](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/#cloudflare-cache-responses)


| Value | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HIT            | The resource was found in Cloudflare’s cache.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| MISS           | The resource was not found in Cloudflare’s cache and was served from the origin web server.                                                                                                                                                                                                                                                                                                                                                                      |
| NONE/UNKNOWN   | Cloudflare generated a response that denotes the asset is not eligible for caching. This may have happened because: A Worker generated a response without sending any subrequests. In this case, the response did not come from the cache, so the cache status will be none/unknown. A Worker request made a subrequest (fetch). In this case, the subrequest will be logged with a cache status, while the main request will be logged with none/unknown status (the main request did not hit the cache, since Workers sit in front of the cache). A WAF custom rule was triggered to block a request. The response will come from the Cloudflare global network before it hits the cache. Since there is no cache status, Cloudflare will log as none/unknown. A redirect cache rule caused the global network to respond with a redirect to another asset/URL. This redirect response happens before the request reaches the cache, so the cache status is none/unknown. |
| EXPIRED        | The resource was found in Cloudflare’s cache but was expired and served from the origin web server.                                                                                                                                                                                                                                                                                                                                                               |
| STALE          | The resource was served from Cloudflare’s cache but was expired. Cloudflare could not contact the origin to retrieve an updated resource.                                                                                                                                                                                                                                                                                                                         |
| BYPASS         | The origin server instructed Cloudflare to bypass the cache via a Cache-Control header set to no-cache, private, or max-age=0, even though Cloudflare originally preferred to cache the asset. BYPASS is returned when enabling Origin Cache-Control. Cloudflare also sets BYPASS when your origin web server sends cookies in the response header. If the Request to your origin includes an Authorization header, in some cases, the response will also be BYPASS. Refer to Conditions in the Origin Cache-Control behavior section for more details.                   |
| REVALIDATED    | The resource is served from Cloudflare’s cache but is stale. The resource was revalidated by either an If-Modified-Since header or an If-None-Match header.                                                                                                                                                                                                                                                                                                      |
| UPDATING       | The resource was served from Cloudflare’s cache and was expired, but the origin web server is updating the resource. UPDATING is typically only seen for very popular cached resources.                                                                                                                                                                                                                                                                           |
| DYNAMIC        | Cloudflare does not consider the asset eligible to cache, and your Cloudflare settings do not explicitly instruct Cloudflare to cache the asset. Instead, the asset was requested from the origin web server. Use Cache Rules to implement custom caching options.                                                                                                                                                                                                      |




## About Me

I’m Monazir Muhammad Doha, a 19-year-old on a mission to bring his ideas to life.
Check my website [HoundSec](https://houndsec.net/)
