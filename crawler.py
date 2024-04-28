import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")

#
# def write_company(company):
#     file = open(f"{company['name']}.csv", mode="w")
#     writer = csv.writer(file)
#     writer.writerow(["place", "title", "time", "pay", "date"])
#
#     for job in (company["jobs"]):
#         writer.writerow(list(job.values()))


alba_url = "https://www.alba.co.kr/search/Search?WsSrchWord=%EC%99%B8%EA%B5%AD%EC%9D%B8%EA%B0%80%EB%8A%A5&wsSrchWordarea=&Section=0&Page=&hidschContainText=&hidWsearchInOut=Y&hidGroupKeyJobArea=&hidGroupKeyJobHotplace=&hidGroupKeyJobJobKind=&hidGroupKeyResumeArea=&hidGroupKeyResumeJobKind=&hidGroupKeyPay=&hidGroupKeyWorkWeek=&hidGroupKeyWorkPeriod=&hidGroupKeyOpt=&hidGroupKeyGender=&hidGroupKeyAge=&hidGroupKeyCareer=&hidGroupKeyLicense=&hidGroupKeyEduData=&hidGroupKeyWorkTime=&hidGroupKeyWorkState=&hidGroupKeyJobCareer=&hidSort=FREEORDER&hidSortOrder=1&hidSortDate=rday0&hidSortCnt=20&hidSortFilter=&hidArea=&area=&hidJobKind=11000000%7C%7C%EC%9D%BC%EB%B0%98%EC%9D%8C%EC%8B%9D%EC%A0%90%2C11000000%7C%7C%EB%8F%84%EC%8B%9C%EB%9D%BD%C2%B7%EB%B0%98%EC%B0%AC%2C11000000%7C%7C%EA%B8%89%EC%8B%9D%C2%B7%ED%91%B8%EB%93%9C%EC%8B%9C%EC%8A%A4%ED%85%9C%2C11000000%7C%7C%ED%98%B8%ED%94%84%C2%B7%EC%9D%BC%EB%B0%98%EC%A3%BC%EC%A0%90%2C11000000%7C%7C%EC%B9%98%ED%82%A8%C2%B7%ED%94%BC%EC%9E%90%EC%A0%84%EB%AC%B8%EC%A0%90%2C&jobkind=%EC%99%B8%EC%8B%9D%C2%B7%EC%9D%8C%EB%A3%8C&jobkindsub=11010000&jobkindsub=11050000&jobkindsub=11090000&jobkindsub=11110000&jobkindsub=11130000&workperiod=&workweek="
alba_request = requests.get(alba_url)
alba_soup = BeautifulSoup(alba_request.text, "html.parser")
orderbyBox = alba_soup.find("div", {"class": "orderbyBox"})
jobs = orderbyBox.find_all("li")


for job in jobs:
    title = job.find("p", {"class": "title"}).text
    print(title)

