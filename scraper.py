
# this is for all the RMP Url's
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_rmp(url, output_file):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(3)  # wait for JavaScript to load
    
    reviews = driver.find_elements(By.CLASS_NAME, "Comments__StyledComments-dzzyvm-0")
    
    with open(output_file, "w") as f:
        for review in reviews:
            text = review.text.strip()
            if text:
                f.write(text + "\n\n")
    
    driver.quit()
    print(f"Saved to {output_file}")

scrape_rmp("https://www.ratemyprofessors.com/professor/2829445", "rmp_prof1.txt")
scrape_rmp("https://www.ratemyprofessors.com/professor/2233896", "rmp_prof2.txt")
scrape_rmp("https://www.ratemyprofessors.com/professor/2892587", "rmp_prof3.txt")
scrape_rmp("https://www.ratemyprofessors.com/professor/2113255", "rmp_prof4.txt")
scrape_rmp("https://www.ratemyprofessors.com/professor/3041210", "rmp_prof5.txt")

# this is for the reddit URL's
def scrape_reddit(url, output_file):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(3)
    
    comments = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='comment']")
    
    with open(output_file, "w") as f:
        for comment in comments:
            text = comment.text.strip()
            if text:
                f.write(text + "\n\n")
    
    driver.quit()
    print(f"Saved to {output_file}")

scrape_reddit("https://www.reddit.com/r/stevens/comments/1rl1talk/how_is_shudong_hao_for_cs_382/", "reddit_1.txt")
scrape_reddit("https://www.reddit.com/r/stevens/comments/zw25al/cs_course_advice/", "reddit_2.txt")
scrape_reddit("https://www.reddit.com/r/stevens/comments/1icm4xo/good_minor_classes_for_cs/", "reddit_3.txt")
scrape_reddit("https://www.reddit.com/r/stevens/comments/1sc2s2h/how_are_the_professors_for_maths_and_cs/", "reddit_4.txt")
scrape_reddit("https://www.reddit.com/r/stevens/comments/unp3nx/would_you_recommend_going_to_stevens_for_a_cs/", "reddit_5.txt")