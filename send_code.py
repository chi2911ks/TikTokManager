import requests

session = requests.Session()
headers = {
    "accept": "application/json, text/javascript",
    "accept-language": "en-US,en;q=0.9,vi;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "pragma": "no-cache",
    "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Cookie": "_ttp=2LBlgV8K5FSfN7cKBGs2wpsxm3C; tt_chain_token=OipBv/BubLq1uHndQ0GfKQ==; tiktok_webapp_lang=vi-VN; tta_attr_id=0.1702053696.7310264960821493762; tta_attr_id_mirror=0.1702053696.7310264960821493762; _gcl_au=1.1.1592674035.1702053724; _ga=GA1.1.1702925613.1702053724; _rdt_uuid=1702053723905.2d78e1fe-182e-4bd4-bfa9-6f3b1d5bd615; _tt_enable_cookie=1; from_way=paid; _gcl_aw=GCL.1702113586.CjwKCAiAvdCrBhBREiwAX6-6UoNeUSSpkMoMjUioDLuIR5Lfbt9iCAGiQOCQHO1XblDs2RSihivGVhoC7ygQAvD_BwE; d_ticket_ads=096b7b20e03fa643edf9d2dc5a8a270a3ab26; sid_guard_ads=25d2ed03a2c303114d6dfd1ce86b11ef%7C1702150145%7C827494%7CTue%2C+19-Dec-2023+09%3A20%3A39+GMT; _uetvid=b788f04095e811eeae525f32ab0be9ac|bxr5yh|1702150147496|2|1|bat.bing.com/p/insights/c/p; _ga_R5EYE54KWQ=GS1.1.1702150119.3.1.1702150147.32.0.0; _ga_HV1FL86553=GS1.1.1702150119.3.1.1702150148.31.0.0; passport_csrf_token=cb57c744c3221a85315f8ac6ccab70ba; passport_csrf_token_default=cb57c744c3221a85315f8ac6ccab70ba; passport_auth_status=6bb1fa1ba456836f9a80c3849bd51816%2C; passport_auth_status_ss=6bb1fa1ba456836f9a80c3849bd51816%2C; tt_csrf_token=qfxmVeZz-bi4iUbRD0De980fEY_Vn6Rd_Y9s; ak_bmsc=6EDE8EB7F3F3C6F6EF0BAEEF922CAD97~000000000000000000000000000000~YAAQhFA7F9UB67mNAQAAiTaswhbLDOSb8vXZhTAPltNlTRvOS3MBiMXD08cVEkr5kvzq3OAAREqupYJTwzd7GIIexXcpittH7AUBzEpaPza6IdSIsZQCf/c0UKAsrlkekm6ExhiXHbES8FSWiZ/TXz1cC0bKG4h3iMehlSl5QjqfSHWjgyR7ODfY1aN4fxOJuxJlUQDNnrBa5yA0aBspXut2RywRIo6F8h5CGZ076CcP9TkK8i/jngNE7AZPhQ710yqsPQK/Fv+LOWR+EN+q8rFuBVSuorCbsI1LZP1WGH4zEQxIyZU7976KDPo0XNV4wP2mAemL//O7eAnx2bUB4aUCnzoQFisbQ6S2V27nJZ6nsv4JlaMWydVctY/vN3+b0qaSPS3G120=; multi_sids=7227953603385754667%3A569008b657e8f6e3e5cdd9cf6e2c52ff; sid_guard=81173c9e85435c6bbad3f85c4f1331ef%7C1708368091%7C21600%7CTue%2C+20-Feb-2024+00%3A41%3A31+GMT; uid_tt=948a748c1334dff8ecf79476d9301f85; uid_tt_ss=948a748c1334dff8ecf79476d9301f85; sid_tt=81173c9e85435c6bbad3f85c4f1331ef; sessionid=81173c9e85435c6bbad3f85c4f1331ef; sessionid_ss=81173c9e85435c6bbad3f85c4f1331ef; sid_ucp_v1=1.0.0-KDkxMDMwOWUyZjk5ZDI5ODcxNWI4OTlkYjRkNDU2MThkMzY4YmY0Y2EKCRDbwc6uBhizCxADGgNzZzEiIDgxMTczYzllODU0MzVjNmJiYWQzZjg1YzRmMTMzMWVm; ssid_ucp_v1=1.0.0-KDkxMDMwOWUyZjk5ZDI5ODcxNWI4OTlkYjRkNDU2MThkMzY4YmY0Y2EKCRDbwc6uBhizCxADGgNzZzEiIDgxMTczYzllODU0MzVjNmJiYWQzZjg1YzRmMTMzMWVm; odin_tt=ca1d413c7a7472774f77356267d0f1585baf6f43b77f493a41437f8f130bf7067da31eb7804e2d3e11306ae12ec13743448666bceebc3b323f5b940ad3b662049c440f12a0aab0bb53ee86f7210bef69; s_v_web_id=verify_lstb1ewu_FTmhDzj2_76P9_4Pno_9nsm_0M5GK2KeHX2I; bm_sv=31786AF01A91148F10B7AD46483175EB~YAAQZFA7Fx8rm7SNAQAAganzwha9EKoTPwczs0Yjl6SvafZlDOU4YobaaX+GJeV6BPTMN4WmgUnU9hmY4NFPdkIeb/aPgAK9Cx9irDnaqKxjGOPYGM8g+4lG/BcHyYuQAMwDD7HQbdw/4a/LKID2rP2blJIxdkym77LY9CKhexp6EVZUkBnjoisF6VuoJ+aVdBn668mkG7NZU34jJBbUC610BSRjKrtH4qM9fryzv92/nUQ0Dbw32t9w74+jU2Za~1; ttwid=1%7CZJmaN2OXKgOu7nROcPb6faBBQSKhUx8y33TrhexyYvY%7C1708372779%7C633f6a0fe963025cae92295a28432f93f7e4ddaa7bd683b49dbfa7864eb284de; msToken=3G16v6YLvVL0LtJt5V-Bz1_sRkFk_NTdWjRvBsjM2Eo309z-WAHHR7mVL5g4XAY8kZxA68TXUri3l9ly7IwqGi6sYDaQvXd5AFoN8fpuz5TPblFG536CQ4vfbPBr_58yk32QKj7nxxRHrQ==",
}
url = "https://www-useast1a.tiktok.com/passport/web/send_code/?multi_login=1&did=7289460409617827346&aid=1459&account_sdk_source=web&sdk_version=2.1.1-tiktok&language=vi&verifyFp=verify_lstb1ewu_FTmhDzj2_76P9_4Pno_9nsm_0M5GK2KeHX2I&shark_extra=%7B%22aid%22:1459,%22app_name%22:%22Tik_Tok_Login%22,%22channel%22:%22tiktok_web%22,%22device_platform%22:%22web_pc%22,%22device_id%22:%227289460409617827346%22,%22region%22:%22VN%22,%22priority_region%22:%22%22,%22os%22:%22windows%22,%22referer%22:%22https:%2F%2Fwww.tiktok.com%2Flogout%3Fredirect_url%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%22,%22root_referer%22:%22https:%2F%2Fwww.tiktok.com%2F%22,%22cookie_enabled%22:true,%22screen_width%22:1920,%22screen_height%22:1080,%22browser_language%22:%22en-US%22,%22browser_platform%22:%22Win32%22,%22browser_name%22:%22Mozilla%22,%22browser_version%22:%225.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F121.0.0.0+Safari%2F537.36%22,%22browser_online%22:true,%22verifyFp%22:%22verify_lstb1ewu_FTmhDzj2_76P9_4Pno_9nsm_0M5GK2KeHX2I%22,%22app_language%22:%22vi-VN%22,%22webcast_language%22:%22vi-VN%22,%22tz_name%22:%22Asia%2FSaigon%22,%22is_page_visible%22:true,%22focus_state%22:true,%22is_fullscreen%22:false,%22history_len%22:3%7D&msToken=0flT8cSw1FVJfgH1wmHJKPaheW5GWT2rCCb2nUqTIamHmBAeHia15uVILMFud24pWoFCf9V-hA5EVdhNMAVvxhGjHKze9j-X52jHp6pZyxubKucpFFT1n4kkTw85l-B0tDIsAPCVipui7g==&X-Bogus=DFSzswVLEef/XQ-ctoUnft9WcBjI&_signature=_02B4Z6wo00001uamiOwAAIDC5qaI7BVCFhrmpoxAANyH4b"

print(
    requests.post(
        url,
        headers=headers,
        data={
            "mix_mode": 1,
            "mobile": "2e3d3125363637363035313c34",
            "type": "3731",
            "account_sdk_source": "web",
            "aid": 1459,
            "did": "7289460409617827346",
            "is6Digits": 1,
            "is_sso": False,
            "language": "vi",
            "region": "VN",
            "fixed_mix_mode": 1,
        },
        proxies={
            "https": "http://chi2911bs:MX5DIuswQd@185.68.245.23:49155",
            "http": "http://chi2911bs:MX5DIuswQd@185.68.245.23:49155",
        },
    ).text
)
