statement = "The URL the where build the results of this build can be found (for build example http://buildserver/build/jenkins/job/MyJobName/17/ )"

lst1 = statement.split()
dic1 = {}
for word in lst1:
    if word in dic1:
        dic1[word] += 1
    else:
        dic1[word] = 1
print(dic1)



logs = ["103.212.20.91 - - [21/Jan/2021:10:56:27 +0000] GET /api/v1/conversations/by_user_id HTTP/1.1 304 0 http://console.abc.com/customer_support/chats?in_iframe=false Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "10.0.1.163 - - [21/Jan/2021:10:56:27 +0000] GET / HTTP/1.1 200 393 - ELB-HealthChecker/2.0",
        "2409:4053:2184:dab7:bca1:3fe2:c919:8124 - - [21/Jan/2021:10:56:28 +0000] GET /.well-known/apple-app-site-association HTTP/1.1 200 442 - swcd (unknown version) CFNetwork/1126 Darwin/19.5.0",
        "13.126.100.180 - - [21/Jan/2021:10:56:29 +0000] GET /users?labs=true HTTP/1.1 200 351 - Python/3.4 aiohttp/0.20.2",
        "35.154.35.163 - - [21/Jan/2021:10:56:29 +0000] GET /nginx_status HTTP/1.1 301 178 - Go-http-client/1.1",
        "13.126.100.180 - - [21/Jan/2021:10:56:29 +0000] GET /addresses/805601?labs=true HTTP/1.1 200 493 - Python/3.4 aiohttp/0.20.2",
        "35.154.35.163 - - [21/Jan/2021:10:56:29 +0000] GET /nginx_status HTTP/1.1 404 22224 http://stag.abc.com/nginx_status Go-http-client/2.0",
        "10.0.31.172 - - [21/Jan/2021:10:56:29 +0000] GET / HTTP/1.1 200 393 - ELB-HealthChecker/2.0",
        "10.0.7.72 - - [21/Jan/2021:10:56:29 +0000] GET / HTTP/1.1 200 393 - ELB-HealthChecker/2.0",
        "13.126.100.180 - - [21/Jan/2021:10:56:30 +0000] GET /addresses/805601?labs=true HTTP/1.1 200 493 - Python/3.4 aiohttp/0.20.2",
        "13.233.80.186 - - [21/Jan/2021:10:56:30 +0000] GET /labs/.well-known/apple-app-site-association HTTP/1.1 200 442 - swcd (unknown version) CFNetwork/1128.0.1 Darwin/19.6.0",
        "2405:205:1488:d807:b00a:9d73:3c42:11a1 - - [21/Jan/2021:10:56:30 +0000] GET /.well-known/apple-app-site-association HTTP/1.1 200 447 - swcd (unknown version) CFNetwork/1128.0.1 Darwin/19.6.0",
        "13.233.80.186 - - [21/Jan/2021:10:56:30 +0000] PUT /cart/collection_time/pathology HTTP/1.1 200 1970 https://abc.com/labs/cart Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
        "103.41.25.90 - - [21/Jan/2021:10:56:30 +0000] PUT /cart/collection_time/pathology HTTP/1.1 200 1958 https://abc.com/labs/cart Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
        "13.126.100.180 - - [21/Jan/2021:10:56:30 +0000] GET /users?labs=true HTTP/1.1 200 351 - Python/3.4 aiohttp/0.20.2",
        "10.0.1.163 - - [21/Jan/2021:10:56:30 +0000] GET /users?labs=true HTTP/1.1 200 351 - Python/3.4 aiohttp/0.20.2",
        "103.41.25.90  - - [21/Jan/2021:10:56:30 +0000] GET /addresses/805601?labs=true HTTP/1.1 200 484 - Python/3.4 aiohttp/0.20.2",
        "13.126.100.180 - - [21/Jan/2021:10:56:31 +0000] GET /payment_details?mode=PAYTM&client=APP&order_id=SSO2686913742-423&transaction_app=DIAGNOSTICS&email=deepanshu.rawat@abc.com&mobile_no=9820002423&txn_amount=1148.0&coupon_code=TAX HTTP/1.1 200 349 - python-requests/2.21.0",
        "10.0.1.163 - - [21/Jan/2021:10:56:31 +0000] GET /wallet/get-balance HTTP/1.1 200 213 - Python/3.4 aiohttp/0.20.2",
        "13.233.80.186 - - [21/Jan/2021:10:56:31 +0000] PUT /cart/checkout HTTP/1.1 200 2443 https://abc.com/labs/cart Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
        "103.41.25.90 - - [21/Jan/2021:10:56:31 +0000] PUT /cart/checkout HTTP/1.1 200 2431 https://abc.com/labs/cart Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
        "10.0.30.187 - - [21/Jan/2021:10:56:31 +0000] GET / HTTP/1.1 200 393 - ELB-HealthChecker/2.0",
        "10.0.4.185 - - [21/Jan/2021:10:56:31 +0000] GET /__onemg-internal__/v1/conversations/realtime_dashboard_details?business_unit=ecom HTTP/1.1 200 4041 - Tpheus - https://github.com/typhoeus/typhoeus",
        "111.93.242.218 - - [21/Jan/2021:10:56:31 +0000] GET /api/v1/chats/performance_matrixes/realtime_dashboard_details.json?business_unit=ecom HTTP/1.1 200 1211 http://abc.com/customer_support?in_iframe=false Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",

        "111.93.242.218 - - [21/Jan/2021:10:56:31 +0000] GET /api/v1/customer_support HTTP/1.1 200 1211 http://stagcs-console.abc.com/customer_support?in_iframe=false Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"]


lst2 = []
dic2 = {}

for line in logs:
    lst2.append(line.split("- -")[0])

for ip in lst2:
    if ip in dic2:
        dic2[ip] += 1
    else:
        dic2[ip] = 1

print(dic2)
