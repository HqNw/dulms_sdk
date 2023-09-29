from bs4 import BeautifulSoup
import requests

class Auth:
  def __init__(self, url: str) -> None:

    self.url = url
    self.cookies = {}


  def login(self, username: str, password: str) -> None:

    html = requests.get(self.url + "/Login.aspx")
    html = BeautifulSoup(html.text, "html.parser")

    __VIEWSTATE = html.body.find('input', attrs={'id':'__VIEWSTATE'}).get('value')
    __VIEWSTATEGENERATOR = html.body.find('input', attrs={'id':'__VIEWSTATEGENERATOR'}).get('value')
    __EVENTVALIDATION = html.body.find('input', attrs={'id':'__EVENTVALIDATION'}).get('value')

    
    data: dict = {
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


  def get_user_data (self) -> dict:
    req = requests.get(self.url + "/Profile/GetStudentAcademicData", cookies=self.cookies)
    return req.json()[0]

  def get_assignments(self) -> list:
    req = requests.get(self.url + "/Assignment/GetStudentAssignments", cookies=self.cookies)
    return req.json()

  def get_quizzes(self)-> list:
    req = requests.get(self.url + "/Quizzes/GetStudentQuizzes", cookies=self.cookies)
    return req.json()

  def get_cookies(self) -> dict:
    return self.cookies.get_dict()

if __name__ == "__main__":
  print("testing sdk")
    

  
