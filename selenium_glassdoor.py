from selenium import webdriver
import time
import re
import csv


#But who's flying the plane
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
driver = webdriver.Chrome(r'C:\Users\Matthew\Documents\NYCDSA\2 Data Science Boot Camp\Python\Notes\Selenium\chromedriver.exe', options=options)


#an attmept to reduce overfishing
fish = open(r'C:\Users\Matthew\Desktop\fish.txt', 'r')
fishing = fish.read()
thing = fishing.split(',')[0].strip()
pass_the_fish = fishing.split(',')[1].strip()
fish.close()

# Go to the page for login
driver.get("https://www.glassdoor.com/profile/login_input.htm")
driver.find_element_by_id('userEmail').send_keys(thing)
driver.find_element_by_id('userPassword').send_keys(pass_the_fish)
driver.find_element_by_name('submit').click()
time.sleep(3)

#Assign target file
#csv_file = open('facebook_reviews.csv', 'w', encoding='utf-8', newline='')
#csv_file = open('google_reviews.csv', 'w', encoding='utf-8', newline='')
#csv_file = open('oracle_reviews.csv', 'w', encoding='utf-8', newline='')
#csv_file = open('apple_reviews.csv', 'w', encoding='utf-8', newline='')
#csv_file = open('amazon_reviews.csv', 'w', encoding='utf-8', newline='')
#csv_file = open('twitter_reviews.csv', 'w', encoding='utf-8', newline='')
csv_file = open('microsoft_reviews.csv', 'w', encoding='utf-8', newline='')
#csv_file = open('airbnb_reviews.csv', 'w', encoding='utf-8', newline='')
#csv_file = open('snap_reviews.csv', 'w', encoding='utf-8', newline='')
#csv_file = open('uber_reviews.csv', 'w', encoding='utf-8', newline='')


writer = csv.writer(csv_file)

#Go to the page for scraping
#driver.get("https://www.glassdoor.com/Reviews/Facebook-Reviews-E40772.htm")
#driver.get("https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm")
#driver.get("https://www.glassdoor.com/Reviews/Oracle-Reviews-E1737.htm")
#driver.get("https://www.glassdoor.com/Reviews/Apple-Reviews-E1138.htm")
#driver.get("https://www.glassdoor.com/Reviews/Amazon-Reviews-E6036.htm")
#driver.get("https://www.glassdoor.com/Reviews/Twitter-Reviews-E100569.htm")
driver.get("https://www.glassdoor.com/Reviews/Microsoft-Reviews-E1651.htm")
#driver.get("https://www.glassdoor.com/Reviews/Airbnb-Reviews-E391850.htm")
#driver.get("https://www.glassdoor.com/Reviews/Snap-Reviews-E671946.htm")
#driver.get("https://www.glassdoor.com/Reviews/Uber-Reviews-E575263.htm")


# Page index
index = 1

# Get the 5000 most recent reviews
while index <= 500:
    try:
        print("Scraping Page number " + str(index))
        index = index + 1
        reviews = driver.find_elements_by_xpath('.//div[@class="gdReview"]')
        # Iterate through the list and find the details of each review.
        for review in reviews:
            # Initialize an empty dictionary for each review
            review_dict = {}
            try:
                co_name = review.find_element_by_xpath('.//img[@class="lazy lazy-loaded"]').get_attribute('alt').split()[0]
            except:
                co_name = 'NA'

            try:    
                rating = review.find_element_by_xpath('.//div[@class="v2__EIReviewsRatingsStylesV2__ratingNum v2__EIReviewsRatingsStylesV2__small"]').text
            except:
                rating = 'NA'

            try:
                emplocation = review.find_element_by_xpath('.//span[@class="authorLocation"]').text
            except:
                emplocation = 'NA'

            try:
                revdate = review.find_element_by_xpath('.//time[@class="date subtle small"]').get_attribute('datetime')
            except:
                revdate = 'NA'
            
            try:
                recommends = review.find_element_by_xpath('.//div[@class="col-sm-4 d-flex align-items-center"][1]').text
            except:
                recommends = 'NA'
            
            try:
                outlook = review.find_element_by_xpath('.//div[@class="col-sm-4 d-flex align-items-center"][2]').text
            except:
                outlook = 'NA'

            try:
                approve_ceo = review.find_element_by_xpath('.//div[@class="col-sm-4 d-flex align-items-center"][3]').text
            except:
                approve_ceo ='NA'
            
            try:
                wlbalance = review.find_element_by_xpath('.//ul[@class="undecorated"]/li[1]/span').get_attribute('title')
            except:
                wlbalance = 'NA'

            try:
                career_opportunities = review.find_element_by_xpath('.//ul[@class="undecorated"]/li[4]/span').get_attribute('title')
            except:
                career_opportunities = 'NA'
                
            #xpath debugging example:
            #print('Text = {}'.format(revdate))

            

            #Add the variables to review_dict
            review_dict['co_name'] = co_name
            review_dict['rating'] = rating
            review_dict['emplocation'] = emplocation
            review_dict['revdate'] = revdate
            review_dict['recommends'] = recommends
            review_dict['outlook'] = outlook
            review_dict['approve_ceo'] = approve_ceo
            review_dict['wlbalance'] = wlbalance
            review_dict['career_opportunities'] = career_opportunities
            
            
            writer.writerow(review_dict.values())

        # Navigate to the next page of reviews
        try:
            button = driver.find_element_by_xpath('.//a[@class="pagination__ArrowStyle__nextArrow  "]')  
            button.click()
            time.sleep(1)
        except:
            csv_file.close()
            driver.close()
            break


    except Exception as e:
        print(e)
        csv_file.close()
        driver.close()
        break
