from bs4 import BeautifulSoup
import requests

class Auth:
  def __init__(self, url) -> None:

    self.url = url
    self.cookies = {}


  def login(self, username, password):

    html = requests.get(self.url + "/Login.aspx")
    html = BeautifulSoup(html.text, "html.parser")

    __VIEWSTATE = html.body.find('input', attrs={'id':'__VIEWSTATE'}).get('value')
    __VIEWSTATEGENERATOR = html.body.find('input', attrs={'id':'__VIEWSTATEGENERATOR'}).get('value')
    __EVENTVALIDATION = html.body.find('input', attrs={'id':'__EVENTVALIDATION'}).get('value')

    
    data = {
      "__VIEWSTATE" : __VIEWSTATE,
      "__VIEWSTATEGENERATOR" : __VIEWSTATEGENERATOR,
      "__EVENTVALIDATION" : __EVENTVALIDATION,
      "txtname" : username,
      "Type" : "1",
      "txtPass" : password,
      "Button1" : "Login",
    }
    
    res = requests.post(self.url + "/Login.aspx", data=data, allow_redirects=False)

    
    self.cookies = res.cookies


  def get_user_data (self):
    req = requests.get(self.url + "/Profile/GetStudentAcademicData", cookies=self.cookies)
    return req.json()[0]

  def get_ass(self):
    pass




if __name__ == "__main__":
  print("testing auth lib")
    

  
