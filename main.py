from requests import post, get 
recaptchaURL_GET = "Your Recaptcha (GET) URL Here"
recaptchaURL_POST = 'Your Recaptcha (POST) URL Here'
tOk = get(url=recaptchaURL_GET).text.split('<input type="hidden" id="recaptcha-token" value="')[1].split('"')[0]
p = post(url=recaptchaURL_POST,data=f'v=gEr-ODersURoIfof1hiDm7R5&reason=q&c={tOk}',headers={'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Accept': '*/*','accept-language': 'fa,en;q=0.9,en-GB;q=0.8,en-US;q=0.7','Connection': 'keep-alive','origin': 'https://www.google.com','referer': 'https://www.recaptcha.net/recaptcha/api2/anchor?ar=1&k=6LcCR2cUAAAAANS1Gpq_mDIJ2pQuJphsSQaUEuc9&co=aHR0cHM6Ly9zaG9wLnRoZWh1bWFuYmVhbi5jb206NDQz&hl=en&v=gEr-ODersURoIfof1hiDm7R5&size=invisible&cb=gqhc1c3tmjz','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','Content-Type': 'application/x-www-form-urlencoded'})
recaptchaToken = p.text.split('["rresp","')[1].split('"')[0]
