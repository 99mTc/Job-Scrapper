from bs4 import BeautifulSoup
import requests


def extract_remoteok_jobs(keyword):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    request = requests.get(
        url,
        headers={
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15'
        })
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        company = (soup.find_all('tr', class_="job"))
        results = []
        for company_section in company:
            company_post = company_section.find_all('td', class_="company")
            company_names = company_section.find_all('h3', itemprop="name")
            company_name = company_names[0]
            for post in company_post:
                anchors = post.find_all('a', class_="preventLink")
                anchor = anchors[0]
                link = anchor['href']
                title = anchor.find('h2', itemprop="title")
                conditions = post.find_all('div', class_="location")
                condition = conditions[0]
                job_data = {
                    'name': company_name.string.replace("\n", ""),
                    'title': title.string.replace("\n", ""),
                    'condition': condition.string,
                    'link': "https://remoteok.com" + link
                }
                results.append(job_data)
        return results

    else:
        return None
