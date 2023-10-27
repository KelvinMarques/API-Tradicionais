from selenium import webdriver
from selenium.webdriver.common.by import By
import feedparser
import time


import json
from multiprocessing import Pool

# Funções do script
def getNews(driver, site):
    site
    pass

def getNewsPain(driver):
#Função que tem como objetivo entrar e retornar os dados das noticias mais recentes da paiN Gaming

    NewsPain = []
    OneNew = {}

    #NewsPain = [
        # OneNew{
            # company
            # title
            # desc
            # data
            # link
            # imagemURL
        # },
        # OneNew{
            # company
            # title
            # desc
            # data
            # link
            # imagemURL
        # },
    # ]


    #Entra na pagina de noticias do google com o tema paiN Gaming
    driver.get("https://www.google.com/search?q=pain+gaming&sca_esv=573047317&tbm=nws")
    
    # bodyNews = driver.find_element(by=By.ID, value="center_col")
        
    allNews = driver.find_elements(by=By.CLASS_NAME, value="SoaBEf")

    for a in allNews:
        moreInfo = a.find_elements(By.TAG_NAME, "a")
        company = a.find_element(By.TAG_NAME, "span")
        title = a.find_element(By.CLASS_NAME, "n0jPhd")
        desc = a.find_element(By.CLASS_NAME, "GI74Re")
        data = a.find_element(By.CLASS_NAME, "OSrXXb")
        for info in moreInfo:
            link = info.get_attribute('href') 
        thumb = a.find_element(By.TAG_NAME, "img").get_attribute('src')

        OneNew = {
            "company": company,
            "title": title,
            "desc": desc,
            "data": data,
            "link": link,
            "imagemURL": thumb,
        } 
        NewsPain.append(OneNew)
        print(company.text)
        print(title.text)
        print(desc.text)
        print(data.text)
        # print(link)
        # print(thumb)
        time.sleep(1)

    
    return NewsPain

# def salvar_json(noticia):
#     # Nome do arquivo JSON (pode ser único para cada notícia ou seguir algum padrão)
#     nome_arquivo = f"{noticia['company']}.json
    
#     with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
#         json.dump(noticia, arquivo, ensure_ascii=False, indent=4)




if __name__ == '__main__':
    # parserFeed()    
    # Inicio do script
    driver = webdriver.Chrome()

    lista_noticias = getNewsPain(driver)
    # json_news = salvar_json(lista_noticias)
    # print(json_news)






    