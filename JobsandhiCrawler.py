import scrapy
import pandas as pd

class Sandhi(scrapy.Spider):
  name = "sandhi"
  start_urls = ["file:///Users/prathameshmadur/Downloads/JS/sandhi.html"]

  def parse(self, response):

    counter = 0
    data = []
    columns=['SerialNo', 'currentCompany', 'currentLocation', 'designation', 'downloadLink', 'downloadName', 'experience', 'name',
            'preferedLocation', 'prevComapny', 'prevDesignation', 'qualification', 'resumeViewed', 'salary', 'skills']

    for responseList in response.css('.rs_list'):
      counter += 1
      name = responseList.css('.rs_2 > .black > a::text').extract_first()
      designation = responseList.css('.rs_2 > .mt10::text').extract_first().replace("\xa0", "")
      company = responseList.css('.rs_2 > .mt2::text').extract()[0].replace("\xa0", "")
      prevDesignation = responseList.css('.rs_2 > .mt2::text').extract()[1].replace("\xa0", "")
      prevComapny = responseList.css('.rs_2 > .mt2::text').extract()[2].replace("\xa0", "")
      skills = responseList.css('.rs_2 > .mt15::text').extract_first().replace("\xa0", "").replace("\r", "").replace("\n", "")
      experience = responseList.css('.rs_3 > p::text').extract()[0].replace("\xa0", "").replace("\r", "").replace("\n", "").replace("|", "")
      salary = responseList.css('.rs_3 > p::text').extract()[1].replace("\xa0", "").replace("\r", "").replace("\n", "").replace("|", "")
      qualification = responseList.css('.rs_3 > .mt2::text').extract()[0].replace("\xa0", "").replace("\r", "").replace("\n", "")
      currentLocation = responseList.css('.rs_3 > .mt2::text').extract()[1].replace("\xa0", "").replace("\r", "").replace("\n", "")
      preferedLocation = responseList.css('.rs_3 > .mt2::text').extract()[2].replace("\xa0", "").replace("\r", "").replace("\n", "")
      resumeViewed = responseList.css('.rs_3 > .mt15 > b::text').extract()[1]
      downloadLink = responseList.css('.rs_3 > .mt10 > a::attr(href)').extract_first()
      downloadName = downloadLink.replace("https://www.jobsandhi.com/members/downloadresume/", "")

      item = { "name": name,
      "designation":  designation,
      "currentCompany": company,
      "prevDesignation": prevDesignation,
      "prevComapny": prevComapny,
      "skills": skills,
      "experience": experience,
      "salary": salary,
      "qualification": qualification,
      "currentLocation": currentLocation,
      "preferedLocation": preferedLocation,
      "resumeViewed": resumeViewed,
      "downloadLink": downloadLink,
      "downloadName": downloadName,
      "Serialno": counter}

      data.append(item)

    df = pd.DataFrame(data)
    df.columns = columns
    df.to_csv('resumes.csv')
    #df.to_csv('resumes.csv', mode='a', header=False)
