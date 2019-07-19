from selenium import webdriver


def get_results(search_term):

    url = "http://www.google.com"
    # create your webdriver
    driver = webdriver.Chrome("/Applications/chromedriver")

    # open google
    driver.get(url)

    # locate the search field
    search_box = driver.find_element_by_name('q')

    # type "foo" into search field
    search_box.send_keys(search_term)

    # execute a search
    search_box.submit()

    # locate the resultStats element
    result_stats = driver.find_element_by_id('resultStats')

    # print the text of resultStats
    print(result_stats.text)

    try:
        links = driver.find_elements_by_xpath("//ol[@class='web_regular_results']h3//a")
    except:
        links = driver.find_elements_by_xpath("//h3//a")


    next_page = driver.find_elements_by_xpath("//html/body/div[8]/div[3]/div[10]/div[1]/div[2]/div/div[5]/div/span[1]/div/table/tbody/tr/td[3]/a")
    next_page.onClick()

    results = []
    print('-------------')
    print(links)
    for link in links:
            href = link.get_attribute("href")
            print(href)
            results.append(href)
             
            
    driver.quit()
    return results

   

get_results("site:responsify.com")
 
