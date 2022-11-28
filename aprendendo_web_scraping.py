#o codigo a seguir foi aprendido e reproduzido baseado na video aula: https://www.youtube.com/watch?v=XEGa6wVh8Sk, sendo um codigo base que ta com o objetivo de fins de se estudar e aprender sobre Web Scraping, ja que o mesmo possui como o autor mesmo disse o coracao da pratica

#biblioteca que permite fazer uma requisicao ao site google.com, que no caso se trata do site escolhido
import requests

#BeautifulSoup ele vai praticamente decodificar o html e vai permitir que navegue e extraia os elementos do html do codigo em si de uma maneira mais facil
from bs4 import BeautifulSoup

#funcao basica que deveria extrair as noticias desse site
def get_Noticias():
  #link/url do site principal da onde voce quer extrair informacoes
  link= 'https://www.globo.com/'

  #fazendo uma requisicao dos dados dessa pagina pelo google, para poder extrailos e utilizalos
  pagina=requests.get(link)

  #funcao que serve para puxar os dados de forma mais organizada, sendo importante passar o parser que nesse caso se trata do html, que seria o formato do site em questao
  soup= BeautifulSoup(pagina.text, 'html.parser')

  #noticias aqui, vai ser pegando todos os que tem o a, vai ser preciso filtra mais tarde, afinal nem todos sao os links que se precisa ou deseja, sendo que sera extraindo assim porque os links ficam com a tag 'a'
  noticias= soup.find_all('a')

  #basicamente, um ponto vital para fazer a estracao de uma determinada informacao em especifico ou de varias, se trata de quando voce consegue pegar e entender o padrao html que aquela determinada informacao costuma aparecer, nesse caso caso de exemplo, seria dentro do 'a' e quando a tag ta com o h2 e com o nome de post_title
  tgt_class1= 'post_title'
  
  #ja nessa outra informacao, que aparece de outra forma no site, se trata de quando ta dentro do 'a' e quando o h2 tem escrito post-multicontent_link-title_text
  tgt_class2= 'post-multicontent_link-title_text'

  #dicionario para fazer a ligacao de chave e valor, nesse caso a chave sendo o nome da noticia, e o valor o link da mesma
  noticias_dicionario={}

  #aqui seria justamenta fazendo o percorrimento das extracoes do tipo soup e verificando se estao dentro dos padroes explicados a cima, para que caso atendam a aquelas requisicoes sejam adicionadas no dicionario
  for noticia in noticias:
    if (noticia.h2 !=None) and noticia.h2.get('class'):
      if tgt_class1 in noticia.h2.get('class'):
        noticiais_dicionario[noticia.h2.text]=noticia_get('href')
        
      if tgt_class2 in noticia.h2.get('class'):
        noticiais_dicionario[noticia.h2.text]=noticia_get('href')
  return noticias_dicionario

#a variavel que recebe o dicionario noticias, o mesmo pode ser feito varias coisas, desde ver a quantidade de noticias, o len, ou transformar em lista com a funcao list e pegar alguma noticia em especifico baseado em posicao, ou varias outras coisas, estando a disposicao da criatividade
news=get_Noticias()
len(news)
      
