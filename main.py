import requests
from bs4 import BeautifulSoup as scrapy
from urllib.parse import urlparse
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from flask import Flask, request, send_from_directory
import os
import json

#app flask mak api function
app = Flask(__name__)

# Create the ThreadPoolExecutor outside the fast_download function.
executor = ThreadPoolExecutor()


@app.route('/', methods=['GET'])
def home():
  return """<!DOCTYPE html>
<html>
<head>
    <style>
        /* CSS styles */
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 20px;
        }

        h1 {
            color: #333;
            font-size: 24px;
        }

        p {
            color: #666;
            font-size: 16px;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #fff;
            border-radius: 4px;
            padding: 30px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .api-link {
            color: #007bff;
            text-decoration: none;
        }

        .api-link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>How to Use this API?</h1>
        <p>
            To use the API, make a GET request to the following URL:
            <br>
            <a href="https://webpage.com/apii?url=(pdf_url)" class="api-link">https://webpage.com/apii?url=(pdf_url)</a>
        </p>
        <p>
            Replace "(pdf_url)" in the URL with the actual URL of the PDF file you want to retrieve data from.
        </p>
    </div>
</body>
</html>
"""


def quizlet(url):
  try:
    cookies = {
        'qi5': '1knm1mtzmpj42%3Ae4EffS4RH661BOPJoOOm',
        'fs': 's4m8f4',
        'sp': 'e5c40354-4288-4db2-9e99-87f3bd030505',
        '_pbjs_userid_consent_data': '6683316680106290',
        '_sharedID': '55c77923-7219-471c-8278-c911d248ecd8',
        '_gcl_au': '1.1.1786758440.1700814294',
        '_gid': 'GA1.2.235250262.1700814295',
        '_cc_id': 'b5fc82da5e1767e4722d822fb6b883f7',
        'panoramaId':
        '01d4e7e32431c1fa59d12e8146084945a702ff45d713ee5de9abe8a5228467f2',
        'panoramaIdType': 'panoIndiv',
        'panoramaId_expiry': '1701419094088',
        'app_session_id': 'd022184b-ff8e-44bd-b1a2-e70321844b69',
        '__cf_bm':
        'CPJuApr.6.Tv0zwz3e8.HPtEIPF0erz9oLSKKI7kcpE-1700843645-0-ASDlnWeHY7BszfXkXQqSgbwtykDxL1JpENvpWjP45bcVTCbnDB1dkOpwwrQBa6ojJSwzmLskXJKFg7DTknNAHXo=',
        '_cfuvid':
        'yLzIHhoRYGhB5nxMDZYbV0Z67Zrsdqhjlsuqo49Zm0w-1700843645665-0-604800000',
        '_sp_ses.424b': '*',
        'session_landing_page': 'Explanations%2FtextbookExercise',
        '__cfruid': '912f75f18966d3808d89a29ab1b3b617e6056203-1700843647',
        'hide-fb-button': '0',
        'IR_gbd': 'quizlet.com',
        'IR_19930': '1700843649597%7C4442780%7C1700843649597%7C%7C',
        'IR_PI': 'f1c74fa9-8aa2-11ee-a8c4-c16465cfdc60%7C1700930049597',
        '__gads':
        'ID=6349429fe03fd816:T=1700843653:RT=1700843653:S=ALNI_MbCZC6blyHdODCVV4HJmtsfXuybIQ',
        '__gpi':
        'UID=00000c980d882029:T=1700843653:RT=1700843653:S=ALNI_MaH5L8reUDqhUPDVyam4YG8DDP_AQ',
        'afUserId': 'a7e46e8a-53c3-4ef0-a8e0-40e9fee2d059-p',
        'g_state': '{"i_l":0,"i_t":1700930056209}',
        'cf_clearance':
        '7CtXbcqEjLWtiJZY2k2v2GXFq8pVejYE5k2FFHuGt9o-1700843655-0-1-ae4f8f65.2ed2a322.f94ed085-160.2.1700808739',
        'qlts':
        '1_CW6nGKzRDlho85epK7NonNFYAXP27SURe5P7EVFfBjvXcSaR8bwKPuDRC1nsiXIac.PBvqNx4Bie3g',
        'qltj':
        'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJzdWIiOiI0Z2RyczkiLCJpc3MiOiJxdWl6bGV0LmNvbSIsImF1ZCI6InYxIn0.zTKpmw2YzsnxnWZ1VOIYFBYQvuJYrvqi8ItEUqag2jdj9iMt0Nim7zZqvbVWktti',
        'qtkn': 'wAwuYAbV5XMmhzuakrK2XY',
        'hecc': '1',
        'es_chat_callout': 'd022184b-ff8e-44bd-b1a2-e70321844b69',
        '_ga': 'GA1.2.470610412.1700814295',
        '_sp_id.424b':
        '3d4e85b4-efc2-4736-81d6-dd332c5d964c.1700814292.2.1700844138.1700814292.b9fb246b-0b80-4c13-8915-29c7baafcae8.aa3db348-945f-47da-a1ab-4f0157e18ad2.6e7eb58f-5567-4f5f-8df9-ca2c9ee70f95.1700843647414.6',
        'datadome':
        'umuOkD~G2XL4p9oEkHW7mxrcZNoBJWqTcDp_EQWVw6jP_8yfGeXJL5Xw_keK_lsTMhInqPWyB6uJvdE4aNlczsMi4WrsOgeoHjwcvWcXEjflLPjt_o7Fy9VJLpu30CBO',
        '_gat_UA-1203987-1': '1',
        '_ga_BGGDEZ0S21': 'GS1.1.1700843650.2.1.1700844139.0.0.0',
    }

    headers = {
        #'cache-control': 'max-age=0',
        #'sec-ch-device-memory': '8',
        'sec-ch-ua':
        '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-arch': '""',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-model': '"CPH2467"',
        'sec-ch-ua-full-version-list':
        '"Google Chrome";v="119.0.6045.163", "Chromium";v="119.0.6045.163", "Not?A_Brand";v="24.0.0.0"',
        'dnt': '1',
        #'upgrade-insecure-requests': '1',
        'user-agent':
        'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
        'accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer':
        'https://quizlet.com/google-one-tap-login?googleToken=eyJhbGciOiJSUzI1NiIsImtpZCI6IjBlNzJkYTFkZjUwMWNhNmY3NTZiZjEwM2ZkN2M3MjAyOTQ3NzI1MDYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE3MDA4NDMzNDgsImF1ZCI6IjUyMDMwNTA3NDk0OS5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwNjE3Mjg4OTY4OTcwNTE5ODc3MyIsImVtYWlsIjoibXVzdGtlZW1vZmZpY2lhbEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXpwIjoiNTIwMzA1MDc0OTQ5LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwibmFtZSI6Ik11c3RrZWVtIEFobWFkIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0syaXBld1dwN2VNU1VHWFlSQzlPSG1OMWI1X2dFVUprQ0ludFJyMjc5dHVRPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6Ik11c3RrZWVtIiwiZmFtaWx5X25hbWUiOiJBaG1hZCIsImlhdCI6MTcwMDg0MzY0OCwiZXhwIjoxNzAwODQ3MjQ4LCJqdGkiOiI4YzZhMmQ1ODYzODkyNGI1ZGJjNDhhNmJlMmUxN2Q5OTU1YTc3NzllIn0.e-08Wz6VewSwZgO5YzEUdZNjeGE7-CbQR2Wm8zilQ1p9fUp0f3VBs3qGXro_t6Y7bdTzwlWtTn0ou-x1bceNHYodpZYG1yZN8EVSzEoKj9KUSLHA6peCyVLsOtgi3BZJrSi_tuMzquHWL_jWYJw4eBcEZQMMtsu02smhSk0MdizsBNgm31pWSbWZjFboc6wUbYrtgmG02t_LsaJGycBJG7uB18kEds_hBZ4uzbON5XKM9KZ9bV_vxJ21cYlq85GbfBmtft91DuNno7UG9JhfDPYwXRUXJJ0iWCAIJjh4OMD1LSjGqgSMEwn2tUiLcA-pt_xIlOXSAT8RBOb1U4kRAw&autoLogin=true&from=%2Fexplanations%2Ftextbook-solutions%2Fcalculus-early-transcendentals-10th-edition-9780470647691%2Fchapter-2-exercises-12-d1e8de79-e4e2-424d-83a1-96ccc24fd0d9&isOneTapSignup=false&__cf_chl_tk=Oec7kvSSQCqdgM6XiE7eVFkJoEWnY_t_0e6tcyUn62I-1700843655-0-gaNycGzNIKU',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'qi5=1knm1mtzmpj42%3Ae4EffS4RH661BOPJoOOm; fs=s4m8f4; sp=e5c40354-4288-4db2-9e99-87f3bd030505; _pbjs_userid_consent_data=6683316680106290; _sharedID=55c77923-7219-471c-8278-c911d248ecd8; _gcl_au=1.1.1786758440.1700814294; _gid=GA1.2.235250262.1700814295; _cc_id=b5fc82da5e1767e4722d822fb6b883f7; panoramaId=01d4e7e32431c1fa59d12e8146084945a702ff45d713ee5de9abe8a5228467f2; panoramaIdType=panoIndiv; panoramaId_expiry=1701419094088; app_session_id=d022184b-ff8e-44bd-b1a2-e70321844b69; __cf_bm=CPJuApr.6.Tv0zwz3e8.HPtEIPF0erz9oLSKKI7kcpE-1700843645-0-ASDlnWeHY7BszfXkXQqSgbwtykDxL1JpENvpWjP45bcVTCbnDB1dkOpwwrQBa6ojJSwzmLskXJKFg7DTknNAHXo=; _cfuvid=yLzIHhoRYGhB5nxMDZYbV0Z67Zrsdqhjlsuqo49Zm0w-1700843645665-0-604800000; _sp_ses.424b=*; session_landing_page=Explanations%2FtextbookExercise; __cfruid=912f75f18966d3808d89a29ab1b3b617e6056203-1700843647; hide-fb-button=0; IR_gbd=quizlet.com; IR_19930=1700843649597%7C4442780%7C1700843649597%7C%7C; IR_PI=f1c74fa9-8aa2-11ee-a8c4-c16465cfdc60%7C1700930049597; __gads=ID=6349429fe03fd816:T=1700843653:RT=1700843653:S=ALNI_MbCZC6blyHdODCVV4HJmtsfXuybIQ; __gpi=UID=00000c980d882029:T=1700843653:RT=1700843653:S=ALNI_MaH5L8reUDqhUPDVyam4YG8DDP_AQ; afUserId=a7e46e8a-53c3-4ef0-a8e0-40e9fee2d059-p; g_state={"i_l":0,"i_t":1700930056209}; cf_clearance=7CtXbcqEjLWtiJZY2k2v2GXFq8pVejYE5k2FFHuGt9o-1700843655-0-1-ae4f8f65.2ed2a322.f94ed085-160.2.1700808739; qlts=1_CW6nGKzRDlho85epK7NonNFYAXP27SURe5P7EVFfBjvXcSaR8bwKPuDRC1nsiXIac.PBvqNx4Bie3g; qltj=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJzdWIiOiI0Z2RyczkiLCJpc3MiOiJxdWl6bGV0LmNvbSIsImF1ZCI6InYxIn0.zTKpmw2YzsnxnWZ1VOIYFBYQvuJYrvqi8ItEUqag2jdj9iMt0Nim7zZqvbVWktti; qtkn=wAwuYAbV5XMmhzuakrK2XY; hecc=1; es_chat_callout=d022184b-ff8e-44bd-b1a2-e70321844b69; _ga=GA1.2.470610412.1700814295; _sp_id.424b=3d4e85b4-efc2-4736-81d6-dd332c5d964c.1700814292.2.1700844138.1700814292.b9fb246b-0b80-4c13-8915-29c7baafcae8.aa3db348-945f-47da-a1ab-4f0157e18ad2.6e7eb58f-5567-4f5f-8df9-ca2c9ee70f95.1700843647414.6; datadome=umuOkD~G2XL4p9oEkHW7mxrcZNoBJWqTcDp_EQWVw6jP_8yfGeXJL5Xw_keK_lsTMhInqPWyB6uJvdE4aNlczsMi4WrsOgeoHjwcvWcXEjflLPjt_o7Fy9VJLpu30CBO; _gat_UA-1203987-1=1; _ga_BGGDEZ0S21=GS1.1.1700843650.2.1.1700844139.0.0.0',
    }

    response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
    )
    print(response.status_code)
    #print(response.text)
    soup = scrapy(response.content, 'html.parser')
    if 'https://quizlet.com/explanations/questions/' in url:
      answerhtml = soup.find('div', '</div>', class_="QuestionDetailsPage")
    elif 'https://quizlet.com/explanations/textbook-solutions/' in url:
      answerhtml = soup.find('div', '</div>', class_="ExerciseDetailPage")
    url_head = "https://nx.aba.vg/quizlet/head/head.html"
    head = requests.get(url_head)
    souphead = scrapy(head.content, 'html.parser')
    headhtml = str(souphead.prettify())
    if answerhtml is None:
      return '<p>Please try again later</p>'
    else:
      answerhtmlfile = f'<html>{headhtml}<body></body>{answerhtml}</html>'
      return answerhtmlfile
  except Exception as e:
    print(f"An error occurred: {e}")


@app.route('/apii', methods=['GET'])
def process_slideshare_api():
  try:
    with app.app_context():
      url = request.args.get('url')
      if url:
        result = quizlet(url)
        return result
      else:
        return "Error: Missing 'url' parameter.", 400
  except Exception as e:
    print(f"An error occurred: {e}")


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
