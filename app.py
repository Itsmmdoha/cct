from flask import Flask,request,render_template, send_from_directory
from requests import get

app = Flask(__name__)

headers = {
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language": "en-US,en;q=0.8",
  "Connection": "close",
  "cache-control": "no-cache",
  "Referer": None,
}
states = {
    "HIT":"The resource was found in Cloudflare’s cache.",
    "MISS":"The resource was not found in Cloudflare’s cache and was served from the origin web server.",
    "EXPIRED":"The resource was found in Cloudflare’s cache but was expired and served from the origin web server.",
    "STALE":"The resource was served from Cloudflare’s cache but was expired. Cloudflare could not contact the origin to retrieve an updated resource.",
    "BYPASS":"The origin server instructed Cloudflare to bypass cache via a Cache-Control header set to no-cache,private, or max-age=0 even though Cloudflare originally preferred to cache the asset. BYPASS is returned when enabling Origin Cache-Control. Cloudflare also sets BYPASS when your origin web server sends cookies in the response header. If the Request to your origin includes an Authorization header, in some cases the response will also be BYPASS. Refer to Conditions in the Origin Cache-Control behavior section for more details.",
    "REVALIDATED":"The resource is served from Cloudflare’s cache but is stale. The resource was revalidated by either an If-Modified-Since header or an If-None-Match header.",
    "UPDATING":"The resource was served from Cloudflare’s cache and was expired, but the origin web server is updating the resource. UPDATING is typically only seen for very popular cached resources.",
    "DYNAMIC":"Cloudflare does not consider the asset eligible to cache and your Cloudflare settings do not explicitly instruct Cloudflare to cache the asset. Instead, the asset was requested from the origin web server. Use Cache Rules to implement custom caching options."
}

@app.route("/") #homepage
def home():
    r = render_template("index.html",title="Cloudflare Cache Tester - Test if Your Website is cached by Cloudflare Edge server.",description="Cloudflare Cache Tester can help you test wheather your website is cached by Cloudflare server or not. It will tell what is the state of the cache, like if it was directly served from cache or was it stale or was it dynamically fetched from the origin server and much more. Just try it!")
    return r

@app.route("/test",methods=["POST"]) # this end point is used by the form in the home page to generate shor urls
def test():
    url = request.form["url"]
    if url=="":
        return render_template("error.html",error="Invalid URL",title="Invalid URL")

    headers["Referer"] = url
    response = get(url,headers=headers)
    try:
        cache_header = response.headers["Cf-Cache-Status"]
        state = states[cache_header]
        cf_headers = {"Cf-Cache-Status":response.headers["Cf-Cache-Status"],
                      "Cache-Control":None,
                      "Cf-Ray":response.headers["Cf-Ray"]
                      }
        try:
            cf_headers["Cache-Control"] = response.headers["Cache-Control"]
        except:
            pass
    except:
        return render_template("not_cached.html")

    return render_template("details.html",status = state, cf_headers = cf_headers )

if __name__ == "__main__":
    app.run(debug=True)
