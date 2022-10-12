from bs4 import BeautifulSoup
import requests


def extract_wwr_jobs(keyword):
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"
    request = requests.get(
        url,
        headers={
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15'
        })
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        company = (soup.find_all('section', class_="jobs"))
        results = []
        for company_section in company:
            company_post = company_section.find_all('li', class_="feature")
            for post in company_post:
                company_name = post.find_all('span', class_="company")
                name = company_name[0]
                company_title = post.find_all('span', class_="title")
                title = company_title[0]

                #time condition
                condition = company_name[1]

                anchors = post.find_all('a')
                anchor = anchors[0]
                link = anchor['href']
                job_data = {
                    'name': name.string,
                    'title': title.string,
                    'condition': condition.string,
                    'link': "https://weworkremotely.com" + link
                }
                results.append(job_data)
        return results

    else:
        return None
